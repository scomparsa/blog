# -*- coding:utf8 -*-

import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

PROJECT_NAME = 'man-spa'
REQUEST_USER_AGENT = '%s(%s;%s;%s)' % (PROJECT_NAME, PROJECT_NAME, PROJECT_NAME, PROJECT_NAME)

BASE_PATH = os.path.dirname(__file__)                                       
TEMPLATE_PATH = os.path.join(BASE_PATH, '..', 'tmpl')                   
STATIC_PATH = os.path.join(BASE_PATH, '..', 'static')                       

LOG_NAME = '%s.log' % PROJECT_NAME
LOG_FILE = os.path.join(BASE_PATH, '..', 'data/%s' % (LOG_NAME,))

COUNTPERPAGE = 40

ITEM_TYPE = {
	1: u'衣服',
	2: u'裤子',
	3: u'鞋子',
	4: u'箱包',
	5: u'配饰'
}