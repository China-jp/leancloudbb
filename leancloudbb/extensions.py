# -*- coding: utf-8 -*-

from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect
from flask_babelex import Babel

# Login
login_manager = LoginManager()

# Babel
babel = Babel()

# CSRF
csrf = CsrfProtect()
