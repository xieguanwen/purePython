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
        db.cursor.execute(""" select id from shouji_send_sms WHERE order_sn=%s""",[row['order_sn']])
        smsRow = db.cursor.fetchone()
        if(smsRow is None):
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
                # print(resp['alibaba_aliqin_fc_sms_num_send_response']['result']['err_code'])
                if(resp['alibaba_aliqin_fc_sms_num_send_response']['result']['err_code'] == '0'):
                    db.cursor.execute(""" INSERT INTO shouji_send_sms(send_type,user_id,mobile,order_sn,add_time,status) VALUES(%s,%s,%s,%s,%s,%s) """,[3,row['user_id'],row['mobile'],row['order_sn'],datetime.datetime.now(),1])
            except Exception,e:
                print(e)