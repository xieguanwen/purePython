# -*- coding: utf-8 -*-
'''
create time 2016-6-12
@author rich
'''
import os

class ConstError(Exception):
    pass

class Const(object):
    def __init__(self):
        self.adPathResource = '/data/www/xiaolajiao8181/data/afficheimg'
        self.adPathTarget = '/data/www/xiaolajiao8181/data/afficheimg/webp'
        self.goodsImagePath = '/data/www/xiaolajiao8181/images'
        self.thumb_img = (300,300)
        self.source_img = (800,800)
        self.goods_img = (480,480)
        self.maxProductWidth = 1000
        self.imageQuality = 70
        self.imageFormat = "WEBP"
        self.imageExtentName = ".webp"

    def __setattr__(self, k, v):
        if k in self.__dict__:
            raise ConstError
        else:
            self.__dict__[k] = v

class ImageExtendName(object):
    '''
    classdocs
    '''
    __discImageExtendName = {'.png':'PNG','.jpg':'JPEG','.gif':'GIF'}

    @staticmethod
    def isExtendName(extendName):
        return ImageExtendName.__discImageExtendName.has_key(extendName)

constConfig = Const()