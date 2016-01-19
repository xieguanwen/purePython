# -*- coding: utf-8 -*-
import os
import logging
from Path import Path
from ImageExtendName import ImageExtendName
from ImageSize import ImageSize
from GImage import GImage


class GenerateImage(object):
    listProduct = ['/goods_img/','/source_img/','/thumb_img/','upload/','detailedmap/']
    pathPrefix = '/data/www/xiaolajiao8181/images'
    pathMoblePrefix = 'mobileimage'

    def create(self,pathImage):
        logging.info(pathImage)
        if os.path.exists(pathImage) == False: #如果不存在目录退出
            return 1

        path = Path(pathImage,self.pathPrefix) #path对象

        if path.batchIsExist(self.listProduct) == False:
            return 2

        gImage = GImage()
        imageExtendName = path.getImageExtend() #图片路径对象
        imageExtend = ImageExtendName(imageExtendName) #图片扩展对象
        imageSize = ImageSize(self.listProduct,path.getNoPrefixPath()) #图片大小

        try:
            targetPath = path.getTargetPath(self.pathMoblePrefix)
            logging.info(targetPath)
            gImage.generateImage(pathImage, targetPath, imageSize.getSize(), imageExtend.formatImageExtendName())
        except Exception,e:
            logging.error(e.__str__())
            return 3