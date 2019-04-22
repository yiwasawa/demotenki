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

import binascii

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

# Blockchain
@route('/blockchain')
def blockchain():
    return template('blockchain')


# Polly
@route('/polly')
def polly():
    return template('polly')

# サンプル原稿取得
@route('/getsamplescript')
def getsamplescript():

    cnxn4 = pyodbc.connect(DB_CONNECT_02)
    cursor4 = cnxn4.cursor()
    sql4 = "SELECT TOP 1 * FROM dbo.TenkiDemo ORDER BY NICHIJI DESC"
    cursor4.execute(sql4)
    row4 = cursor4.fetchone()

    script = "最新の南さいたまの気温は" + str(row4[1]) + "度、湿度は" + str(row4[2]) + "％くらいです。"

    return '[{"type":"message", "text":"text", "script":"' + script + '"}]'

# サンプル原稿取得JSON
@route('/getsamplescriptjson', method='POST')
def getsamplescriptjson():

    cnxn4 = pyodbc.connect(DB_CONNECT_02)
    cursor4 = cnxn4.cursor()
    sql4 = "SELECT TOP 1 * FROM dbo.TenkiDemo ORDER BY NICHIJI DESC"
    cursor4.execute(sql4)
    row4 = cursor4.fetchone()

    script = "最新の南さいたまの気温は" + str(row4[1]) + "度、湿度は" + str(row4[2]) + "％くらいです。"



    body = '{"type":"message", "text":"text"}'
    r = HTTPResponse(status=200, body=body)
    r.set_header("Content-Type", "application/json")
    return r

    return '[{}]'


@route('/postscript', method='POST')
def postscript():

    try:
        body = json.load(request.body)
    except:
        raise ValueError
    
    script = body["script"]
    ssml = body["ssml"]

    if ssml == "true":
        tt = "ssml"
    else:
        tt = "text"

    # 現在時刻の取得
    nowtime = datetime.datetime.now()
    nowtime = nowtime + datetime.timedelta(hours=9)
    nowtime = nowtime.strftime("%Y%m%d%H%M%S")

    session = Session(region_name="ap-northeast-1")
    client = session.client("polly")
    filename = "/home/ec2-user/demotenki/static/polly/" + nowtime + ".mp3"

    response = client.synthesize_speech(Text=script, TextType=tt, OutputFormat="mp3", VoiceId="Takumi")

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

    return '[{"fromaddress":"1TgN4QggTGgyN8hPcda5qQPA5t2kjj9zXpxMhA","toaddress":"1PN6wchQ348Rn8rW5qgbgQZAytZeSuuF8oyT3s","currency":"' + CURRENCY + '", "qty":"10"}]'

# 口座名称取得
@route('/mc_getaccountname', method='POST')
def mc_getaccountname():

    try:
        body = json.load(request.body)
    except:
        raise ValueError
    
    address = body["address"]

    headers = {'apikey':MULTIAPIKEY}
    payload = {'method':'liststreamkeyitems','params':['accountname',address]}
    response_multi1 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)

    # response_multi1はrequestsのオブジェクトで、requests.json()ということ。
    # pythonの辞書型にデコードされる。
    data_multi1 = response_multi1.json()

    print(data_multi1)

    data = data_multi1["result"][0]["data"]

    accountname = binascii.unhexlify(data).decode('utf-8')

    print(accountname)

    return '[{"accountname":"' + accountname + '"}]'





# サンプル原稿取得
@route('/mc_getmultibalances', method='GET')
def getmultibalances():

    # スタブ
    headers = {'apikey':MULTIAPIKEY}

    payload = {'method':'getmultibalances','params':['*','MKICoins']}
    response_multi1 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)

    data_multi1 = response_multi1.json()

    payload = {'method':'liststreamkeyitems','params':['accountname','1PN6wchQ348Rn8rW5qgbgQZAytZeSuuF8oyT3s']}
    response_multi2 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)
    data_multi2 = response_multi2.json()
    data = data_multi2["result"][0]["data"]
    accountname = binascii.unhexlify(data).decode('utf-8')

    accountname_1 = accountname
    address_1 = "1PN6wchQ348Rn8rW5qgbgQZAytZeSuuF8oyT3s"
    qty_1 = data_multi1["result"]["1PN6wchQ348Rn8rW5qgbgQZAytZeSuuF8oyT3s"][0]["qty"]

    # 2件目

    payload = {'method':'liststreamkeyitems','params':['accountname','1TgN4QggTGgyN8hPcda5qQPA5t2kjj9zXpxMhA']}
    response_multi2 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)
    data_multi2 = response_multi2.json()
    data = data_multi2["result"][0]["data"]
    accountname = binascii.unhexlify(data).decode('utf-8')

    accountname_2 = accountname
    address_2 = "1TgN4QggTGgyN8hPcda5qQPA5t2kjj9zXpxMhA"
    qty_2 = data_multi1["result"]["1TgN4QggTGgyN8hPcda5qQPA5t2kjj9zXpxMhA"][0]["qty"]

    # 3件目

    payload = {'method':'liststreamkeyitems','params':['accountname','163bVJBXpwrBZX3qsv8aBf4S2KJHaQiPCj2zAV']}
    response_multi2 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)
    data_multi2 = response_multi2.json()
    data = data_multi2["result"][0]["data"]
    accountname = binascii.unhexlify(data).decode('utf-8')

    accountname_3 = accountname
    address_3 = "163bVJBXpwrBZX3qsv8aBf4S2KJHaQiPCj2zAV"
    qty_3 = data_multi1["result"]["163bVJBXpwrBZX3qsv8aBf4S2KJHaQiPCj2zAV"][0]["qty"]

    print(accountname_1)
    print(address_1)
    print(qty_1)
    print(accountname_2)
    print(address_2)
    print(qty_2)
    print(accountname_3)
    print(address_3)
    print(qty_3)

    returndata = [
        {"accountname":accountname_1, "address":address_1, "qty":qty_1},
        {"accountname":accountname_2, "address":address_2, "qty":qty_2},
        {"accountname":accountname_3, "address":address_3, "qty":qty_3}
    ]

    print(returndata)

    return json.dumps(returndata)

