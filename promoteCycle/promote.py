import datetime
import time
from MySQLdb.connections import Connection
from MySQLdb.cursors import DictCursor

def timeUnix():
    return int(time.time())

if __name__ == '__main__' :
    connect = Connection(host='192.168.1.2',user='newxlj',passwd='5OpqU7zv324a7KJxu@4d',db='xiaolajiao',port=3306,charset='utf8')
    cursor = connect.cursor(cursorclass=DictCursor)
    cursor.execute(""" select * from shouji_goods WHERE is_promote = 1 AND promote_cycle>0 """)
    rows = cursor.fetchall()
    for goods in rows:
        # print(datetime.datetime.fromtimestamp(goods.get('promote_end_date')).strftime('%Y-%m-%d %H:%M:%S'))
        if(goods.get('promote_end_date')<=timeUnix()):
            startDate = goods.get('promote_end_date')
            endDate = int(goods.get('promote_end_date')) + int(goods.get('promote_cycle'))*24*3600
            cursor.execute(""" update shouji_goods SET promote_start_date=%s,promote_end_date=%s""" % (startDate,endDate))
    cursor.close()
    connect.close()