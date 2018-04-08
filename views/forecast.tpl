<!-- Import siimple -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/siimple@3.0.0/dist/siimple.css">

<!-- styles -->
<style>
    body {
        margin: 0px;
    }
</style>

<meta content="width=device-width,initial-scale=1.0" name="viewport">

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
                <div class="siimple-table-row">
                    <div class="siimple-table-cell"></div>
                    <div class="siimple-table-cell"></div>
                    <div class="siimple-table-cell"></div>
                </div>
                %end
            </div>
        </div>

        <p class="siimple-p"><span class="siimple-tag siimple-tag--navy">SQL文</span></p>

        <pre class="siimple-pre">SELECT CONVERT(VARCHAR, NICHIJI, 111) AS DATE, MAX(TEMP1) AS MAX , MIN(TEMP1) AS MIN FROM TenkiDemo GROUP BY CONVERT(VARCHAR, NICHIJI, 111) ORDER BY DATE DESC;</pre>
    </div>
    
</body>