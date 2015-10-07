# -*- coding: utf-8 -*-

import os

import leancloud
from leancloudbb.utils.populate import create_test_data

from manage import app

APP_ID = os.environ['LC_APP_ID']
MASTER_KEY = os.environ['LC_APP_MASTER_KEY']
PORT = int(os.environ['LC_APP_PORT'])


leancloud.init(APP_ID, master_key=MASTER_KEY)

application = leancloud.Engine(app)

if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    create_test_data(users=0, categories=0)
    app.run()
