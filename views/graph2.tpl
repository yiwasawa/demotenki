<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/jquery.jqplot.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/plugins/jqplot.cursor.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/plugins/jqplot.dateAxisRenderer.js"></script>
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/jquery.jqplot.min.css"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/siimple@3.0.0/dist/siimple.css">

<!-- Test styles -->
<style>
  body
  {
    margin: 40px;
  }
  .chart
  {
    padding: 20px;
  }
</style>


<head>
	<title>気象台 > グラフ</title>
</head>

<body>

	<div class="siimple-content--small">
		
		<div class="siimple-h2">気象台</div>
		
		<p class="siimple-p"><a href="./" class="siimple-link">表紙</a></p>
		
		<div class="siimple-h3">グラフ</div>

		<!--
		<form id="form">
			<div class="siimple-form">
				<input type="datetime-local" id="start">
				<span>　～　</span>
				<input type="datetime-local" id="end">
			</div>
		</form>
		-->

		<!--
		<div class="siimple-form">
			<div class="siimple-form-field-label">出力開始日</div>
			<input type="date" id="start">
			<div class="siimple-form-field-label">出力終了日</div>
			<input type="date" id="end">
		</div>
		-->
		
		<div class="siimple-tip siimple-tip--teal">
			グラフ上で期間を選択するとズームできます。ダブルクリックでもどります。
		</div>
		
		<div id="chart" style="height:400px;"></div>
	
	</div>

</body>

<script>

	function getData() {
		var data = '[[[]]]';
		$.ajax({
			async: false,
			url: '/data2',
			type: 'GET',
			dataType: 'json',
		}).done(function(json) {
			data = json
		});
		return data;
	};

	function getTokyoData() {
		var data = '[[[]]]';
		$.ajax({
			async: false,
			url: '/tokyodata',
			type: 'GET',
			dataType: 'json',
		}).done(function(json) {
			data = json
		});
		return data;
	};

	function getSaitamaData() {
		var data = '[[[]]]';
		$.ajax({
			async: false,
			url: '/saitamadata',
			type: 'GET',
			dataType: 'json',
		}).done(function(json) {
			data = json
		});
		return data;
	};
	
	function str2unixtime(str){
		var date = new Date(str);
		return date.getTime();
	}

	$(function(){

		var options = {
			// title: 'さまざまな気温',
			axes: {
				xaxis: {
					renderer: $.jqplot.DateAxisRenderer,
					// renderer: jQuery . jqplot . DateAxisRenderer,
					tickOptions: { formatString: '%m/%d %H:%M' },
					// tickOptions: { formatString: '%D' },
				},
			},

			grid: {
				background: '#fff',
				shadow: false
			},

			seriesDefaults: {
				shadow: false,
				lineWidth: 1,
				markerOptions: {
					show: false
				},
			},
			series: [
					{ label: '自宅＠南さいたま' },
					{ label: '東京' },
					{ label: '札幌' }
			],
			legend: {
					show: true,
					location: 'ne',
			},
			cursor: {
					show: true,
					zoom: true,
					constrainZoomTo: 'x',
			},

		};

		var jqplot = $.jqplot('chart', [getData(), getTokyoData(), getSaitamaData()], options);

		/*
		$('#start').change(function(){
			var hizuke = $('#start').val() + 'T00:00';
			console.log('グラフの開始時刻が設定されました。\n' + '日時 = ' + hizuke);
			// var unix_time = str2unixtime($('#start').val());
			var unix_time = str2unixtime(hizuke);
			var opt = options;
			opt.axes.xaxis.min = unix_time;
			jqplot.replot(opt);
		});

		$('#end').change(function(){
			var hizuke = $('#end').val() + 'T23:59';
			console.log('グラフの終了時刻が設定されました。\n' + '日時 = ' + hizuke);
			// var unix_time = str2unixtime($('#end').val());
			var unix_time = str2unixtime(hizuke);
			var opt = options;
			opt.axes.xaxis.max = unix_time;
			jqplot.replot(opt);
		});
		*/


	});

</script>
