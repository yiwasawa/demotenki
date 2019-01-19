from bottle import *
import pyodbc
from password.password import *

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess

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

@get('/demopolly')
def demopolly():
    demopolly = ''

    cnxn4 = pyodbc.connect(DB_CONNECT_02)
    cursor4 = cnxn4.cursor()
    sql4 = "SELECT TOP 1 * FROM dbo.TenkiDemo ORDER BY NICHIJI DESC"
    cursor4.execute(sql4)
    row4 = cursor4.fetchone()
    
    speech = "ただいまの南さいたまの気温は" + str(row4[1]) + "℃、湿度は" + str(row4[2]) + "％くらいです。"

    session = Session(region_name="ap-northeast-1")
    polly = session.client("polly")

    try:
        response = polly.synthesize_speech(Text=speech, OutputFormat="mp3", VoiceId="Mizuki")
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)
    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output = "/var/www/html/speech.mp3"
            try:
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
            print("synthesize_speech OK ->>" + output)
    else:
        print("Could not stream audio")
        sys.exit(-1)




run(host='0.0.0.0', port=8080, debug=True, reloader=True)
