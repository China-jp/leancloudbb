import unidecode
from leancloudbb._compat import text_type
import re

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
