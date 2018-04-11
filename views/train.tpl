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

% import pyodbc
% cnxn = pyodbc.connect(DB_CONNECT_02)
% cursor = cnxn.cursor()
% sql = "SELECT TOP 5 TIME_FROM, TIME_TO, DESTINATION, NOTE FROM TrainTime"
% cursor.execute(sql)

% cnxn2 = pyodbc.connect(DB_CONNECT_02)
% cursor2 = cnxn2.cursor()
% sql2 = "SELECT TOP 1 * FROM dbo.TenkiDemo ORDER BY NICHIJI DESC"
% cursor2.execute(sql2)
% row2 = cursor2.fetchone()

% tenki = row2[8]
% tenki = tenki[1:3]

% tenkilist = {
% "01": "晴れ",
% "02": "晴れ",
% "03": "くもり",
% "04": "くもり",
% "09": "雨",
% "10": "雨",
% "13": "雪",
% "50": "もや"
% }

% tenkiicon = {
% "clear-day": "icons8-sun-24.png",
% "clear-night": "icons8-moon-and-stars-24.png",
% "partly-cloudy-day": "icons8-partly-cloudy-day-24.png",
% "partly-cloudy-night": "icons8-night-24.png",
% "wind": "icons8-windsock-24.png",
% "cloudy": "icons8-cloudy-24.png",
% "rain": "icons8-rainy-weather-24.png",
% "50": "mark_tenki_kumori.png"
% }

% tenkitext = tenkilist.get(tenki,"不明")
% tenkiimg = tenkiicon.get(tenki,"icons8-barometer-50.png")

<head>
  <title>気象台</title>
</head>

<body>

  <div class="siimple-content--small">

    <div class="siimple-h2">通勤時刻表</div>

    <p class="siimple-p"><a href="./" class="siimple-link">表紙</a></p>

    % nowtime = datetime.now().strftime("%H:%M")
    <div class="siimple-h3">{{nowtime}}</div>

    <div class="siimple-h3">新橋⇒赤羽</div>

    <div class="siimple-table">
      <div class="siimple-table-header">
        <div class="siimple-table-row">
          <div class="siimple-table-cell">発時刻</div>
          <div class="siimple-table-cell">着時刻</div>
          <div class="siimple-table-cell">行先</div>
          <div class="siimple-table-cell">備考</div>
        </div>
      </div>
      <div class="siimple-table-body">
        % for row in cursor.fetchall():
        <div class="siimple-table-row">
          % row[0] = row[0][0:5]
          <div class="siimple-table-cell">{{row[0]}}</div>
          % row[1] = row[1][0:5]
          <div class="siimple-table-cell">{{row[1]}}</div>
          <div class="siimple-table-cell">{{row[2]}}</div>
          <div class="siimple-table-cell">{{row[3]}}</div>
        </div>
        %end
      </div>
    </div>


  </div>
</body>