# -*- coding: utf-8 -*-
from flask import Flask
from leancloudbb.extensions import csrf, login_manager
from leancloudbb.forum.views import forum


def create_app(config=None):
    """Creates the app."""

    # Initialize the app
    app = Flask("leancloudbb")

    # Use the default config and override it afterwards
    app.config.from_object('leancloudbb.configs.default.DefaultConfig')
    # Update the config
    app.config.from_object(config)

    configure_blueprints(app)
    configure_extensions(app)

    return app


def configure_blueprints(app):
    app.register_blueprint(forum, url_prefix=app.config["FORUM_URL_PREFIX"])

def configure_extensions(app):
    # Flask-WTF CSRF
    csrf.init_app(app)
    
    # Flask-Login
    login_manager.login_view = app.config["LOGIN_VIEW"]
    login_manager.refresh_view = app.config["REAUTH_VIEW"]


    login_manager.init_app(app)