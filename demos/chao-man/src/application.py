# -*- coding:utf8 -*-

import traceback
import tornado.web

from tornado.web import asynchronous
from tornado import gen
from logger import get_logger, close_logger
from definition import TEMPLATE_PATH, STATIC_PATH, LOG_NAME, LOG_FILE
from config import DB_SETTINGS
from view import View
from db import DBProxy
from utils import transfer_normal_params

class Application(tornado.web.Application):

    def __init__(self, debug=True):
        handlers = [
            (r'^/*', tornado.web.RedirectHandler, {'url':'/index', 'permanent':True}),
            (r'^/admin$', tornado.web.RedirectHandler, {'url':'/admin/items', 'permanent':True}),

            # View
            (r'^/index$', IndexHandler),
            (r'^/admin/login$', AdminLoginHandler),
            (r'^/admin/items$', AdminItemsHandler),

            # Ajax
            (r'^/ajax/login$', AjaxLoginHandler),
            (r'^/ajax/item/check$', AjaxItemCheckHandler),
            (r'^/ajax/item/add$', AjaxItemAddHandler),
            (r'^/ajax/item/update$', AjaxItemUpdateHandler),
        ]

        settings = dict(
            template_path = TEMPLATE_PATH,
            static_path = STATIC_PATH,
            debug = debug,
            autoescape = None,
            login_url = '/admin/login',
            cookie_secret = '11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo='
        )
            
        tornado.web.Application.__init__(self, handlers, **settings)
        self.logger = get_logger(LOG_NAME, LOG_FILE)
        self.db = DBProxy(DB_SETTINGS)
        
    def close(self):
        close_logger(self.logger)
        self.db.close()

class BaseHandler(tornado.web.RequestHandler):
    ''' tornado basehandler class '''
    
    @property
    def logger(self):
        return self.application.logger

    @property
    def db(self):
        return self.application.db 
    
    def view_name(self):
        raise NotImplementedError

class UnLoginHandler(BaseHandler):
    ''' no need login handler '''
    
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.__view = getattr(View(self, self.db, self.logger), self.view_name())

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, **kwargs):
        yield gen.Task(self.service, **kwargs)

    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, **kwargs):
        yield gen.Task(self.service, **kwargs)

    def service(self, **kwargs):
        try:
            callback = kwargs.pop('callback')
            valid, params = transfer_normal_params(self.request.arguments)
            if valid:
                params.update(kwargs)
                # pagination(params)
                callback = self.__view(params)
                if self.request.method.lower() == 'post':
                    self.write(callback)
        except Exception, e:
            self.logger.error('error_arg\t%s' % (str(self.request.arguments)))
            self.logger.error('error_msg\t%s' % (str(e),))
            self.logger.error('error_trace\t%s' % (str(traceback.format_exc()),))
        finally:
            if not self._finished:
                self.finish()

class NeedLoginHandler(BaseHandler):
    ''' no need login handler '''
    
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.__view = getattr(View(self, self.db, self.logger), self.view_name())
        
    def get_current_user(self):
        user_id = self.get_secure_cookie('user_id')
        if not user_id: 
            return None
        else:
            return user_id

    # def permission_check(self):
    #     # 检查帐户是否可用
    #     user_id = self.get_current_user()

    #     if not self.db.user.getone(user_id):
    #         self.clear_all_cookies()
    #         return False

    #     if self.get_secure_cookie('is_superadmin') == '1':
    #         return True

    #     user_group_ids = [str(dic['groupId']) for dic in self.db.user_group.get_groups(user_id)]
    #     permission_group_list = self.db.permission_group.getbatch(','.join(user_group_ids)) if user_group_ids else []
    #     permission_ids = []
    #     for permission_group in permission_group_list:
    #         pids = json.loads(permission_group['permissionIds'])
    #         for pid in pids:
    #             if pid not in permission_ids:
    #                 permission_ids.append(str(pid))
    #     permission_list = self.db.permission.getbatch(','.join(permission_ids)) if permission_ids else []
    #     for permission in permission_list:
    #         if self.request.uri.startswith(permission['url']):
    #             return True

    #     return False

    @tornado.web.authenticated
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, **kwargs):
        yield gen.Task(self.service, **kwargs)

    @tornado.web.authenticated
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, **kwargs):
        yield gen.Task(self.service, **kwargs)

    def service(self, **kwargs):
        try:            
            callback = kwargs.pop('callback')
            request_method = self.request.method.lower()

            # if not any(self.request.uri.startswith(i) for i in UNNEED_PERMISSION_CHECK_URL):
            #     if not self.permission_check():
            #         if request_method == 'get':
            #             callback = self.redirect('/permission_denied')
            #         if self.request.method.lower() == 'post':
            #             self.write('permission_denied')
            #         return

            valid, params = transfer_normal_params(self.request.arguments)
            if valid:
                params.update(kwargs)
                # params.update(self.params())
                callback = self.__view(params)
                if request_method == 'post':
                    self.write(callback)
        except Exception, e:
            self.logger.error('error_arg\t%s' % (str(self.request.arguments)))
            self.logger.error('error_msg\t%s' % (str(e),))
            self.logger.error('error_trace\t%s' % (str(traceback.format_exc()),))
        finally:
            if not self._finished:
                self.finish()

class IndexHandler(UnLoginHandler):
    def view_name(self):
        return 'index'

class AdminLoginHandler(UnLoginHandler):
    def view_name(self):
        return 'admin_login'

class AdminItemsHandler(NeedLoginHandler):
    def view_name(self):
        return 'admin_items'

class AjaxLoginHandler(UnLoginHandler):
    def view_name(self):
        return 'ajax_login'

class AjaxItemCheckHandler(NeedLoginHandler):
    def view_name(self):
        return 'ajax_item_check'

class AjaxItemAddHandler(NeedLoginHandler):
    def view_name(self):
        return 'ajax_item_add'

class AjaxItemUpdateHandler(NeedLoginHandler):
    def view_name(self):
        return 'ajax_item_update'