function timeToChange (){

	var from = $('#timeRange_from').val();
	var to = $('#timeRange_to').val();


	graphs[0]["layout"]["xaxis"] = {range: [from, to], color:'#cccccc'};
    Plotly.newPlot(ids[0], // the ID of the div, created above
    graphs[0].data,
    graphs[0]["layout"] || {});

    graphs[0]["data"][0]

    var startIndex=graphs[0]["data"][0]["x"].findIndex(function(number) {
		return number > from;
	});

	var endIndex=graphs[0]["data"][0]["x"].findIndex(function(number) {
		return number > to;
	});


	dataRange = graphs[0]["data"][0]["y"].slice(startIndex,endIndex)
	console.log(dataRange)
    $("#rangeDisplay").text(round(Math.min(...dataRange),2).toString()+" - "+round(Math.max(...dataRange),2).toString());
}
function timeFromChange (){
	var from = $('#timeRange_from').val();
	var to = $('#timeRange_to').val();

	$("#rangeDisplay").text("hello");

	graphs[0]["layout"]["xaxis"] = {range: [from, to], color:'#cccccc'};
    Plotly.newPlot(ids[0], // the ID of the div, created above
    graphs[0].data,
    graphs[0]["layout"] || {});

    var startIndex=graphs[0]["data"][0]["x"].findIndex(function(number) {
		return number > from;
	});

	var endIndex=graphs[0]["data"][0]["x"].findIndex(function(number) {
		return number > to;
	});

	dataRange = graphs[0]["data"][0]["y"].slice(startIndex,endIndex)
	console.log(dataRange)
    $("#rangeDisplay").text(round(Math.min(...dataRange),2).toString()+" - "+round(Math.max(...dataRange),2).toString());

}

function round(value, decimals) {
 return Number(Math.round(value+'e'+decimals)+'e-'+decimals);
}  
