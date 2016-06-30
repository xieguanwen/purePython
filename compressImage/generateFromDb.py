# -*- coding: utf-8 -*-
from db.db import DbMysql
from compress.common import constConfig,ImageExtendName
from compress.log import MyLog
import datetime,time
import os
import logging
from PIL import Image

def ad(timestamp):
    sql = """ select ad_id,ad_code from shouji_ad WHERE end_time>=%s """ %timestamp
    db = DbMysql()
    db.cursor.execute(sql)
    rows = db.cursor.fetchall()
    for row in rows:
        realPath = os.path.join(constConfig.adPathResource,row['ad_code'])
        if(os.path.isfile(realPath)):
            if(ImageExtendName.isExtendName(os.path.splitext(row['ad_code'])[1])):
                im = Image.open(realPath)
                generateFileName = os.path.join(constConfig.adPathTarget,row['ad_code'] + constConfig.imageExtentName)
                logging.info(generateFileName)
                im.save(generateFileName,constConfig.imageFormat,quality = constConfig.imageQuality)

def goods(timestamp):
    sql = """ select * from shouji_goods WHERE last_update=%s """ %timestamp


if __name__ == "__main__":
    MyLog.log(fileName="db.log")
    timestamp = int(time.mktime(datetime.datetime.now().timetuple()))
    ad(timestamp)
