# -*- coding:utf8 -*-

import json

class View:

    def __init__(self, request_handler, logger):
        self.render = request_handler.render
        self.redirect = request_handler.redirect
        self.request = request_handler.request
        self.write = request_handler.write
        self.logger = logger

    def __render(self, template_path, page_type=None, **kwargs):
        render_dic = { 'page_type': page_type or template_path.split('.')[0] }
        render_dic.update(kwargs)
        self.render(template_path, **render_dic)

    def __resp(self, resp={}, status='success'):
        resp_dic = { 'status': status }
        resp_dic.update(resp)
        return json.dumps(resp_dic)

    def note_drafts(self, params):
        self.__render('note_drafts.html')

    def note_draft(self, params):
        self.__render('note_draft.html', **params)        