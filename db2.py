import requests
from bs4 import BeautifulSoup
import json
import time
from pymysql import *

def mes():
    url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0'  #请求地址
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36 SLBrowser/6.0.1.6181'}#创建头部信息
    resp =  requests.get(url,headers = headers)  #发送网络请求
    content=resp.content.decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    listA = soup.find_all(name='script',attrs={"id":"getAreaStat"})
    account =str(listA)
    mes = account.replace('[<script id="getAreaStat">try { window.getAreaStat = ', '')
    mes=mes.replace('}catch(e){}</script>]','')
    #mes=account[52:-21]
    messages_json = json.loads(mes)
    print(messages_json)
    times=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(times)
    provinceList=[]
    cityList=[]
    lenth=total()
    con=len(messages_json)+lenth#算出数据库已有的条数+今天省份的条数，才是城市的开始id
    for item in messages_json:
        lenth+=1
        provinceName=item['provinceName']
        confirmedCount=item['confirmedCount']
        suspectedCount=item['suspectedCount']
        curedCount=item['curedCount']
        deadCount=item['deadCount']
        cities=item['cities']
        provinceList.append((lenth,times,provinceName,None,confirmedCount,suspectedCount,curedCount,deadCount))
        for i in cities:
            con+=1
            provinceName = item['provinceName']
            cityName=i['cityName']
            confirmedCount = i['confirmedCount']
            suspectedCount = item['suspectedCount']
            curedCount = i['curedCount']
            deadCount = i['deadCount']
            cityList.append((con,times,provinceName,cityName,confirmedCount,suspectedCount,curedCount,deadCount))
    insert(provinceList,cityList)

def insert(provinceList, cityList):
    provinceTuple=tuple(provinceList)
    cityTuple=tuple(cityList)
    cursor = db.cursor()
    sql = "insert into info_new values (%s,%s,%s,%s,%s,%s,%s,%s) "
    try:
        cursor.executemany(sql,provinceTuple)
        print("插入成功")
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    try:
        cursor.executemany(sql,cityTuple)
        print("插入成功")
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    cursor.close()
def total():
    sql= "select * from info_new"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        lenth = len(results)
        db.commit()
        return lenth
    except:
        print('执行失败，进入回调1')
        db.rollback()

# 连接数据库的方法
def connectDB():
    try:
        db = connect(host='localhost', port=3306, user='root', password='whyjlbcdy2001', db='virus',charset='utf8')
        print("数据库连接成功")
        return db
    except Exception as e:
        print(e)
    return NULL
if __name__ == '__main__':
    db=connectDB()
    mes()
