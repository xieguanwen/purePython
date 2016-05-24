# -*- coding: utf-8 -*-
import top.api
import datetime,time
import json
from config import AliyunConfig
from db.db import DbMysql
import sys
reload(sys)
sys.setdefaultencoding('utf8')

if(__name__== "__main__"):
    db = DbMysql()
    nowTimestamp = int(time.mktime(datetime.datetime.now().timetuple()))
    nowTimestamp = nowTimestamp - 10*60

    db.cursor.execute(""" select * from shouji_order_info WHERE order_status = 0 AND pay_status=0 AND add_time>=%s""",[nowTimestamp])
    rows = db.cursor.fetchall()

    for row in rows:
        if(row):
            req=top.api.AlibabaAliqinFcSmsNumSendRequest()
            req.set_app_info(top.appinfo(AliyunConfig.appkey,AliyunConfig.secret))

            # req.extend="123456"
            req.sms_type="normal"
            req.sms_free_sign_name="小辣椒"
            req.sms_param=json.dumps({"name":row['consignee']})
            req.rec_num=row['mobile']
            req.sms_template_code="SMS_9651659"
            try:
                resp = req.getResponse()
            except Exception,e:
                print(e)