@route('/sc_get')
def sc_get():

    headers = {'apikey':MULTIAPIKEY}
    payload = {'method':'liststreamkeyitems','params':['demo','1904050001',False]}
    response_sc1 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)

    dict_sc1 = response_sc1.json()

    dict_save = {}
    list_saveline = []

    for i, v in enumerate(dict_sc1['result']):
        # 16進数からUTF-8に変換
        str_status = binascii.unhexlify(dict_sc1['result'][i]['data']).decode('utf-8')

        # UNIXタイムスタンプを抽出し、日本時間化＆書式変換
        int_timestamp = int(dict_sc1['result'][i]['blocktime'])
        datetime_timestamp = datetime.datetime.fromtimestamp(int_timestamp)
        datetime_timestamp = datetime_timestamp + datetime.timedelta(hours=9)
        str_timestamp = datetime_timestamp.strftime("%Y/%m/%d %H:%M:%S")

        # 注文番号、タイムスタンプ、ステータスを配列に格納
        list_saveline.append({"ordernumber":"1904050001","timestamp":str_timestamp,"status":str_status})

    # 返却用の辞書型に格納
    dict_save = {"blockchainitems":list_saveline}

    return json.dumps(dict_save, ensure_ascii=False, indent=4)


@route('/sc_listitems')
def sc_listitems():

    headers = {'apikey':MULTIAPIKEY}
    payload = {'method':'liststreamitems','params':['demo',False,999]}
    response_sc1 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)

    dict_sc1 = response_sc1.json()

    dict_save = {}
    list_saveline = []

    for i, v in enumerate(dict_sc1['result']):
        # 注文番号
        str_ordernumber = dict_sc1['result'][i]['key']

        # タイムスタンプ：UNIXタイムスタンプを抽出し、日本時間化＆書式変換
        int_timestamp = int(dict_sc1['result'][i]['blocktime'])
        datetime_timestamp = datetime.datetime.fromtimestamp(int_timestamp)
        datetime_timestamp = datetime_timestamp + datetime.timedelta(hours=9)
        str_timestamp = datetime_timestamp.strftime("%Y/%m/%d %H:%M:%S")

        # ステータス：16進数からUTF-8に変換
        str_status = binascii.unhexlify(dict_sc1['result'][i]['data']).decode('utf-8')

        # 注文番号、タイムスタンプ、ステータスを配列に格納
        list_saveline.append({"ordernumber":str_ordernumber,"timestamp":str_timestamp,"status":str_status})

    # 返却用の辞書型に格納
    dict_save = {"blockchainitems":list_saveline}

    return json.dumps(dict_save, ensure_ascii=False, indent=4)

@route('/sc_listitems_aws')
def sc_listitems_aws():

    headers = {'Authorization':AWS_BASIC_AUTH}
    payload = {'method':'liststreamitems','params':['demo',False,999]}
    response_sc1 = requests.post(AWS_MULTICHAIN_ENDPOINT, data=json.dumps(payload), headers=headers)

    dict_sc1 = response_sc1.json()

    dict_save = {}
    list_saveline = []

    for i, v in enumerate(dict_sc1['result']):
        # 注文番号
        str_ordernumber = dict_sc1['result'][i]['key']

        # タイムスタンプ：UNIXタイムスタンプを抽出し、日本時間化＆書式変換
        int_timestamp = int(dict_sc1['result'][i]['blocktime'])
        datetime_timestamp = datetime.datetime.fromtimestamp(int_timestamp)
        datetime_timestamp = datetime_timestamp + datetime.timedelta(hours=9)
        str_timestamp = datetime_timestamp.strftime("%Y/%m/%d %H:%M:%S")

        # ステータス：16進数からUTF-8に変換
        str_status = binascii.unhexlify(dict_sc1['result'][i]['data']).decode('utf-8')

        # 注文番号、タイムスタンプ、ステータスを配列に格納
        list_saveline.append({"ordernumber":str_ordernumber,"timestamp":str_timestamp,"status":str_status})

    # 返却用の辞書型に格納
    dict_save = {"blockchainitems":list_saveline}

    return json.dumps(dict_save, ensure_ascii=False, indent=4)


@route('/sc_updatestatus', method='POST')
def sc_updatestatus():

    try:
        body = json.load(request.body)
    except:
        raise ValueError
    
    str_stream = "demo"
    str_ordernumber = body["ordernumber"]
    str_status = body["status"]

    headers = {'apikey':MULTIAPIKEY}
    payload = {'method':'publish','params':[str_stream, str_ordernumber, str_status]}
    response_multi1 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)

    data_multi1 = response_multi1.json()

    print(data_multi1)

    # qty = json.dumps(data_multi1["result"][0]["qty"])
    # result = {"qty":qty}
    # return json.dumps(result)
    return data_multi1


# bottleのデモWebサーバー
# run(host='0.0.0.0', port=8080, debug=True, reloader=True)
# run(host='13.113.245.130', port=80, debug=True, reloader=True)
# run(host='0.0.0.0', port=8080, debug=True, reloader=True)