from flask import Flask, jsonify, render_template, request

from .grandpapybot import GrandPapyBot

app = Flask(__name__)

app.config.from_object('config.Config')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/answer')
def answer():
    question = request.args.get('question')
    response = GrandPapyBot().getResponse(question)
    return jsonify({"answer": response})


if __name__ == '__main__':
    app.run()
