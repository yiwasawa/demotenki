import requests
import time
import json
import datetime
import pyodbc
from password.password import *

# Dark Sky APIからのデータ取得
response_ds1 = requests.get(DS1_URL)
response_ds2 = requests.get(DS2_URL)
response_ds3 = requests.get(DS3_URL)
response_ds4 = requests.get(DS4_URL)

# darkskyから取得したデータを格納
data_ds1= response_ds1.json()
data_ds2= response_ds2.json()
data_ds3= response_ds3.json()
data_ds4= response_ds4.json()

# クリア
cnxn = pyodbc.connect(DB_CONNECT_02)
cursor = cnxn.cursor()
sql = "DELETE FROM dbo.TenkiHour"
cursor.execute(sql)
cnxn.commit()

# 1回目----------------------------------------
i_area = DS1_AREA
i_latitude = json.dumps(data_ds1["latitude"])
i_longitude = json.dumps(data_ds1["longitude"])

for i in range(49):

    i_time = int(json.dumps(data_ds1["hourly"]["data"][i]["time"]))
    i_time = datetime.datetime.fromtimestamp(i_time)
    i_time = i_time + datetime.timedelta(hours=9)
    i_time = str(i_time)

    i_icon = json.dumps(data_ds1["hourly"]["data"][i]["icon"])
    i_icon = i_icon.strip('"')    

#    now = int(json.dumps(data_ds1["hourly"]["data"][i]["time"]))
#    now = datetime.datetime.fromtimestamp(now)
#    now = "{0:%m/%d(%a)%H:%M}".format(now)
#    print (now)

    i_precipIntensity = json.dumps(data_ds1["hourly"]["data"][i]["precipIntensity"])
    i_precipProbability = json.dumps(data_ds1["hourly"]["data"][i]["precipProbability"])
    i_temperature = json.dumps(data_ds1["hourly"]["data"][i]["temperature"])
    i_humidity = json.dumps(data_ds1["hourly"]["data"][i]["humidity"])
    i_pressure = json.dumps(data_ds1["hourly"]["data"][i]["pressure"])
    i_windSpeed = json.dumps(data_ds1["hourly"]["data"][i]["windSpeed"])
    i_windGust = json.dumps(data_ds1["hourly"]["data"][i]["windGust"])
    i_windBearing = json.dumps(data_ds1["hourly"]["data"][i]["windBearing"])
    i_cloudCover = json.dumps(data_ds1["hourly"]["data"][i]["cloudCover"])
    i_uvIndex = json.dumps(data_ds1["hourly"]["data"][i]["uvIndex"])

    # Azure DBへのINSERT
    cnxn = pyodbc.connect(DB_CONNECT_02)
    cursor = cnxn.cursor()
    sql = "INSERT INTO dbo.TenkiHour (area, latitude, longitude, time, icon, precipIntensity, precipProbability, temperature, humidity, pressure, windSpeed, windGust, windBearing, cloudCover, uvIndex) VALUES ('" + i_area + "','" + i_latitude + "','" + i_longitude + "','" + i_time + "','" + i_icon + "','" + i_precipIntensity + "','" + i_precipProbability + "','" + i_temperature + "','" + i_humidity + "','" + i_pressure + "','" + i_windSpeed + "','" + i_windGust + "','" + i_windBearing + "','" + i_cloudCover + "','" + i_uvIndex + "')"
    cursor.execute(sql)
    cnxn.commit()

# 2回目----------------------------------------
i_area = DS2_AREA
i_latitude = json.dumps(data_ds2["latitude"])
i_longitude = json.dumps(data_ds2["longitude"])

for i in range(49):

    i_time = int(json.dumps(data_ds2["hourly"]["data"][i]["time"]))
    i_time = datetime.datetime.fromtimestamp(i_time)
    i_time = i_time + datetime.timedelta(hours=9)
    i_time = str(i_time)

    i_icon = json.dumps(data_ds2["hourly"]["data"][i]["icon"])
    i_icon = i_icon.strip('"')    

    i_precipIntensity = json.dumps(data_ds2["hourly"]["data"][i]["precipIntensity"])
    i_precipProbability = json.dumps(data_ds2["hourly"]["data"][i]["precipProbability"])
    i_temperature = json.dumps(data_ds2["hourly"]["data"][i]["temperature"])
    i_humidity = json.dumps(data_ds2["hourly"]["data"][i]["humidity"])
    i_pressure = json.dumps(data_ds2["hourly"]["data"][i]["pressure"])
    i_windSpeed = json.dumps(data_ds2["hourly"]["data"][i]["windSpeed"])
    i_windGust = json.dumps(data_ds2["hourly"]["data"][i]["windGust"])
    i_windBearing = json.dumps(data_ds2["hourly"]["data"][i]["windBearing"])
    i_cloudCover = json.dumps(data_ds2["hourly"]["data"][i]["cloudCover"])
    i_uvIndex = json.dumps(data_ds2["hourly"]["data"][i]["uvIndex"])

    # Azure DBへのINSERT
    cnxn = pyodbc.connect(DB_CONNECT_02)
    cursor = cnxn.cursor()
    sql = "INSERT INTO dbo.TenkiHour (area, latitude, longitude, time, icon, precipIntensity, precipProbability, temperature, humidity, pressure, windSpeed, windGust, windBearing, cloudCover, uvIndex) VALUES ('" + i_area + "','" + i_latitude + "','" + i_longitude + "','" + i_time + "','" + i_icon + "','" + i_precipIntensity + "','" + i_precipProbability + "','" + i_temperature + "','" + i_humidity + "','" + i_pressure + "','" + i_windSpeed + "','" + i_windGust + "','" + i_windBearing + "','" + i_cloudCover + "','" + i_uvIndex + "')"
    cursor.execute(sql)
    cnxn.commit()

