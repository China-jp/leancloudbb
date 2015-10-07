# -*- coding: utf-8 -*-

import pickle
from flask import abort

from wtforms import (TextField, IntegerField, FloatField, BooleanField,
                     SelectField, SelectMultipleField, validators)
from flask_wtf import Form
from leancloud import Object, Query, LeanCloudError

from leancloudbb._compat import max_integer, text_type, iteritems


class SettingsGroup(Object):
    @property
    def key(self):
        return self.get("key")

    @property
    def name(self):
        return self.get("name")

    @property
    def description(self):
        return self.get("description")

    @property
    def settings(self):
        return Query(Setting).equal_to("settingsgroup", self).find()


class Setting(Object):
    @property
    def key(self):
        return self.get("key")


    @property
    def value(self):
        return self.get("value")

    @property
    def settingsgroup(self):
        return self.get("settingsgroup")

    # The name (displayed in the form)
    @property
    def name(self):
        return self.get("name")

    # The description (displayed in the form)
    @property
    def description(self):
        return self.get("description")

    # Available types: string, integer, float, boolean, select, selectmultiple
    @property
    def value_type(self):
        return self.get("value_type")

    # Extra attributes like, validation things (min, max length...)
    # For Select*Fields required: choices
    @property
    def extra(self):
        return pickle.loads(self.get("extra"))

    @classmethod
    def get_form(cls, group):
        """Returns a Form for all settings found in :class:`SettingsGroup`.

        :param group: The settingsgroup name. It is used to get the settings
                      which are in the specified group.
        """

        class SettingsForm(Form):
            pass

        # now parse the settings in this group
        for setting in group.settings:
            field_validators = []

            if setting.value_type in ("integer", "float"):
                validator_class = validators.NumberRange
            elif setting.value_type == "string":
                validator_class = validators.Length

            # generate the validators
            if "min" in setting.extra:
                # Min number validator
                field_validators.append(
                    validator_class(min=setting.extra["min"])
                )

            if "max" in setting.extra:
                # Max number validator
                field_validators.append(
                    validator_class(max=setting.extra["max"])
                )

            # Generate the fields based on value_type
            # IntegerField
            if setting.value_type == "integer":
                setattr(
                    SettingsForm, setting.key,
                    IntegerField(setting.name, validators=field_validators,
                                 description=setting.description)
                )
            # FloatField
            elif setting.value_type == "float":
                setattr(
                    SettingsForm, setting.key,
                    FloatField(setting.name, validators=field_validators,
                               description=setting.description)
                )

            # TextField
            elif setting.value_type == "string":
                setattr(
                    SettingsForm, setting.key,
                    TextField(setting.name, validators=field_validators,
                              description=setting.description)
                )

            # SelectMultipleField
            elif setting.value_type == "selectmultiple":
                # if no coerce is found, it will fallback to unicode
                if "coerce" in setting.extra:
                    coerce_to = setting.extra['coerce']
                else:
                    coerce_to = text_type

                setattr(
                    SettingsForm, setting.key,
                    SelectMultipleField(
                        setting.name,
                        choices=setting.extra['choices'](),
                        coerce=coerce_to,
                        description=setting.description
                    )
                )

            # SelectField
            elif setting.value_type == "select":
                # if no coerce is found, it will fallback to unicode
                if "coerce" in setting.extra:
                    coerce_to = setting.extra['coerce']
                else:
                    coerce_to = text_type

                setattr(
                    SettingsForm, setting.key,
                    SelectField(
                        setting.name,
                        coerce=coerce_to,
                        choices=setting.extra['choices'](),
                        description=setting.description)
                )

            # BooleanField
            elif setting.value_type == "boolean":
                setattr(
                    SettingsForm, setting.key,
                    BooleanField(setting.name, description=setting.description)
                )

        return SettingsForm

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def update(cls, settings, app=None):
        """Updates the cache and stores the changes in the
        database.

        :param settings: A dictionary with setting items.
        """
        # update the database
        for key, value in iteritems(settings):
            setting = Query(cls).equal_to("key", key.lower()).first()

            setting.value = value

            setting.save()

    @classmethod
    def get_settings(cls, from_group=None):
        """This will return all settings with the key as the key for the dict
        and the values are packed again in a dict which contains
        the remaining attributes.

        :param from_group: Optionally - Returns only the settings from a group.
        """
        result = None
        if from_group is not None:
            result = from_group.settings
        else:
            result = cls.query.all()

        settings = {}
        for setting in result:
            settings[setting.key] = {
                'name': setting.name,
                'description': setting.description,
                'value': setting.value,
                'value_type': setting.value_type,
                'extra': setting.extra
            }

        return settings

    @classmethod
    def as_dict(cls, from_group=None, upper=True):
        """Returns all settings as a dict. This method is cached. If you want
        to invalidate the cache, simply execute ``self.invalidate_cache()``.

        :param from_group: Returns only the settings from the group as a dict.
        :param upper: If upper is ``True``, the key will use upper-case
                      letters. Defaults to ``False``.
        """

        settings = {}
        result = None
        if from_group is not None:
            try:
                result = Query(SettingsGroup).equal_to("key", from_group).find()
            except LeanCloudError, e:
                if e.code == 101:
                    abort(404)
            result = result.settings
        else:
            print(Query(Setting))
            result = Query(cls).find()

        for setting in result:
            if upper:
                setting_key = setting.key.upper()
            else:
                setting_key = setting.key

            settings[setting_key] = setting.value

        return settings
