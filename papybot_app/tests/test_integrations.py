import pytest
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
