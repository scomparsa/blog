# -*- coding:utf8 -*-

import json

from definition import ITEM_TYPE
from utils import datetime_to_str
from service.idworker import IDWorker

class View:

    def __init__(self, request_handler, db, logger):
        self.render = request_handler.render
        self.redirect = request_handler.redirect
        self.request = request_handler.request
        self.write = request_handler.write
        self.db = db 
        self.logger = logger
        # self.host = '%s://%s' % (request_handler.request.protocol, request_handler.request.host)
        # self.url = '%s://%s%s' % (request_handler.request.protocol, request_handler.request.host, request_handler.request.uri)
        # self.mode = mode
        self.set_secure_cookie = request_handler.set_secure_cookie
        self.get_secure_cookie = request_handler.get_secure_cookie
        self.clear_cookie = request_handler.clear_cookie
        self.clear_all_cookies = request_handler.clear_all_cookies

        # if 'HTTP_X_FORWARDED_FOR' in request_handler.request.headers:
        #     self.ip = request_handler.request.headers['HTTP_X_FORWARDED_FOR']
        # else:
        #     self.ip = request_handler.request.remote_ip
        
        self.user_id = self.get_secure_cookie('user_id') or 0
        self.user_email = self.get_secure_cookie('email')
        self.is_super = self.get_secure_cookie('is_super') or 0

        self.idworker = IDWorker(1, 1)
        # self.muma_proxy = MumaProxy()
        # self.qiniu_setting = qiniu_setting()

    def __render(self, template_path, page_type=None, **kwargs):
        render_dic = {
            'page_type': page_type or template_path.split('.')[0],
            # 'page': kwargs.pop('page', 1),
            # 'order': kwargs.pop('order', 'desc')
        }
        render_dic.update(kwargs)
        self.render(template_path, **render_dic)

    def __resp(self, resp={}, status='success'):
        resp_dic = { 'status': status }
        resp_dic.update(resp)
        return json.dumps(resp_dic)

    def __render_items(self, items):
        for item in items:
            item['id'] = str(item['id'])
            item['t_id'] = str(item['t_id'])
            item['type_name'] = ITEM_TYPE[item['type']]
            item['created_at'] = datetime_to_str(item['created_at'])

        return items

    def index(self, params):
        items = self.__render_items(self.db.item.list())
        self.__render('index.html', 'index', items=items)    

    def admin_login(self, params):
        self.__render('admin/login.html', 'login')

    def admin_items(self, params):
        items = self.__render_items(self.db.item.list())
        self.__render('admin/items.html', 'items', items=json.dumps(items))

    def ajax_login(self, params):
        email = params['email']
        password = params['password']

        user = self.db.admin.login(email, password)

        if not user:
            return self.__resp({ 'msg': u'登录失败' }, status='fail')

        self.set_secure_cookie('user_id', str(user['id']))
        self.set_secure_cookie('email', email)
        self.set_secure_cookie('is_super', str(user['is_super']))

        # next = params.get('next', '/')
        return self.__resp({ 'next': '/admin/items' })

    def ajax_item_check(self, params):
        t_id = params['t_id']

        if self.db.item.check_exist(t_id):
            exist = 1
        else:
            exist = 0

        return self.__resp({ 'exist': exist })

    def ajax_item_add(self, params):
        id = self.idworker.get_id()
        t_id = params['t_id']
        title = params['title'].decode('utf8')
        desc = params['desc'].decode('utf8')
        price = params['price'] 
        cover = params['cover']
        link = params['link']
        type = params['type']
        delflag = params['delflag']

        if self.db.item.check_exist(t_id):
            return self.__resp({ 'msg': u'淘宝ID已存在' }, status='fail')

        self.db.item.add(id, t_id, title, desc, price, cover, link, type, delflag)
        return self.__resp()

    def ajax_item_update(self, params):
        id = params['id']
        t_id = params['t_id']
        title = params['title'].decode('utf8')
        desc = params['desc'].decode('utf8')
        price = params['price'] 
        cover = params['cover']
        link = params['link']
        type = params['type']
        delflag = params['delflag']

        if self.db.item.check_exist(t_id, id=id):
            return self.__resp({ 'msg': u'淘宝ID已存在' }, status='fail')

        self.db.item.update(id, t_id, title, desc, price, cover, link, type, delflag)
        return self.__resp({ 'item': self.__render_items([self.db.item.single(id)])[0] })