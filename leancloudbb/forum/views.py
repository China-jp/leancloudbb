from flask import Blueprint
import datetime

__author__ = 'pan'

forum = Blueprint("forum", __name__)


@forum.route("/")
def index():
    return datetime.datetime.now()
