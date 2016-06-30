# -*- coding: utf-8 -*-
import logging
import datetime
import os

class MyLog(object):
    @classmethod
    def log(cls,fileName='monitor.log'):
        fileName = "../log/"+ datetime.date.today().__str__() + fileName
        path = os.path.realpath(os.path.join(os.path.dirname(__file__),fileName))
        logging.basicConfig(level=logging.INFO,filename=path,format='%(levelname)s:%(message)s %(asctime)s',datefmt='%Y/%d/%m %I:%M:%S %p')

