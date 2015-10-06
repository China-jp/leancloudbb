# -*- coding: utf-8 -*-
from flask import Flask
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

    return app


def configure_blueprints(app):
    app.register_blueprint(forum, url_prefix=app.config["FORUM_URL_PREFIX"])