# 3回目----------------------------------------
i_area = DS3_AREA
i_latitude = json.dumps(data_ds3["latitude"])
i_longitude = json.dumps(data_ds3["longitude"])

for i in range(49):

    i_time = int(json.dumps(data_ds3["hourly"]["data"][i]["time"]))
    i_time = datetime.datetime.fromtimestamp(i_time)
    i_time = i_time + datetime.timedelta(hours=9)
    i_time = str(i_time)

    i_icon = json.dumps(data_ds3["hourly"]["data"][i]["icon"])
    i_icon = i_icon.strip('"')    

    i_precipIntensity = json.dumps(data_ds3["hourly"]["data"][i]["precipIntensity"])
    i_precipProbability = json.dumps(data_ds3["hourly"]["data"][i]["precipProbability"])
    i_temperature = json.dumps(data_ds3["hourly"]["data"][i]["temperature"])
    i_humidity = json.dumps(data_ds3["hourly"]["data"][i]["humidity"])
    i_pressure = json.dumps(data_ds3["hourly"]["data"][i]["pressure"])
    i_windSpeed = json.dumps(data_ds3["hourly"]["data"][i]["windSpeed"])
    i_windGust = json.dumps(data_ds3["hourly"]["data"][i]["windGust"])
    i_windBearing = json.dumps(data_ds3["hourly"]["data"][i]["windBearing"])
    i_cloudCover = json.dumps(data_ds3["hourly"]["data"][i]["cloudCover"])
    i_uvIndex = json.dumps(data_ds3["hourly"]["data"][i]["uvIndex"])

    # Azure DBへのINSERT
    cnxn = pyodbc.connect(DB_CONNECT_02)
    cursor = cnxn.cursor()
    sql = "INSERT INTO dbo.TenkiHour (area, latitude, longitude, time, icon, precipIntensity, precipProbability, temperature, humidity, pressure, windSpeed, windGust, windBearing, cloudCover, uvIndex) VALUES ('" + i_area + "','" + i_latitude + "','" + i_longitude + "','" + i_time + "','" + i_icon + "','" + i_precipIntensity + "','" + i_precipProbability + "','" + i_temperature + "','" + i_humidity + "','" + i_pressure + "','" + i_windSpeed + "','" + i_windGust + "','" + i_windBearing + "','" + i_cloudCover + "','" + i_uvIndex + "')"
    cursor.execute(sql)
    cnxn.commit()

# 4回目----------------------------------------
i_area = DS4_AREA
i_latitude = json.dumps(data_ds4["latitude"])
i_longitude = json.dumps(data_ds4["longitude"])

for i in range(49):

    i_time = int(json.dumps(data_ds4["hourly"]["data"][i]["time"]))
    i_time = datetime.datetime.fromtimestamp(i_time)
    i_time = i_time + datetime.timedelta(hours=9)
    i_time = str(i_time)

    i_icon = json.dumps(data_ds4["hourly"]["data"][i]["icon"])
    i_icon = i_icon.strip('"')    

    i_precipIntensity = json.dumps(data_ds4["hourly"]["data"][i]["precipIntensity"])
    i_precipProbability = json.dumps(data_ds4["hourly"]["data"][i]["precipProbability"])
    i_temperature = json.dumps(data_ds4["hourly"]["data"][i]["temperature"])
    i_humidity = json.dumps(data_ds4["hourly"]["data"][i]["humidity"])
    i_pressure = json.dumps(data_ds4["hourly"]["data"][i]["pressure"])
    i_windSpeed = json.dumps(data_ds4["hourly"]["data"][i]["windSpeed"])
    i_windGust = json.dumps(data_ds4["hourly"]["data"][i]["windGust"])
    i_windBearing = json.dumps(data_ds4["hourly"]["data"][i]["windBearing"])
    i_cloudCover = json.dumps(data_ds4["hourly"]["data"][i]["cloudCover"])
    i_uvIndex = json.dumps(data_ds4["hourly"]["data"][i]["uvIndex"])

    # Azure DBへのINSERT
    cnxn = pyodbc.connect(DB_CONNECT_02)
    cursor = cnxn.cursor()
    sql = "INSERT INTO dbo.TenkiHour (area, latitude, longitude, time, icon, precipIntensity, precipProbability, temperature, humidity, pressure, windSpeed, windGust, windBearing, cloudCover, uvIndex) VALUES ('" + i_area + "','" + i_latitude + "','" + i_longitude + "','" + i_time + "','" + i_icon + "','" + i_precipIntensity + "','" + i_precipProbability + "','" + i_temperature + "','" + i_humidity + "','" + i_pressure + "','" + i_windSpeed + "','" + i_windGust + "','" + i_windBearing + "','" + i_cloudCover + "','" + i_uvIndex + "')"
    cursor.execute(sql)
    cnxn.commit()

