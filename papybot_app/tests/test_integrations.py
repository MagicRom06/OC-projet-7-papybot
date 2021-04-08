import json

import flask
import pytest

from ..views import app


@pytest.fixture
def client():
    """
    pre-config for app tests
    """
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'TEST.localhost'
    client = app.test_client()
    with app.app_context():
        pass
    app.app_context().push()
    yield client


def test_index(client):
    """
    testing index route is reachable and
    PapyBot in displayed
    """
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'PapyBot' in rv.data


def test_index_post(client):
    """
    testing post request from index
    """
    rv = client.post(
        "/",
        data="question=TEST AJAX",
        content_type='application/x-www-form-urlencoded',)
    assert rv.status_code == 200


def test_anwser(client):
    """
    testing answer route is reachable with url parameters
    and testing if the right answer is displayed
    """
    rv = client.get('/answer?question=merci')
    assert rv.status_code == 200
    assert b'answer' in rv.data
    data = json.loads(rv.get_data(as_text=True))
    assert data['answer'] == "De rien jeune padawan"
