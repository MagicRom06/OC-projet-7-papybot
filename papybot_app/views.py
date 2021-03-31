from flask import Flask, render_template, request
from flask import jsonify
from .grandpapybot import GrandPapyBot


app = Flask(__name__)

app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/' , methods = ['GET', 'POST'])
def index():
	return render_template('index.html')


@app.route('/answer')
def answer():
	question = request.args.get('question')
	response = GrandPapyBot().getResponse(question)
	if "7 cité Paradis, 75010 Paris" in response:
		return jsonify({"answer":GrandPapyBot().getResponse(question), "map": [48.87490994630691, 2.350530240516839]})
	else:
		return jsonify({"answer":GrandPapyBot().getResponse(question)})


if __name__ == '__main__':
	app.run()
