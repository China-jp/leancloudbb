import pickle

from leancloud import User
from leancloudbb.forum.models import Category
from leancloudbb.management.models import SettingsGroup, Setting

__author__ = 'pan'


def create_test_data(users=5, categories=2, forums=2, topics=1, posts=1, create_settings=True):
    if create_settings:
        create_default_settings()
    # create 5 users
    for u in range(1, users + 1):
        username = "test%s" % u
        email = "test%s@example.org" % u
        user = User()
        user.set("username", username)
        user.set("password", "test")
        user.set("email", email)
        user.sign_up()

    # create 2 categories
    for i in range(1, categories + 1):
        category_title = "Test Category %s" % i
        category = Category(title=category_title,
                            description="Test Description")
        category.save()

        # create 2 forums in each category

    return "create success"


def create_default_settings():
    """Creates the default settings."""
    from leancloudbb.fixtures.settings import fixture
    create_settings_from_fixture(fixture)
   
    
def create_settings_from_fixture(fixture):
    """Inserts the settings from a fixture into the database.
    Returns the created groups and settings.

    :param fixture: The fixture which should inserted.
    """
    created_settings = {}
    for settingsgroup in fixture:
        group = SettingsGroup(
            key=settingsgroup[0],
            name=settingsgroup[1]["name"],
            description=settingsgroup[1]["description"]
        )
        group.save()
        created_settings[group] = []

        for settings in settingsgroup[1]["settings"]:
            value = pickle.dumps(settings[1]["value"])

            extra = settings[1].get("extra", "")
            if extra:
                extra = pickle.dumps(extra)
            setting = Setting(
                key=settings[0],
                value=value,
                value_type=settings[1]["value_type"],
                name=settings[1]["name"],
                description=settings[1]["description"],
                extra=extra,     # Optional field

                settingsgroup=group.key
            )
            if setting:
                setting.save()
                created_settings[group].append(setting)

    return created_settings
