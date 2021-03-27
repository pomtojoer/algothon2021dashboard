from flask import Flask, render_template
import json
import plotly
import datetime
import numpy as np

app = Flask(__name__)

import csv

with open('data_cleaned.csv', newline='') as csvfile:
    data_input = list(csv.reader(csvfile))


@app.route('/')
def index():
	data_y = []

	for i in range(0, len(data_input)):
		try:
			data_y.append(float(data_input[i][0]))
		except:
			data_y.append(0)

	print(data_y)
	data_x = list(range(0,len(data_y)))

	data_t = []
	for point in data_x:
		data_t.append(datetime.datetime.now() + datetime.timedelta(hours=point) - datetime.timedelta(hours=data_x[-1]))

	data_y1 = calcSMA(data_y, 4)
	data_y2 = calcSMA(data_y, 10)
	data_y2 = calcSMA(data_y, 25)

	changeDay = 100*((data_y[-1]/data_y[-24])-1)
	displayRange = str(np.round(np.min(data_y),2))+ " - " + str(np.round(np.max(data_y),2))
	dailyVolatility = np.sqrt(np.var(data_y[-24:-1]))
	annVolatility = np.sqrt(252)*dailyVolatility

	data = [dict(x=data_t, y=data_y, name="Data", mode="lines", line={"color":"#cccccc"}, type='scatter'),dict(x=data_t, y=data_y1, name="SMA9", type='scatter'),dict(x=data_t, y=data_y2, name="SMA21", type='scatter'),dict(x=data_t, y=data_y2, name="SMA51", type='scatter')]
	layout = dict(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0.2)', title_font_color="#cccccc", xaxis={"tickfont":{"color":"#cccccc"}}, yaxis={"tickfont":{"color":"#cccccc"},"fixedrange":"true"}, margin={"l": 50,"r": 50,"b": 50,"t": 0,"pad": 4})

	graphs = [dict(data=data, layout=layout)]
	ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
	graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
	return render_template('index.html',ids=ids,graphJSON=graphJSON,endTime=data_t[-1].strftime("%Y-%m-%dT%H:%M"),startTime=data_t[0].strftime("%Y-%m-%dT%H:%M"), currentVal=np.round(data_y[-1],2), changeDay=np.round(changeDay,2), displayRange=displayRange, dailyVolatility=dailyVolatility, annVolatility=annVolatility)

def calcSMA(array, nums):
	outArray = []
	for i in range(0,len(array)):
		iMax = np.min([i+nums,len(array)])
		iMin = np.max([i-nums,0])
		arrOfInterest = array[iMin:iMax]
		outArray.append(np.mean(arrOfInterest))

	return outArray


if __name__ == '__main__':
    app.run()
