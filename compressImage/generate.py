# -*- coding: utf-8 -*-
from PIL import Image
import os
from compress.common import constConfig,ImageExtendName
import logging
import datetime

def log():
    fileName = "log/"+ datetime.date.today().__str__() + "monitor.log"
    path = os.path.join(os.getcwd(),fileName)
    logging.basicConfig(level=logging.INFO,filename=path,format='%(levelname)s:%(message)s %(asctime)s',datefmt='%Y/%d/%m %I:%M:%S %p')

def generateAdImage():
    dirAndFiles = os.listdir(constConfig.adPathResource)
    for fileName in dirAndFiles:
        resourceImageFileName = constConfig.adPathResource+os.sep+fileName    # resource image file path name
        if(os.path.isfile(resourceImageFileName)):
            if(ImageExtendName.isExtendName(os.path.splitext(fileName)[1])):
                generateFileName = os.path.join(constConfig.adPathTarget,fileName+constConfig.imageExtentName)
                if(os.path.isfile(generateFileName) is False):
                    logging.info(generateFileName)
                    im = Image.open(resourceImageFileName)
                    im.save(generateFileName,constConfig.imageFormat,quality = constConfig.imageQuality)

def multiGenerateImage(dirPath):
    dirAndFiles = os.listdir(dirPath)
    for fileName in dirAndFiles:
        realFileName = os.path.join(dirPath,fileName)
        if(os.path.isfile(realFileName)):
            if(ImageExtendName.isExtendName(os.path.splitext(fileName)[1])):
                generateFileName = realFileName + constConfig.imageExtentName
                if(os.path.isfile(generateFileName) is False):
                    logging.info(generateFileName)
                    im = Image.open(realFileName)
                    im.save(generateFileName,constConfig.imageFormat, quality = constConfig.imageQuality)
        elif(os.path.isdir(realFileName)):
            multiGenerateImage(realFileName)




if __name__ == "__main__":
    log()   # open log
    try:
        generateAdImage()   # generate ad image webp format
        multiGenerateImage(constConfig.goodsImagePath) # generate image webp format
    except Exception,e:
        print(e)
        logging.info(e)
