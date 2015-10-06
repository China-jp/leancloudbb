"""
    flaskbb.configs.development
    ~~~~~~~~~~~~~~~~~~~~

    This is the FlaskBB's development config.

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
from leancloudbb.configs.default import DefaultConfig


class DevelopmentConfig(DefaultConfig):

    # Indicates that it is a dev environment
    DEBUG = True

    # SQLAlchemy connection options
    # This will create in the applications folder (where manage.py is)
    # a database named flaskbb.sqlite.
    #SQLALCHEMY_DATABASE_URI = "postgresql://flaskbb@localhost:5432/flaskbb"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DefaultConfig._basedir + '/' + \
                              'flaskbb.sqlite'

    # This will print all SQL statements
    SQLALCHEMY_ECHO = True

    # Security
    SECRET_KEY = "Panmax"
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "i_am_panmax"

    # Recaptcha
    # To get recaptcha, visit the link below:
    # https://www.google.com/recaptcha/admin/create
    # Those keys are only going to work on localhost!
    RECAPTCHA_ENABLED = True
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = "6LcZB-0SAAAAAGIddBuSFU9aBpHKDa16p5gSqnxK"
    RECAPTCHA_PRIVATE_KEY = "6LcZB-0SAAAAAPuPHhazscMJYa2mBe7MJSoWXrUu"
    RECAPTCHA_OPTIONS = {"theme": "white"}

    # Mail
    # Local SMTP Server
    #MAIL_SERVER = "localhost"
    #MAIL_PORT = 25
    #MAIL_USE_SSL = False
    #MAIL_USERNAME = ""
    #MAIL_PASSWORD = ""
    #MAIL_DEFAULT_SENDER = "noreply@example.org"

    # Google Mail Example
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = "jiapan.china@gmail.com"
    MAIL_PASSWORD = "3839jphj"
    MAIL_DEFAULT_SENDER = ("Your Name", "967168@qq.com")

    # The user who should recieve the error logs
    ADMINS = ["jiapan00@163.com"]
