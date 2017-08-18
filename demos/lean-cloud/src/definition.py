# -*- coding:utf8 -*-

import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

PROJECT_NAME = 'lean_cloud'
REQUEST_USER_AGENT = '%s(%s;%s;%s)' % (PROJECT_NAME, PROJECT_NAME, PROJECT_NAME, PROJECT_NAME)

BASE_PATH = os.path.dirname(__file__)                                       
TEMPLATE_PATH = os.path.join(BASE_PATH, '..', 'template')                   
STATIC_PATH = os.path.join(BASE_PATH, '..', 'static')                       

LOG_NAME = '%s.log' % PROJECT_NAME
LOG_FILE = os.path.join(BASE_PATH, '..', 'data/%s' % (LOG_NAME,))