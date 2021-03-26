from flask import Flask, render_template
import json
import plotly
app = Flask(__name__)


@app.route('/')
def index():
	graphs = [dict(data=[dict(x=[1, 2, 3], y=[10, 20, 30],   type='scatter'  ), ], layout=dict(  title='first graph' ))]
	ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
	graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
	return render_template('index.html',ids=ids,graphJSON=graphJSON)

if __name__ == '__main__':
    app.run()
