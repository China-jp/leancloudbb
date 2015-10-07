# -*- coding: utf-8 -*-

import collections

from leancloudbb.management.models import Setting


class LeanCloudBBConfig(collections.MutableMapping):
    """Provides a dictionary like interface for interacting with FlaskBB's
    Settings cache.
    """

    def __init__(self, *args, **kwargs):
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        return Setting.as_dict()[key]

    def __setitem__(self, key, value):
        Setting.update({key.lower(): value})

    def __delitem__(self, key):  # pragma: no cover
        pass

    def __iter__(self):
        return iter(Setting.as_dict())

    def __len__(self):
        return len(Setting.as_dict())


leancloudbb_config = LeanCloudBBConfig()
