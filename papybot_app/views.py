from flask import Flask, jsonify, render_template, request

from .grandpapybot import GrandPapyBot

# initialize flask.
app = Flask(__name__)

# load flask config.
app.config.from_object('config.Config')


@app.route('/')
def index():
    """
    index route displaying main page app.
    """
    return render_template('index.html')


@app.route('/answer')
def answer():
    """
    answer route displaying papy answer in json format.
    """
    question = request.args.get('question')
    response = GrandPapyBot().getResponse(question)
    return jsonify({"answer": response})


if __name__ == '__main__':
    app.run()
