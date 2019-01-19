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
    
% speech = "ただいまの南さいたまの気温は" + str(row4[1]) + "℃、湿度は" + str(row4[2]) + "％くらいです。"

% session = Session(region_name="ap-northeast-1")
% polly = session.client("polly")

%    try:
%        response = polly.synthesize_speech(Text=speech, OutputFormat="mp3", VoiceId="Mizuki")
%    except (BotoCoreError, ClientError) as error:
%        print(error)
%        sys.exit(-1)
%    if "AudioStream" in response:
%        with closing(response["AudioStream"]) as stream:
%            output = "/var/www/html/speech3.mp3"
%            try:
%                with open(output, "wb") as file:
%                    file.write(stream.read())
%            except IOError as error:
%                print(error)
%                sys.exit(-1)
%            print("synthesize_speech OK ->>" + output)
%    else:
%        print("Could not stream audio")
%        sys.exit(-1)


<head>
  <title>通勤時刻表</title>
</head>

<body>

  <div class="siimple-content--small">

    <div class="siimple-h2">通勤時刻表</div>

    <p class="siimple-p"><a href="./" class="siimple-link">表紙</a></p>

    <div class="siimple-h3">{{nowtime}}時点</div>

    <p class="siimple-p"><span class="siimple-tag siimple-tag--teal">（朝）赤羽⇒新橋／（夜）新橋⇒赤羽</span></p>

    <audio controls>
        <source src="http://13.113.245.130/speech3.mp3" type="audio/mp3">
    </audio>


  </div>
</body>