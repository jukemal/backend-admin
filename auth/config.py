import os

# Create dummy secrey key so we can use sessions
SECRET_KEY = 'c5282ad3ea38420ab8ac0326a48d3a8c'

# Create in-memory database
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
# SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = 'bf9797d59d094abb92fdca167494a7ee'

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
