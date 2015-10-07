import unidecode
from flask import session
from flask_login import current_user
from flask_themes2 import render_theme_template
from leancloudbb._compat import text_type
import re
from leancloudbb.utils.settings import leancloudbb_config

__author__ = 'pan'

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug.
    Taken from the Flask Snippets page.

   :param text: The text which should be slugified
   :param delim: Default "-". The delimeter for whitespace
    """
    text = unidecode.unidecode(text)
    result = []
    for word in _punct_re.split(text.lower()):
        if word:
            result.append(word)
    return text_type(delim.join(result))

def render_template(template, **context):  # pragma: no cover
    """A helper function that uses the `render_theme_template` function
    without needing to edit all the views
    """
    if current_user.is_authenticated() and current_user.theme:
        theme = current_user.theme
    else:
        theme = session.get('theme', leancloudbb_config['DEFAULT_THEME'])
    return render_theme_template(theme, template, **context)


def crop_title(title, length=None, suffix="..."):
    """Crops the title to a specified length

    :param title: The title that should be cropped

    :param suffix: The suffix which should be appended at the
                   end of the title.
    """
    length = leancloudbb_config['TITLE_LENGTH'] if length is None else length

    if len(title) <= length:
        return title

    return title[:length].rsplit(' ', 1)[0] + suffix
