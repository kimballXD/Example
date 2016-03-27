
websiteList=['sinyi', 'hbhousing', 'yungching', 'pacific', 'sale591', 'utrust', 'houseFun']

_sinyi_header={'Cookie':'__uid=wKgIalW+E5q8OwVgDfr5Ag==; SINYI_guestID=79fde69786d3ae7a420ea4689135faaa; _gat=1; SYL_ID=55bf4db1285f1; _ga=GA1.3.1175027947.1438600447; _ga=GA1.4.1175027947.1438600447; __uwait=0'}

_houseFun_header={'Cookie':'TRID_G=cdb3a978-1241-4d23-aab3-5928a45b1f3a; SEID_G=31e7380b-f000-4012-8832-91a47a26bab1; ASP.NET_SessionId=ylavmh5vmfy1hndeffsda4gn; _dc_gtm_UA-22823074-10=1; _dc_gtm_UA-34471860-1=1; __ltmwga=utmcsr=google|utmcmd=organic; _ga=GA1.3.1094928032.1440262690; _gat_UA-22823074-10=1; CSCWORM_UNID=1443947324361361; _dc_gtm_UA-22823074-5=1; WMX_Channel=,3,; objID=87877613; _gat_UA-22823074-5=1; __asc=0243717e15031f7549b38c3d503; __auc=51d30b2f14f563c5853beb572d9; _ga=GA1.4.1046775431.1440260840; sto-id-%3Fv30%3FGroup-buy.housefun.com.tw%3A80=GCABBOKM'}

