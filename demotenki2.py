import os
import sys

sys.path.append('/home/ec2-user/.pyenv/versions/3.6.2/lib/python3.6/site-packages')
sys.path.append('/home/ec2-user/.pyenv/versions/3.6.2/lib/python3.6/lib-dynload')
sys.path.append('/home/ec2-user/.pyenv/versions/3.6.2/lib/python3.6')
sys.path.append('/home/ec2-user/demotenki')
sys.path.append('/home/ec2-user')

from bottle import *
import pyodbc
from password.password import *

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing

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

# Polly
@route('/demopolly')
def demopolly():
    return template('demopolly')


# run(host='0.0.0.0', port=8080, debug=True, reloader=True)
# run(host='13.113.245.130', port=80, debug=True, reloader=True)

run(host='0.0.0.0', port=8080, debug=True, reloader=True)