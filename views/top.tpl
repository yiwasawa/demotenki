<!-- Import siimple -->
<!-- <link rel="stylesheet" href="../dist/siimple.css"> -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/siimple@3.0.0/dist/siimple.css">

<!-- Test styles -->
<style>
  body
  {
    margin: 40px;
  }
  .stattable
  {
    max-width: 400px;
  }
</style>

% import sys
% sys.path.append('..')
% from password.password import *

% import pyodbc
% cnxn = pyodbc.connect(DB_CONNECT_02)
% cursor = cnxn.cursor()
% sql = "SELECT TOP 100 * FROM dbo.TenkiDemo ORDER BY NICHIJI DESC"
% cursor.execute(sql)

% cnxn2 = pyodbc.connect(DB_CONNECT_02)
% cursor2 = cnxn2.cursor()
% sql2 = "SELECT TOP 1 * FROM dbo.TenkiDemo ORDER BY NICHIJI DESC"
% cursor2.execute(sql2)
% row2 = cursor2.fetchone()

<head>
  <title>気象台</title>
</head>

<body>

  <div class="siimple-content--small">

    <div class="siimple-h2">気象台</div>

    <p class="siimple-p">ただいまの南さいたまの気温は<b>{{row2[1]}}℃</b>、湿度は<b>{{row2[2]}}％</b>くらいです。</p>
    <p class="siimple-p">{{row2[3]}} {{row2[4]}} {{row2[5]}} {{row2[6]}} {{row2[7]}}</p>    

    <p class="siimple-p"><a href="/stat" class="siimple-link">統計情報</a></p>
    <p class="siimple-p"><a href="/graph2" class="siimple-link">グラフ</a></p>
    <p class="siimple-p"><a href="/graph" class="siimple-link">旧グラフ</a></p>

    <div class="siimple-h3">最新100件</div>

    <p class="siimple-p"><span class="siimple-tag siimple-tag--teal">南さいたま</span></p>

    <div class="siimple-table">
      <div class="siimple-table-header">
        <div class="siimple-table-row">
          <div class="siimple-table-cell">日時</div>
          <div class="siimple-table-cell">温度</div>
          <div class="siimple-table-cell">湿度</div>
        </div>
      </div>
      <div class="siimple-table-body">
        % for row in cursor.fetchall():
        <div class="siimple-table-row">
          <div class="siimple-table-cell">{{row[0]}}</div>
          <div class="siimple-table-cell">{{row[1]}}</div>
          <div class="siimple-table-cell">{{row[2]}}</div>
        </div>
        %end
      </div>
    </div>

    <p class="siimple-p"><span class="siimple-tag siimple-tag--navy">SQL文</span></p>
    <pre class="siimple-pre">SELECT TOP 100 * FROM dbo.TenkiDemo ORDER BY NICHIJI DESC;</pre>

  </div>
</body>