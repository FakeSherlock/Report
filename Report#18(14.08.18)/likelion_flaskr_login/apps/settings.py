import os
from datetime import timedelta
"""
settings.py

Configuration for Flask app

"""


class Config(object):
	# Set secret key to use session
	SECRET_KEY = "likelion-flaskr-secret-key"
	debug = False
	PERMANENT_SESSION_LIFETIME = timedelta(minutes=2)


class Production(Config):
	debug = True
	CSRF_ENABLED = False
	ADMIN = "kant2010@naver.com"
	SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///blog?instance=fakesherlock1984:fakesherlock-db'
	migration_directory = 'migrations'