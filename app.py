from flask import Flask, render_template
import json
import plotly
import datetime

app = Flask(__name__)

import csv

with open('data_clean.csv', newline='') as csvfile:
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
		data_t.append(datetime.datetime.now() - datetime.timedelta(seconds=point))

	print(data_t)

	data = [dict(x=data_t, y=data_y, type='scatter')]
	layout = dict(title='Dashboard', paper_bgcolor='rgba(0,0,0,0.5)',plot_bgcolor='rgba(0,0,0,0.5)', plot_color='rgba(0,0,0,0.5)')

	graphs = [dict(data=data, layout=layout)]
	ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
	graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
	return render_template('index.html',ids=ids,graphJSON=graphJSON)

if __name__ == '__main__':
    app.run()
