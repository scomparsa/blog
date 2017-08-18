import itertools
import functools
from oursql import OperationalError
from definition import COUNTPERPAGE

def ensure_close(method):
    @functools.wraps(method)
    def wrapper(self, *args, **argkw):
        self.conn = self.pool.connection()
        try:
            res = method(self, *args, **argkw)
        except OperationalError, error:
            # OperationalError: (2006, 'MySQL server has gone away', None) 
            # OperationalError: (2013, 'Lost connection to MySQL server during query', None) 
            res = method(self, *args, **argkw)
        except Exception, error:
            raise error
        finally:
            self.conn.close()
        return res
    return wrapper 

class DBProxy:
    """ pool connection """
 
    def __init__(self, pool):
        self.countperpage = COUNTPERPAGE
        self.pool = pool
        self.create_table()

    def create_table(self):
        pass

    @property
    def tablename(self):
        return None
    
    @ensure_close
    def query(self, query, *parameters):
        """Returns a row list for the given query and parameters."""
        cursor = self.conn.cursor()
        query = query % (self.tablename,)
        cursor.execute(query, parameters)
        values = cursor.fetchall()
        column_names = [d[0] for d in cursor.description]
        cursor.close()
        return [Row(itertools.izip(column_names, value)) for value in values]

    @ensure_close
    def get(self, query, *parameters):
        """Returns the first row returned for the given query."""
        rows = self.query(query, *parameters)
        if not rows:
            return None
        elif len(rows) > 1:
            raise Exception("Multiple rows returned for Database.get() query")
        else:
            return rows[0]

    @ensure_close
    def execute(self, query, *parameters):
        """Executes the given query, returning the lastrowid from the query."""
        cursor = self.conn.cursor()
        query = query % (self.tablename,)
        cursor.execute(query, parameters)
        cursor.close()
        self.conn.commit()
        
class Row(dict):
    """A dict that allows for object-like property access syntax."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)
