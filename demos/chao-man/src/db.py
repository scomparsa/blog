# -*- coding: utf-8 -*-

from dbpool import get_dbpool
from table.admin import Admin
from table.item import Item

class DBProxy:

    def __init__(self, db_settings):
		self.db_pool = get_dbpool(db_settings)

		self.admin = Admin(self.db_pool)
		self.item = Item(self.db_pool)

    def close(self):
		self.db_pool.close()        