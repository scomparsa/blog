# -*- coding:utf-8 -*-

from abstable import DBProxy, ensure_close

class Item(DBProxy):
   
    @property 
    def tablename(self):
        return 'item'

    @ensure_close
    def create_table(self):
        cursor = self.conn.cursor()
        query = 'CREATE TABLE IF NOT EXISTS %s (' \
			'id BIGINT(20) NOT NULL,' \
            't_id BIGINT(20) NOT NULL,' \
            'title VARCHAR(256) NOT NULL,' \
            'description TEXT DEFAULT NULL,' \
            'price VARCHAR(16) NOT NULL,' \
            'cover VARCHAR(256) NOT NULL,' \
            'link TEXT DEFAULT NULL,' \
            'type TINYINT(4) NOT NULL,' \
            'created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,' \
            'delflag TINYINT(4) NOT NULL DEFAULT 0,' \
            'INDEX index_item_type (type),' \
            'UNIQUE KEY unique_item_t_id (t_id),' \
			'PRIMARY KEY (id)' \
            ') ENGINE=INNODB DEFAULT CHARSET=UTF8;' % self.tablename
        cursor.execute(query)
        cursor.close()
        self.conn.commit()

    def add(self, id, t_id, title, desc, price, cover, link, type, delflag):
        query = 'INSERT INTO %s (id, t_id, title, description, price, cover, link, type, delflag) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.execute(query, id, t_id, title, desc, price, cover, link, type, delflag)

    def check_exist(self, t_id, id=None):
        query = 'SELECT id FROM %s WHERE t_id=?'
        params = [t_id]
        if id:
            query += ' AND id<>?'
            params.append(id)
        query += ' LIMIT 1'
        return self.get(query, *params)

    def single(self, id):
        query = 'SELECT id, t_id, title, description as "desc", price, cover, link, type, created_at, delflag FROM %s WHERE id=? LIMIT 1'
        return self.get(query, id)

    def list(self):
        query = 'SELECT id, t_id, title, description as "desc", price, cover, link, type, created_at, delflag FROM %s ORDER BY id DESC'
        return self.query(query)

    def update(self, id, t_id, title, desc, price, cover, link, type, delflag):
        query = 'UPDATE %s SET t_id=?, title=?, description=?, price=?, cover=?, link=?, type=?, delflag=? WHERE id=?'
        self.execute(query, t_id, title, desc, price, cover, link, type, delflag, id)