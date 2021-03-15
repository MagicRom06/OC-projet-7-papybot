from flask import Flask


app = Flask(__name__)

app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
	return 'Hello world'

if __name__ == '__main__':
	app.run()
