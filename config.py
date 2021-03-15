import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ['SECRET_KEY']
	CSRF_ENABLED = True
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
