import MySQLdb
from MySQLdb.cursors import DictCursor

class ConfigDb(object):

    def __init__(self):
        self.host="192.168.1.219"
        self.user="xiaolajiao"
        self.passwd="xiaolajiao"
        self.db="xiaolajiao"
        self.port=3306
        self.charset="utf8"

class DbMysql(object):

    cursor = None
    conn = None

    def __init__(self,cursorclass=DictCursor):
        kwargs = ConfigDb().__dict__
        self.conn = MySQLdb.connect(**kwargs)
        self.cursor = self.conn.cursor(cursorclass=cursorclass)

    def __delete__(self, instance):
        self.cursor.close()
        self.conn.close()