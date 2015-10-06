from flask import Blueprint

__author__ = 'pan'

forum = Blueprint("forum", __name__)


@forum.route("/")
def index():
    return "hello world!!"
