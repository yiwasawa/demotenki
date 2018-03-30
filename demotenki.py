import lnetatmo
import requests
import time
import json
import datetime
import pyodbc
from password.password import *

# Netatmoの認証情報
authorization = lnetatmo.ClientAuth(
    clientId = NETA_ID,
    clientSecret = NETA_PW,
    username = STD_EMAIL,
    password = STD_PW,
    scope = ""
    )

# Netatmoからのデータ取得
devList = lnetatmo.WeatherStationData(authorization)
outdoors_temp = devList.lastData()['Outdoor']['Temperature']
outdoors_humi = devList.lastData()['Outdoor']['Humidity']

#HANAのタイムスタンプへの変換
posttime = time.time()
print(posttime)
posttime = posttime * 1000
print(posttime)
posttime = posttime + 32400000
print(posttime)
posttime = str(posttime)
print(posttime)
posttime = posttime[0:13]
print(posttime)
posttime = '/Date(' + posttime + ")/"
print(posttime)

#MSSQLのタイムスタンプへの変換
posttime_mssql = datetime.datetime.now()
print(posttime_mssql)
posttime_mssql = posttime_mssql + datetime.timedelta(hours=9)
print(posttime_mssql)
posttime_mssql = str(posttime_mssql)
print(posttime_mssql)
posttime_mssql = posttime_mssql[0:19]
print(posttime_mssql)

outdoors_temp = str(outdoors_temp)
outdoors_humi = str(outdoors_humi)

# Open Weather Mapからのデータ取得
# 東京
response_owm1 = requests.get(TOKYO_WEATHER_URL)
# 埼玉
response_owm2 = requests.get(SAITAMA_WEATHER_URL)
# 札幌
response_owm3 = requests.get(SAPPORO_WEATHER_URL)

# Open Weather Mapから取得したデータを格納
data_owm1= response_owm1.json()
data_owm2= response_owm2.json()
data_owm3= response_owm3.json()

# print(data_owm1)
print ("東京の気温は" + json.dumps(data_owm1["main"]["temp"]) + "℃くらいです。")
print (data_owm1["weather"][0]["icon"])
tokyo_temp = json.dumps(data_owm1["main"]["temp"])
tokyo_humi = json.dumps(data_owm1["main"]["humidity"])
tokyo_tenki = json.dumps(data_owm1["weather"][0]["icon"])

# print(data_owm2)
print ("さいたまの気温は" + json.dumps(data_owm2["main"]["temp"]) + "℃くらいです。")
print (data_owm2["weather"][0]["icon"])
saitama_temp = json.dumps(data_owm2["main"]["temp"])
saitama_humi = json.dumps(data_owm2["main"]["humidity"])
saitama_tenki = json.dumps(data_owm2["weather"][0]["icon"])

# print(data_owm3)
print ("札幌の気温は" + json.dumps(data_owm3["main"]["temp"]) + "℃くらいです。")
print (data_owm3["weather"][0]["icon"])
sapporo_temp = json.dumps(data_owm3["main"]["temp"])
sapporo_humi = json.dumps(data_owm3["main"]["humidity"])
sapporo_tenki = json.dumps(data_owm3["weather"][0]["icon"])

# 個人 Azure DBへのINSERT
cnxn = pyodbc.connect(DB_CONNECT_02)
cursor = cnxn.cursor()
sql = "INSERT INTO dbo.Tenki (TIMESTAMP, TEMP, HUMI) VALUES ('" + posttime_mssql + "','" + outdoors_temp + "','" + outdoors_humi + "')"
cursor.execute(sql)
cnxn.commit()

# Azure DBへのINSERT
cnxn = pyodbc.connect(DB_CONNECT_02)
cursor = cnxn.cursor()
sql = "INSERT INTO dbo.TenkiDemo (NICHIJI, TEMP1, HUMI1, TEMP2, HUMI2, TEMP3, HUMI3, TENKI2, TENKI3) VALUES ('" + posttime_mssql + "','" + outdoors_temp + "','" + outdoors_humi + "','" + tokyo_temp + "','" + tokyo_humi + "','" + sapporo_temp + "','" + sapporo_humi + "','" + tokyo_tenki + "','" + sapporo_tenki + "')"
cursor.execute(sql)
cnxn.commit()
