<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/siimple@3.0.0/dist/siimple.css">

<style>
    body {
        margin: 0px;
    }
</style>

<meta content="width=device-width,initial-scale=1.0" name="viewport">

<head>
  <title>demoform</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>

<body>

  <div class="siimple-content--small">

    <div class="siimple-h2">demoform</div>

    <b>検索語句を入れてください。</b>
    <form id="demoform" action="javascript:void(0);">
    testname :<input type="text" id="testnameran" name="testname" />
    testitem :<input type="text" id="testitemran" name="testitem" />
    <input id="testbtn" type="submit" value="送信" /> <input type="reset" value="取り消し" />
    </form>

  </div>
</body>

<script type="text/javascript">

$("#testbtn").on("click", function () {

  // 一括してフォームデータを取得
  var formData = $("#demoform").serialize();
  console.log(formData);

  $.ajax({
      url: "/demoform",  //POST送信を行うファイル名を指定
      type: "POST",
      data: formData,  //POST送信するデータを指定（{ 'hoge': 'hoge' }のように連想配列で直接書いてもOK）
      datatype: "json"
  })
  .done(function(data){
    $("#testnameran").val(data.testname);
    $("#testitenran").val(data.testitem);
    alert("OKのはず。");

  });

});

</script>