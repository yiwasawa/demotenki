<!-- Import siimple -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/siimple@3.0.0/dist/siimple.css">

<!-- styles -->
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
% sql = "SELECT CONVERT(VARCHAR, NICHIJI, 111) AS DATE, MAX(TEMP1) AS MAX , MIN(TEMP1) AS MIN FROM TenkiDemo GROUP BY CONVERT(VARCHAR, NICHIJI, 111) ORDER BY DATE DESC;"
% cursor.execute(sql)

% cnxn2 = pyodbc.connect(DB_CONNECT_02)
% cursor2 = cnxn2.cursor()
% sql2 = "SELECT CONVERT(VARCHAR(7), NICHIJI, 111) AS DATE, MAX(TEMP1) AS MAX , MIN(TEMP1) AS MIN FROM TenkiDemo GROUP BY CONVERT(VARCHAR(7), NICHIJI, 111) ORDER BY DATE DESC;"
% cursor2.execute(sql2)

% cnxn3 = pyodbc.connect(DB_CONNECT_02)
% cursor3 = cnxn3.cursor()
% sql3 = "SELECT TOP 10 CONVERT(VARCHAR, NICHIJI, 111) AS DATE, MAX(TEMP1) AS MAX FROM TenkiDemo GROUP BY CONVERT(VARCHAR, NICHIJI, 111) ORDER BY MAX DESC;"
% cursor3.execute(sql3)

<head>
  <title>気象台 > 統計情報</title>
</head>

<body>

  <div class="siimple-content--small">

    <div class="siimple-h2">気象台</div>

    <p class="siimple-p"><a href="./" class="siimple-link">表紙</a></p>

    <div class="siimple-h3">統計情報</div>

    <p class="siimple-p"><span class="siimple-tag siimple-tag--teal">南さいたま</span></p>


    <div class="siimple-table">
      <div class="siimple-table-header">
        <div class="siimple-table-row">
          <div class="siimple-table-cell">日付</div>
          <div class="siimple-table-cell">最高気温</div>
          <div class="siimple-table-cell">最低気温</div>
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

    <pre class="siimple-pre">SELECT CONVERT(VARCHAR, NICHIJI, 111) AS DATE, MAX(TEMP1) AS MAX , MIN(TEMP1) AS MIN FROM TenkiDemo GROUP BY CONVERT(VARCHAR, NICHIJI, 111) ORDER BY DATE DESC;</pre>

    <div class="siimple-table">
      <div class="siimple-table-header">
        <div class="siimple-table-row">
          <div class="siimple-table-cell">年月</div>
          <div class="siimple-table-cell">最高気温</div>
          <div class="siimple-table-cell">最低気温</div>
        </div>
      </div>
      <div class="siimple-table-body">
        % for row in cursor2.fetchall():
        <div class="siimple-table-row">
          <div class="siimple-table-cell">{{row[0]}}</div>
          <div class="siimple-table-cell">{{row[1]}}</div>
          <div class="siimple-table-cell">{{row[2]}}</div>
        </div>
        %end
      </div>
    </div>

    <p class="siimple-p"><span class="siimple-tag siimple-tag--navy">SQL文</span></p>

    <pre class="siimple-pre">SELECT CONVERT(VARCHAR(7), NICHIJI, 111) AS DATE, MAX(TEMP1) AS MAX , MIN(TEMP1) AS MIN FROM TenkiDemo GROUP BY CONVERT(VARCHAR(7), NICHIJI, 111) ORDER BY DATE DESC;</pre>


  </div>

</body>