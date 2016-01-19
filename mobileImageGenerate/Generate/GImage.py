# -*- coding: utf-8 -*-
'''
Created on 2014年6月12日

@author: Rich
'''
import os
from PIL import Image

class GImage(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def generateImage(self,sourcePath,targetPath,size,formatImage):
        im = Image.open(sourcePath)
        if im.size[0]<size[0]:
            size = im.size       
        im.thumbnail(size)
        if os.path.exists(os.path.dirname(targetPath)) == False :
            os.makedirs(os.path.dirname(targetPath))
        im.save(targetPath,formatImage,quality = 60)