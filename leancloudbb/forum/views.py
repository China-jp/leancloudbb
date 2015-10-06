from flask import Blueprint, render_template
import datetime
from leancloud import Query, User
from leancloudbb.forum.models import Category

__author__ = 'pan'

forum = Blueprint("forum", __name__)


@forum.route("/")
def index():
    # categories = Category.get_all()
    user_count = Query(User).count()
    return render_template("forum/index.html",
                           user_count=user_count)