_yungching_header={'Cookie':'OvertureRecord=OR=a3d3c3Y9MjJ6enoxanJyam9oMWZycDF3ejI=&OQ=RE9PYktXV1NAS1dXU2JGUlFRSEZXTFJRKDZkbmhoczBkb2x5aCgzZygzZEtXV1NiREZGSFNXKDZkd2h7dyg1aWt3cG8oNWZkc3NvbGZkd2xycSg1aXtrd3BvKDVle3BvKDVmZHNzb2xmZHdscnEoNWl7cG8oNmV0KDZnMzE8KDVmbHBkamgoNWl6aGVzKDVmLSg1aS0oNmV0KDZnMzE7KDNnKDNkS1dXU2JERkZIU1diSFFGUkdMUUooNmRqfWxzKDVmLmdoaW9kd2goNWYudmdmaygzZygzZEtXV1NiREZGSFNXYk9EUUpYREpIKDZkfWswV1ooNWZ9ayg2ZXQoNmczMTsoNWZocTBYVig2ZXQoNmczMTkoNWZocSg2ZXQoNmczMTcoM2coM2RLV1dTYktSVlcoNmR6enoxfHhxamZrbHFqMWZycDF3eigzZygzZEtXV1NiVUhJSFVIVSg2ZGt3d3N2KDZkKDVpKDVpenp6MWpycmpvaDFmcnAxd3ooNWkoM2coM2RLV1dTYlhWSFViREpIUVcoNmRQcn1sb29kKDVpODEzLitabHFncnp2LlFXLjkxNCg2ZS5aUlo5NywuRHNzb2haaGVObHcoNWk4NjoxNjkuK05LV1BPKDVmLm9sbmguSmhmbnIsLkZrdXJwaCg1aTc4MTMxNTc4NzE0MzQuVmRpZHVsKDVpODY6MTY5KDNnKDNkS1dXU2JYU0pVREdIYkxRVkhGWFVIYlVIVFhIVldWKDZkNCgzZygzZClET09iVURaQEZycXFoZndscnEoNmQubmhoczBkb2x5aCgzZygzZERmZmhzdyg2ZC53aHt3KDVpa3dwbyg1ZmRzc29sZmR3bHJxKDVpe2t3cG8oNWV7cG8oNWZkc3NvbGZkd2xycSg1aXtwbyg2ZXQoNmczMTwoNWZscGRqaCg1aXpoZXMoNWYtKDVpLSg2ZXQoNmczMTsoM2coM2REZmZoc3cwSHFmcmdscWooNmQuan1scyg1Zi5naGlvZHdoKDVmLnZnZmsoM2coM2REZmZoc3cwT2RxanhkamgoNmQufWswV1ooNWZ9ayg2ZXQoNmczMTsoNWZocTBYVig2ZXQoNmczMTkoNWZocSg2ZXQoNmczMTcoM2coM2RLcnZ3KDZkLnp6ejF8eHFqZmtscWoxZnJwMXd6KDNnKDNkVWhpaHVodSg2ZC5rd3dzdig2ZCg1aSg1aXp6ejFqcnJqb2gxZnJwMXd6KDVpKDNnKDNkWHZodTBEamhxdyg2ZC5Qcn1sb29kKDVpODEzLitabHFncnp2LlFXLjkxNCg2ZS5aUlo5NywuRHNzb2haaGVObHcoNWk4NjoxNjkuK05LV1BPKDVmLm9sbmguSmhmbnIsLkZrdXJwaCg1aTc4MTMxNTc4NzE0MzQuVmRpZHVsKDVpODY6MTY5KDNnKDNkWHNqdWRnaDBMcXZoZnh1aDBVaHR4aHZ3dig2ZC40KDNnKDNkKURTU09iUEdiU0RXS0AoNWlPUCg1aVo2VllGKDVpNTUoNWlVUlJXKURTU09iU0tcVkxGRE9iU0RXS0BHKDZkKDhmU1VSTUhGVyg4Znp6ejF8eHFqZmtscWoxZnJwMXd6KDhmWlpaVVJSVyg4ZilEWFdLYldcU0hAKURYV0tiWFZIVUApRFhXS2JTRFZWWlJVR0ApT1JKUlFiWFZIVUApVUhQUldIYlhWSFVAKUZIVVdiRlJSTkxIQClGSFVXYklPREpWQClGSFVXYkxWVlhIVUApRkhVV2JOSFxWTF1IQClGSFVXYlZIRlVIV05IXFZMXUhAKUZIVVdiVkhVTERPUVhQRUhVQClGSFVXYlZIVVlIVWJMVlZYSFVAKUZIVVdiVkhVWUhVYlZYRU1IRldAKUZIVVdiVlhFTUhGV0ApRlJRV0hRV2JPSFFKV0tAMylGUlFXSFFXYldcU0hAKUpEV0haRFxiTFFXSFVJREZIQEZKTCg1aTQxNClLV1dTVkByaWkpS1dXU1ZiTkhcVkxdSEApS1dXU1ZiVkhGVUhXTkhcVkxdSEApS1dXU1ZiVkhVWUhVYkxWVlhIVUApS1dXU1ZiVkhVWUhVYlZYRU1IRldAKUxRVldEUUZIYkxHQDU1KUxRVldEUUZIYlBIV0RiU0RXS0AoNWlPUCg1aVo2VllGKDVpNTUpT1JGRE9iREdHVUA0OjUxNjMxNDE5OylTRFdLYkxRSVJAKDVpKVNEV0tiV1VEUVZPRFdIR0BHKDZkKDhmU1VSTUhGVyg4Znp6ejF8eHFqZmtscWoxZnJwMXd6KDhmWlpaVVJSVylUWEhVXGJWV1VMUUpAKVVIUFJXSGJER0dVQDQ0NzE3ODE0ODsxNDs6KVVIUFJXSGJLUlZXQDQ0NzE3ODE0ODsxNDs6KVVIUFJXSGJTUlVXQDU2NTgpVUhUWEhWV2JQSFdLUkdASkhXKVZGVUxTV2JRRFBIQCg1aSlWSFVZSFViUURQSEB6enoxfHhxamZrbHFqMWZycDF3eilWSFVZSFViU1JVV0A7MylWSFVZSFViU1JVV2JWSEZYVUhAMylWSFVZSFViU1VSV1JGUk9AS1dXUyg1aTQxNClWSFVZSFViVlJJV1pEVUhAUGxmdXJ2cml3MExMVig1aTsxOClYVU9AKDVpKUtXV1NiRlJRUUhGV0xSUUBuaGhzMGRvbHloKUtXV1NiREZGSFNXQHdoe3coNWlrd3BvKDVmZHNzb2xmZHdscnEoNWl7a3dwbyg1ZXtwbyg1ZmRzc29sZmR3bHJxKDVpe3BvKDZldCg2ZzMxPCg1ZmxwZGpoKDVpemhlcyg1Zi0oNWktKDZldCg2ZzMxOylLV1dTYkRGRkhTV2JIUUZSR0xRSkBqfWxzKDVmLmdoaW9kd2goNWYudmdmaylLV1dTYkRGRkhTV2JPRFFKWERKSEB9azBXWig1Zn1rKDZldCg2ZzMxOyg1ZmhxMFhWKDZldCg2ZzMxOSg1ZmhxKDZldCg2ZzMxNylLV1dTYktSVldAenp6MXx4cWpma2xxajFmcnAxd3opS1dXU2JVSElIVUhVQGt3d3N2KDZkKDVpKDVpenp6MWpycmpvaDFmcnAxd3ooNWkpS1dXU2JYVkhVYkRKSFFXQFByfWxvb2QoNWk4MTMuK1pscWdyenYuUVcuOTE0KDZlLlpSWjk3LC5Ec3NvaFpoZU5sdyg1aTg2OjE2OS4rTktXUE8oNWYub2xuaC5KaGZuciwuRmt1cnBoKDVpNzgxMzE1Nzg3MTQzNC5WZGlkdWwoNWk4NjoxNjkpS1dXU2JYU0pVREdIYkxRVkhGWFVIYlVIVFhIVldWQDQ=; SEID_G=2c2d79b1-c5a1-4ec1-9eae-db76c79fd20e; __ltmwga=utmcsr=google|utmcmd=organic; _dc_gtm_UA-35108030-1=1; _ga=GA1.3.297006320.1443947390; _gat_UA-35108030-1=1; TRID_G=5fe5039f-3de6-46eb-8780-100962b7895d; TRID_G=2c294eea-ff30-40b3-8a55-829c9fe7f2fd; yawbewkcehc=0; CSCWORM_UNID=144394740109999; _ga=GA1.4.297006320.1443947390; __asc=68b72e1815031f8a37e7b1f6e00; __auc=68b72e1815031f8a37e7b1f6e00; WMX_Channel=,1,; __sonar=13847973182577720728; sto-id-%3Fv30%3FGroup-buy.yungching.com.tw%3A80=EDABBOKM'}

