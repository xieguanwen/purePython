# -*- coding: utf-8 -*-
'''
Created on 2014年6月12日

@author: Rich
'''

class ImageSize(object):
    '''
    classdocs @todo 还没有做好
    '''
    __listProductSize = {'goods_img':(480,480),'source_img':(800,800),'thumb_img':(300,300),'upload':(720,10000),'detailedmap':(720,10000)}
    __listProduct = None
    __pathName = ''
    
    def __init__(self,listProduct,pathName):
        '''
        Constructor
        '''
        self.__listProduct = listProduct
        self.__pathName = pathName
    
    def getSize(self):
        size=(0,0)
        for productPath in self.__listProduct:
            if self.__pathName.find(productPath) != -1:
                size = self.__listProductSize.get(productPath.strip('/'))
                break
        return size
            