import pytest
import flask
from ..views import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	app.config['SERVER_NAME'] = 'TEST.localhost'
	client = app.test_client()
	with app.app_context():
		pass
	app.app_context().push()
	yield client

def test_index(client):
	rv = client.get('/')
	assert rv.status_code == 200
	assert b'PapyBot' in rv.data

def test_index_post(client):
	rv = client.post("/", data="question=TEST AJAX", content_type='application/x-www-form-urlencoded',)
	assert rv.status_code == 200

def test_anwser(client):
	rv = client.get('/answer?question=merci')
	assert rv.status_code == 200
	assert b'answer' in rv.data
	with app.test_request_context('/answer?question=merci'):
		assert flask.request.path == '/answer'
		assert flask.request.args['question'] == 'merci'
