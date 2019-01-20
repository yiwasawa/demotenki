<!-- Import siimple -->
<!-- <link rel="stylesheet" href="../dist/siimple.css"> -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/siimple@3.0.0/dist/siimple.css">

<!-- styles -->
<style>
    body {
        margin: 0px;
    }
</style>

<meta content="width=device-width,initial-scale=1.0" name="viewport">

% import sys
% sys.path.append('..')
% from password.password import *

% from boto3 import Session
% from botocore.exceptions import BotoCoreError, ClientError
% from contextlib import closing
% import os
% import subprocess

% import pyodbc
% cnxn4 = pyodbc.connect(DB_CONNECT_02)
% cursor4 = cnxn4.cursor()
% sql4 = "SELECT TOP 1 * FROM dbo.TenkiDemo ORDER BY NICHIJI DESC"
% cursor4.execute(sql4)
% row4 = cursor4.fetchone()


% import datetime
% nowtime = datetime.datetime.now()
% nowtime = nowtime + datetime.timedelta(hours=9)
% nowtime = nowtime.strftime("%Y%m%d%H%M%S")

% speech = "お疲れさまです。生麦生米生卵、隣の客はよく柿食う客だ。今のさいたまの気温は" + str(row4[1]) + "度、湿度は" + str(row4[2]) + "％くらいです。"

% session = Session(region_name="ap-northeast-1")
% polly = session.client("polly")
% filename = "/home/ec2-user/demotenki/static/polly/" + nowtime + ".mp3"

% response = polly.synthesize_speech(Text=speech, OutputFormat="mp3", VoiceId="Mizuki")
% if "AudioStream" in response:
%     with closing(response["AudioStream"]) as stream:
%         output = filename
%         with open(output, "wb") as file:
%             file.write(stream.read())

% filepath = "http://13.113.245.130/file/polly/" + nowtime + ".mp3"

<head>
  <title>話す気象台</title>
</head>

<body>

  <div class="siimple-content--small">

    <div class="siimple-h2">話す気象台</div>



    <audio controls>
        <source src="{{filepath}}" type="audio/mp3">
    </audio>


  </div>
</body>