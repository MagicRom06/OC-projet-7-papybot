from flask import Flask, render_template


app = Flask(__name__)

app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
