import os
import sys

sys.path.append('/home/ec2-user/.pyenv/versions/3.6.2/lib/python3.6/site-packages')

from bottle import *


import pyodbc
from password.password import *

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing

import subprocess
import json
import datetime
import requests

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    

# 表紙
@route('/')
@route('/top')
def top():
    return template('top')

# 旧グラフ
@route('/graph')
def graph():
    return template('graph')

# グラフ
@route('/graph2')
def graph2():
    return template('graph2')

# 統計情報
@route('/stat')
def stat():
    return template('stat')

# 予報
@route('/forecast')
def forecast():
    return template('forecast')

# 電車
@route('/train')
def forecast():
    return template('train')

# モバイル
@route('/mobile')
def mobile():
    return template('mobile')

# RSS
@route('/rss2')
def rss2():
    return template('rss2')

# static
@route('/file/<filename:path>')
def static(filename):
    return static_file(filename, root="/home/ec2-user/demotenki/static")

@get('/data')
def data():
    data = ''

    # SQLを発行してデータを取得
    cnxn2 = pyodbc.connect(DB_CONNECT_02)
    cursor2 = cnxn2.cursor()
    sql2 = "SELECT * from dbo.Tenki ORDER BY TIMESTAMP"
    cursor2.execute(sql2)

    # 取得したデータを出力データとして整形
    for row in cursor2.fetchall():
        data += '["{0}",{1}],'.format(row[0], row[1])
    data = data[:-1]

    # データ返却
    return '[[{}]]'.format(data)

@get('/data2')
def data2():
    data2 = ''

    # SQLを発行してデータを取得
    cnxn3 = pyodbc.connect(DB_CONNECT_02)
    cursor3 = cnxn3.cursor()
    sql3 = "SELECT * from dbo.TenkiDemo WHERE NICHIJI > '2018-03-01 12:00:00' ORDER BY NICHIJI DESC"
    cursor3.execute(sql3)

    # 取得したデータを出力データとして整形
    for row in cursor3.fetchall():
        data2 += '["{0}",{1}],'.format(row[0], row[1])
    data2 = data2[:-1]

    # データ返却
    return '[{}]'.format(data2)

@get('/tokyodata')
def tokyodata():
    tokyodata = ''

    # SQLを発行してデータを取得
    cnxn3 = pyodbc.connect(DB_CONNECT_02)
    cursor3 = cnxn3.cursor()
    sql3 = "SELECT * from dbo.TenkiDemo WHERE NICHIJI > '2018-03-01 12:00:00' ORDER BY NICHIJI DESC"

    cursor3.execute(sql3)


    # 取得したデータを出力データとして整形
    for row in cursor3.fetchall():
        tokyodata += '["{0}",{1}],'.format(row[0], row[3])
    tokyodata = tokyodata[:-1]

    # データ返却
    return '[{}]'.format(tokyodata)

@get('/saitamadata')
def saitamadata():
    saitamadata = ''

    # SQLを発行してデータを取得
    cnxn3 = pyodbc.connect(DB_CONNECT_02)
    cursor3 = cnxn3.cursor()
    sql3 = "SELECT * from dbo.TenkiDemo WHERE NICHIJI > '2018-03-01 12:00:00' ORDER BY NICHIJI DESC"
    cursor3.execute(sql3)


    # 取得したデータを出力データとして整形
    for row in cursor3.fetchall():
        saitamadata += '["{0}",{1}],'.format(row[0], row[5])
    saitamadata = saitamadata[:-1]

    # データ返却
    return '[{}]'.format(saitamadata)

# Polly
@route('/demopolly')
def demopolly():
    return template('demopolly')


# Form
@route('/demoform')
def demoform():
    return template('demoform')

# サンプル原稿取得
@route('/getsamplescript')
def getsamplescript():

    cnxn4 = pyodbc.connect(DB_CONNECT_02)
    cursor4 = cnxn4.cursor()
    sql4 = "SELECT TOP 1 * FROM dbo.TenkiDemo ORDER BY NICHIJI DESC"
    cursor4.execute(sql4)
    row4 = cursor4.fetchone()

    script = "最新の南さいたまの気温は" + str(row4[1]) + "度、湿度は" + str(row4[2]) + "％くらいです。"

    return '[{"script":"' + script + '"}]'

@route('/postscript', method='POST')
def postscript():

    try:
        body = json.load(request.body)
    except:
        raise ValueError
    
    script = body["script"]

    # 現在時刻の取得
    nowtime = datetime.datetime.now()
    nowtime = nowtime + datetime.timedelta(hours=9)
    nowtime = nowtime.strftime("%Y%m%d%H%M%S")

    session = Session(region_name="ap-northeast-1")
    polly = session.client("polly")
    filename = "/home/ec2-user/demotenki/static/polly/" + nowtime + ".mp3"

    response = polly.synthesize_speech(Text=script, OutputFormat="mp3", VoiceId="Mizuki")
    if "AudioStream" in response:
      with closing(response["AudioStream"]) as stream:
        output = filename
        with open(output, "wb") as file:
          file.write(stream.read())

    filepath = "http://13.113.245.130/file/polly/" + nowtime + ".mp3"

    result = {"filepath":filepath, "script":script, "time":nowtime}

    # JSONにエンコードして返す。
    # return json.dumps(body)
    return json.dumps(result)


@route('/demoform', method='POST')
def search():

    # フォームの入力値を受け取る感じ。
    testname = request.forms.testname
    testitem = request.forms.testitem

    # JSON的なのを返す。
    testdata = [
        {"id":"1", "testname":"testname1", "testitem":"testitem1"},
        {"id":"2", "testname":"testname2", "testitem":"testitem2"},
        {"id":"3", "testname":"testname3", "testitem":"testitem3"}
    ]

    return json.dumps(testdata)



@route('/mc_getaddressbalances', method='POST')
def mc_getaddressbalances():

    try:
        body = json.load(request.body)
    except:
        raise ValueError
    
    address = body["address"]

    headers = {'apikey':MULTIAPIKEY}
    payload = {'method':'getaddressbalances','params':[address]}
    response_multi1 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)

    data_multi1 = response_multi1.json()

    qty = json.dumps(data_multi1["result"][0]["qty"])

    result = {"qty":qty}
    return json.dumps(result)

@route('/mc_sendassetfrom', method='POST')
def mc_sendassetfrom():

    try:
        body = json.load(request.body)
    except:
        raise ValueError
    
    fromaddress = body["fromaddress"]
    toaddress = body["toaddress"]
    currency = body["currency"]
    qty = body["qty"]

    headers = {'apikey':MULTIAPIKEY}
    payload = {'method':'sendassetfrom','params':[fromaddress, toaddress, currency, int(qty)]}
    response_multi1 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)

    data_multi1 = response_multi1.json()

    print(data_multi1)

    # qty = json.dumps(data_multi1["result"][0]["qty"])
    # result = {"qty":qty}
    # return json.dumps(result)
    return data_multi1

# サンプル原稿取得
@route('/mc_sendassetfrom', method='GET')
def getsamplescript():

    currency = CURRENCY

    return '[{"fromaddress":"1TgN4QggTGgyN8hPcda5qQPA5t2kjj9zXpxMhA","toaddress":"1PN6wchQ348Rn8rW5qgbgQZAytZeSuuF8oyT3s","currency":currency, "qty":"10"}]'

# run(host='0.0.0.0', port=8080, debug=True, reloader=True)
# run(host='13.113.245.130', port=80, debug=True, reloader=True)
# run(host='0.0.0.0', port=8080, debug=True, reloader=True)