import datetime,time

nowTimestamp = int(time.mktime(datetime.datetime.now().timetuple()))
nowTimestamp = nowTimestamp - 100000*60

print(nowTimestamp)