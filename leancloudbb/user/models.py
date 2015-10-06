from flask_login import UserMixin

from leancloud import Object
__author__ = 'pan'


class UserData(Object, UserMixin):
    pass
