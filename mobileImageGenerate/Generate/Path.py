# -*- coding: utf-8 -*-
'''
Created on 2014年6月11日

@author: Rich
'''
import os

class Path(object):
    '''
    classdocs
    '''
    __pathName = ''
    __prefixPath = ''
    __noPrefixPath = ''

    def __init__(self, pathName,prefixPath):
        '''
        Constructor
        '''
        self.__pathName = pathName
        self.__prefixPath = prefixPath
        self.__noPrefixPath = self.__pathName.replace(self.__prefixPath,'')
        
    def getImageExtend(self):
        return self.__pathName.split('.')[-1]
    
    def getPath(self):
        return self.__pathName.replace(self.__pathName.split(os.sep)[-1],'')
    
    def isExist(self,strPath):
        if(self.__noPrefixPath.find(strPath) != -1 ):
            return True
        else:
            return False
        
    def getTargetPath(self,mobilePath):
        rootPath = os.path.split(self.__prefixPath.rstrip(os.sep))[0]
        pathTarget = rootPath + os.sep + mobilePath + os.sep + self.__noPrefixPath.lstrip(os.sep)
        return pathTarget
    
    def getNoPrefixPath(self):
        return self.__noPrefixPath

    def batchIsExist(self,listProduct):
        boolValue = False
        for productPath in listProduct:
            if(self.__noPrefixPath.find(productPath) != -1 ):
                boolValue = True
                break
        return boolValue