_hbhousing_header={'Cookie':'ccguid=2013032713430508681bac085829e1; trkID=9f1c2839a7564703abf14290509e9816; ASPSESSIONIDACTRRSQT=IHPMHDNDBGNKIBIEAJMMPJAJ; ccsession=201510041702076601a8c0209cbfd9; __utmt=1; _TUCS=1; _dc_gtm_UA-34980571-19=1; iQuery=2%5E1%5E3%5E%5E%5EP0%5F0%5E%5E%5E0%5F0%5E0%5F0%5E0%5E0%5F0%5E0%5F0%5E0%5E0%5E0%5E0%5E; myHistory=AS11585; __utma=10173420.656931167.1443947463.1443947463.1443947463.1; __utmb=10173420.3.10.1443947463; __utmc=10173420; __utmz=10173420.1443947463.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _TUCI=sessionNumber+1&pageView+3&produckPageView+1&UUproduckPageView+1&produckList+AS11585; _ga=GA1.3.656931167.1443947463'}

_utrust_header={'Cookie':'ASP.NET_SessionId=noga4mnv2onzx4tuun32arw4; VistCaseID=2559f7e4-45a1-428d-96c9-8305586439a9,; sto-id-%3Fv30%3FGroup-www.u-trust.com.tw=DLABBOKM; __utma=61016232.1174778262.1443947555.1443947555.1443947555.1; __utmb=61016232.2.10.1443947555; __utmc=61016232; __utmz=61016232.1443947555.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmt_b=1; ASPSESSIONIDCQBRQCQR=ABAOJPFAHBFLBJNGLIKKEFEJ'}

