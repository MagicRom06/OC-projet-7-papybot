import json
import os

import flask
import googlemaps
import pytest
from wikipedia import summary

from ..grandpapybot import GrandPapyBot
from ..views import app
from .googlemapmock import GoogleMapMock


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


def test_anwser(client):
    """
    testing answer route is reachable with url parameters
    and testing if the right answer is displayed
    """
    rv = client.get('/answer?question=merci')
    assert rv.status_code == 200
    assert b'answer' in rv.data
    data = json.loads(rv.get_data(as_text=True))
    assert data['answer'] == {"papy": "De rien jeune padawan"}


def test_search_adress(client):
    """
    testing adress searching
    """
    rv = client.get("/answer?question=tu connais l'adresse de openclassrooms ?")
    assert rv.status_code == 200
    assert b'answer' in rv.data
    data = json.loads(rv.get_data(as_text=True))
    assert data['answer'] == {"location": {"lat": 48.8975156, "lng": 2.3833993}, "papy": "Bien sûr mon poussin ! La voici: 10 Quai de la Charente, 75019 Paris, France.", "wiki": "OpenClassrooms est un site web de formation en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur des métiers en croissance. Ses contenus sont réalisés en interne, par des écoles, des universités, des entreprises partenaires comme Microsoft ou IBM, ou historiquement par des bénévoles."}


def test_search_movie(client):
    """
    testing movie searching
    """
    rv = client.get("/answer?question=tu connais le film sacré graal ?")
    assert rv.status_code == 200
    assert b'answer' in rv.data
    data = json.loads(rv.get_data(as_text=True))
    assert data['answer'] == {'movie': "Monty Python : Sacré Graal ! (Monty Python and the Holy Grail) est un film britannique sorti en 1975, écrit et réalisé par Terry Gilliam et Terry Jones de la troupe des Monty Python.", "papy": "oui j'adore ce film !"}


def test_search_book(client):
    """
    testing book searching
    """
    rv = client.get("/answer?question=tu connais le livre un bonheur insoutenable ?")
    assert b'answer' in rv.data
    data = json.loads(rv.get_data(as_text=True))
    assert data['answer'] == {'book': "Un bonheur insoutenable (titre original This Perfect Day) est un roman d'anticipation dystopique américain d'Ira Levin, publié en 1970.\n\n\n== Histoire ==\nL'action se situe dans l'avenir, après l'année 2000.", 'papy': "oui j'adore ce livre !"}


def test_mocking_find_wiki(mocker):
    """
    mock wikimedia api
    """
    mocker.patch('wikipedia.summary', return_value="wiki answer")
    assert GrandPapyBot.findAnswer('tu connais livre 1984 ?') == {'book': 'wiki answer', 'papy': 'oui j\'adore ce livre !'}


def test_mocking_find_adress(mocker):
    """
    mock google api
    """
    mock = mocker.patch('googlemaps.Client', return_value= GoogleMapMock())
    mock = mocker.patch('wikipedia.summary', return_value="info wiki")
    assert GrandPapyBot.findAnswer("tu connais l'adresse de openclassrooms ?") == {'papy': 'Bien sûr mon poussin ! La voici: adress.', 'wiki': 'info wiki', 'location': 'info location'}
