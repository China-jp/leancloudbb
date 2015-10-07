from flask import Blueprint
import datetime
from leancloud import Query, User
from leancloudbb.forum.models import Category
from leancloudbb.utils.helpers import render_template

__author__ = 'pan'

forum = Blueprint("forum", __name__)


@forum.route("/")
def index():
    categories = Category.get_all()
    user_count = Query(User).count()

    newest_user = Query(User).descending("created_at").first()
    return render_template("forum/index.html",
                           categories=categories,
                           user_count=user_count,
                           newest_user=newest_user)