_sale591_header={'Cookie':'__utmt=1; __utma=82835026.754351571.1443948542.1443948542.1443948542.1; __utmb=82835026.2.10.1443948542; __utmc=82835026; __utmz=82835026.1443948542.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=a3cfd3680e16114a93c1198acf0ca281; ba_cid=a%3A5%3A%7Bs%3A6%3A%22ba_cid%22%3Bs%3A32%3A%220b6f661550f4b84a7c655a2ed4c1671d%22%3Bs%3A7%3A%22page_ex%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22page%22%3Bs%3A47%3A%22http%3A%2F%2Fsale.591.com.tw%2Fsale-detail-2048306.html%22%3Bs%3A7%3A%22time_ex%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22time%22%3Bi%3A1443948569%3B%7D; __asc=28d37cce150320a37a5ffbf4067; __auc=28d37cce150320a37a5ffbf4067; _gat=1; _ga=GA1.3.754351571.1443948542; _gat_testUA=1; urlJumpIp=6; urlJumpIpByTxt=%E6%A1%83%E5%9C%92%E5%B8%82'}

_pacific_header={'Cookie':''}

cookieDict={'sinyi':_sinyi_header,'houseFun':_houseFun_header,'yungching':_yungching_header,'hbhousing':_hbhousing_header,
            'pacific':_pacific_header,'utrust':_utrust_header,'sale591':_sale591_header}
                    
         
def getSampleByCol(df,col,n,proportional=None): 
    catSizeSeries=df.groupby([col]).apply(lambda x:len(x))
    catSizeSeries.sort()
    if proportional==False:
        catCount=len(catSizeSeries)
        catSize=n/catCount
        diff=n%catCount        
        catSizeSeries.iloc[0:]=catSize
        if diff!=0:                 
            for i in range(diff):
                catSizeSeries[i]=catSizeSeries[i]+1
    else: #proportional 
        pSeries=catSizeSeries*1.0/len(df)
        catSizeSeries=pSeries.apply(lambda x: int(round(x*n,0)))
        catSizeSeries.sort()
        diff=n-(catSizeSeries.sum())
        for i in range(abs(diff)):
            if diff>0:
                catSizeSeries[i]= catSizeSeries[i]+1
            elif diff<0:
                catSizeSeries[-(i+1)]= catSizeSeries[-(i+1)]-1
    result=[]
    for cat,catSize in catSizeSeries.iteritems():
        result.append(df.ix[df[col]==cat,:].sample(catSize))                
    return result[0].append(result[1:])
    
    
def devideManage_Cleaning(gData):
    gData['URL']=gData['URL'].str.strip() 
    if gData['website'].unique()[0]=='pacific':   
        gData['URL']=gData['URL'].str.replace('([^\d])(0)','\g<1>o')        
    return gData

import requests
import time
import random
import traceback
def urlValidate(url,website,multithread=False,hid=None,resultList=None):    
    try:
        res=requests.head(url, headers=cookieDict[website])    
    except:
        excType, excValue, excTB=sys.exc_info()
        print '====Waring==== request failed due to {}.Message: {}'.format(excType, excValue)
    time.sleep(random.randint(1,3))
    time.sleep(random.random())
    result = -1
    if website in ['yungching','utrust','pacific']:
        result= 1 if res.status_code==200 and len(res.history)==0 else 0        
    elif website == 'hbhousing':       
        result= 1 if res.status_code==200 and int(res.headers.get('content-length'))>50000 else 0 #actual value is 48423
    elif website == 'sale591':
        result= 1 if res.status_code==200 and res.headers.get('set-cookie')!=None else 0
    elif website =='houseFun':
        result= 1 if res.status_code==200 and res.headers.get('last-modified')!=None else 0
    else: #sinyi
        result= 1 if res.status_code==200 else 0
    
    if multithread:
        resulttuple=(hid,result)
        resultList.append(resulttuple)     
        return
    else:
        return result

