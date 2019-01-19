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

% import datetime

% nowtime = datetime.datetime.now()
% nowtime = nowtime + datetime.timedelta(hours=9)
% nowtime = nowtime.strftime("%H:%M")


% import pyodbc
% cnxn = pyodbc.connect(DB_CONNECT_02)
% cursor = cnxn.cursor()
% sql = "SELECT TOP 6 TIME_FROM, TIME_TO, DESTINATION, NOTE FROM TrainTime WHERE TIME_FROM > '" + nowtime + "' ORDER BY TIME_FROM ASC"
% cursor.execute(sql)

% cnxn2 = pyodbc.connect(DB_CONNECT_02)
% cursor2 = cnxn2.cursor()
% sql2 = "SELECT TOP 1 * FROM dbo.TenkiDemo ORDER BY NICHIJI DESC"
% cursor2.execute(sql2)
% row2 = cursor2.fetchone()

<head>
  <title>通勤時刻表</title>
</head>

<body>

  <div class="siimple-content--small">

    <div class="siimple-h2">通勤時刻表</div>

    <p class="siimple-p"><a href="./" class="siimple-link">表紙</a></p>

    <div class="siimple-h3">{{nowtime}}時点</div>

    <p class="siimple-p"><span class="siimple-tag siimple-tag--teal">（朝）赤羽⇒新橋／（夜）新橋⇒赤羽</span></p>

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