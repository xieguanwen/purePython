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

class Db(object):

    cursor = None
    conn = None

    def __init__(self,cursorclass=None):
        kwargs = ConfigDb().__dict__
        self.conn = MySQLdb.connect(**kwargs)
        self.cursor = self.conn.cursor(cursorclass=cursorclass)



# conn = MySQLdb.connect(host="192.168.1.219",user="xiaolajiao",passwd="xiaolajiao",db="xiaolajiao",port=3306,charset="utf8")
# cursor = conn.cursor(cursorclass=DictCursor)
# print(cursor)

if __name__ == "__main__":
    db = Db(DictCursor)
    db.cursor.execute(""" select * from shouji_order_info limit 0,1 """)
    print(db.cursor.fetchone())
