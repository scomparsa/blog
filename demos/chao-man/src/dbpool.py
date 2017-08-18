import oursql
from DBUtils.PooledDB import PooledDB

dbpool = None

def get_dbpool(db_settings, maxcached=3, maxconnections=3):
    global dbpool
    dbpool = PooledDB(oursql, port=db_settings['port'], host=db_settings['host'], db=db_settings['db'], user=db_settings['user'], passwd=db_settings['passwd'], ping=7, maxcached=maxcached, maxconnections=maxconnections)
    return dbpool