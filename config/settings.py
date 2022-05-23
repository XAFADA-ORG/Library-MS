from datetime import timedelta

DEBUG = True
LOG_LEVEL = 'DEBUG'
SECRET_KEY = 'abdinafac'

# SQLAlchemy.
# db_uri = 'postgresql://postgres:970894cC@localhost:5432/HMS_flask'
db_uri = 'postgresql://postgres:ali12.,ali@192.168.1.12:5432/Library_MS'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = db_uri


# User.
SEED_ADMIN_EMAIL = "adminstrator@gmail.com"
SEED_ADMIN_PASSWORD = "123"
SEED_ADMIN_USER = "adminstrator"
PERMANENT_SESSION_LIFETIME = timedelta(minutes=120)
REMEMBER_COOKIE_DURATION = timedelta(minutes=60)
SESSION_COOKIE_HTTPONLY = True