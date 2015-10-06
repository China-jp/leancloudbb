from flask import current_app
from leancloudbb import create_app
from flask_script import Manager, Server
from leancloudbb.utils.populate import create_test_data

__author__ = 'pan'

# Use the development configuration if available
try:
    from leancloudbb.configs.development import DevelopmentConfig as Config
except ImportError:
    from leancloudbb.configs.default import DefaultConfig as Config

app = create_app(Config)
manager = Manager(app)

manager.add_command("runserver", Server("localhost", port=5000))

if __name__ == "__main__":
    manager.run()
