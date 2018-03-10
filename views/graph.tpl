<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/jquery.jqplot.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/plugins/jqplot.dateAxisRenderer.js"></script>
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/jquery.jqplot.min.css"/>

<h1>気象台</h1>
<p><a href="./">表紙</a></p>
<div id="chart" style="height:400px;"></div>

<script>

    function getData() {
        var data = '[[[]]]';
        $.ajax({
            async: false,
            url: '/data',
            type: 'GET',
            dataType: 'json',
        }).done(function(json) {
            data = json
        });
        return data;
    };

$(function() {

    var options = {
        title: '南さいたまの気温',
        axes: {
            xaxis: {
                renderer: $.jqplot.DateAxisRenderer,
                tickOptions: { formatString: '%m/%d %H:%M' },
            }
        },
    };

    var jqplot = $.jqplot('chart', getData(), options);
});
</script>

