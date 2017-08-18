# -*- coding:utf-8 -*-

from abstable import DBProxy, ensure_close

class Admin(DBProxy):
   
    @property 
    def tablename(self):
        return 'admin'

    @ensure_close
    def create_table(self):
        cursor = self.conn.cursor()
        query = 'CREATE TABLE IF NOT EXISTS %s (' \
			'id INT(11) NOT NULL AUTO_INCREMENT,' \
            'email VARCHAR(64) NOT NULL,' \
            'password VARCHAR(40) NOT NULL,' \
            'created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,' \
            'is_super TINYINT(4) NOT NULL DEFAULT 0,' \
			'PRIMARY KEY (id)' \
            ') ENGINE=INNODB DEFAULT CHARSET=UTF8;' % self.tablename
        cursor.execute(query)
        cursor.close()
        self.conn.commit()

    def create(self, email, password):
        query = 'INSERT INTO %s (email, password) VALUES (?, ?)'
        self.execute(query, email, password)

    def login(self, email, password):
        query = 'SELECT id, is_super FROM %s WHERE email=? AND password=? LIMIT 1'
        return self.get(query, email, password)

    def getone(self, id):
        query = 'SELECT id, email FROM %s WHERE id=? LIMIT 1'
        return self.get(query, id)

    def getlist(self, order='desc', offset=0, **kwargs):
        query = 'SELECT id, email FROM %s WHERE id>1'
        query += ' ORDER BY id %s LIMIT ?,?' % order
        rows = self.query(query, offset, self.countperpage)
        return rows if order == 'desc' else rows[::-1]

    def update(self, id, email):
        query = 'UPDATE %s SET email=? WHERE id=?'
        self.execute(query, email, id)

    def resetpwd(self, id, pwd):
        query = 'UPDATE %s SET password=? WHERE id=?'
        self.execute(query, pwd, id)

    def delete(self, id):
        query = 'DELETE FROM %s WHERE id=?'
        self.execute(query, id)

    def check(self, email, id=None):
        query = 'SELECT id FROM %s WHERE email=?'
        params = [email]
        if id:
            query += ' AND id<>?'
            params.append(id)
        query += ' LIMIT 1'
        return self.get(query, *params)