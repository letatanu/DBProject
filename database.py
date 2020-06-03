from psycopg2 import pool

# connection_pool = pool.SimpleConnectionPool(1,
#                                             10,
#                                             user='letanu',
#                                             password='1',
#                                             database='learning',
#                                             host='localhost')
password = 'h36*vfvZpj' # your password here
userName = 'spr2020adb49' # your username here
connection_pool = pool.SimpleConnectionPool(1,
                                            10,
                                            user=userName,
                                            password=password,
                                            database='spr2020adb49',
                                            host='dbclass.cs.pdx.edu')


class CursorConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection  = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)