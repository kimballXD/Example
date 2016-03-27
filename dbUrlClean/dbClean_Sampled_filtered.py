import sys
import datetime
import re
import MySQLdb
import requests
import pandas as pd
import multiprocessing.dummy as mt
from dbCleanUtil import *


def getFloatArg(arg):
    return float(re.findall('\d+',arg)[0])

if __name__ == '__main__':
    mt.freeze_support()    
    sampleSize=int(getFloatArg(sys.argv[1]))
    sampleSize=sampleSize if sampleSize%2==0 else sampleSize+1
    repeat=int(getFloatArg(sys.argv[2]))
    repeat=sys.maxint if repeat==0 else repeat

    for i in xrange(repeat):
        start=datetime.datetime.now()
        #get data from database
        connection = MySQLdb.connect(host="localhost",user="root",passwd="mysql123",db="zb102" )
        cur=connection.cursor()
        try:    
            cur.execute('SELECT hid, website FROM houseTestAll WHERE NOT (lastUpdate BETWEEN DATE_SUB(now(),INTERVAL 12 HOUR) AND now()) AND (resFailCount<1) ORDER BY lastupDate;')
            hidResult=cur.fetchall()
            if len(hidResult)>=sampleSize:             
                hidResult=pd.DataFrame(list(hidResult),columns=['hid','website'])
            else:
                print 'The record waiting for updating is less the than update volumn per cycle: {}/{} records. Suspend for 5 minutes.'.format(len(hidResult), sampleSize)
                time.sleep(300)
                continue
            hidsubSampleList=[]
            hidsubSampleList.append(hidResult[0:sampleSize/2]) # half of the sample came from updated time order
            hidsubSampleList.append(getSampleByCol(hidResult[sampleSize/2:],'website',sampleSize/2,proportional=True)) #the other half came from sampling
            hidSample=hidsubSampleList[0].append(hidsubSampleList[1])
            hidList=[str(x) for x in hidSample['hid'].tolist()]
            cur.execute('SELECT hid, website, URL, resFailCount FROM houseTestAll WHERE hid in ({})'.format(','.join(hidList)))
            data=pd.DataFrame(list(cur.fetchall()),columns=['hid','website','URL','resFailCount']).sample(sampleSize)
        finally:
            connection.close()

        #prepare dataList for multithread module
        dataList=[]
        resultList=[]
        for index, row in data.iterrows():
            result=([row.URL,row.website],{'multithread':True,'hid':row.hid,'resultList':resultList})
            dataList.append(result)
           
        #multithread!
        try:
            pool= mt.Pool(5)           
            [pool.apply_async(urlValidate, item[0], item[1]) for item in dataList]
            pool.close()
            pool.join()

        except:
            excType, excValue, excTB=sys.exc_info()
            print '====Waring==== dbUrl cleaning job cycle {} failed due to {}.Message: {}'.format(i,excType, excValue)        
            continue
        
        #data transform
        resultFrame=pd.DataFrame(resultList, columns=['hid','valid'])
        resultFrame=pd.merge(data,resultFrame,on='hid')
        resultFrame['resFailCount']=resultFrame.apply(lambda x: 0 if x['valid']==1 else x['resFailCount']+1,axis=1)
        sucess=int((resultFrame['resFailCount']!=(-1)).sum())

        #write back to database
        try:
            connection = MySQLdb.connect(host="localhost",user="root",passwd="mysql123",db="zb102" )
            cur=connection.cursor()
            for index, row in resultFrame.iterrows():       
                cur.execute('UPDATE houseTestAll SET resFailCount={},valid={},lastUpdate=now() WHERE hid={};'
                               .format(row['resFailCount'],row['valid'],row['hid']))  
            connection.commit()
        finally:
            connection.close()
        
        #print log
        end=datetime.datetime.now()
        delta=end-start
        print 'A dbUrl cleaning job cycle is done! Cycle {}: send {} request in {}, average {:.1f} per minute'.format(i,len(data),delta, len(data)/(delta.total_seconds()/60.0))
        print 'Updated {} records sucessfully, remain {} records waiting for updating'.format(sucess, len(hidResult)-sucess)
        if i+1==repeat:
            print 'job has done!'
        else:
            time.sleep(30)
    