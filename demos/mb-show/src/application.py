# -*- coding:utf8 -*-

import traceback
import tornado.web

from tornado.web import asynchronous
from tornado import gen
from logger import get_logger, close_logger
from definition import TEMPLATE_PATH, STATIC_PATH, LOG_NAME, LOG_FILE

class Application(tornado.web.Application):

    def __init__(self, debug=True):
        handlers = [
            (r'^/tyjs$', TYJSHandler), # 体院健帅
        ]

        settings = dict(
            template_path = TEMPLATE_PATH,
            static_path = STATIC_PATH,
            debug = debug,
            autoescape = None
        )
            
        tornado.web.Application.__init__(self, handlers, **settings)
        self.logger = get_logger(LOG_NAME, LOG_FILE)
        
    def close(self):
        close_logger(self.logger)

class BaseHandler(tornado.web.RequestHandler):
    ''' tornado basehandler class '''
    
    @property
    def logger(self):
        return self.application.logger
    
    def template_name(self):
        raise NotImplementedError

class UnLoginHandler(BaseHandler):
    ''' no need login handler '''
    
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, **kwargs):
        yield gen.Task(self.service, **kwargs)

    def service(self, **kwargs):
        try:
            callback = kwargs.pop('callback')
            callback = self.render('%s.html' % self.template_name())
        except Exception, e:
            self.logger.error('error_arg\t%s' % (str(self.request.arguments)))
            self.logger.error('error_msg\t%s' % (str(e),))
            self.logger.error('error_trace\t%s' % (str(traceback.format_exc()),))
        finally:
            if not self._finished:
                self.finish()

class TYJSHandler(UnLoginHandler):
    def template_name(self):
        return 'tyjs'