# -*- coding: utf-8 -*-
'''
Created on 2014年6月12日

@author: Rich
'''

class ImageExtendName(object):
    '''
    classdocs
    '''
    __extendName = ''
    __discImageExtendName = {'png':'PNG','jpg':'JPEG','gif':'GIF'}

    def __init__(self,extendName):
        '''
        Constructor
        '''
        self.__extendName = extendName
    
    def formatImageExtendName(self):
        return self.__discImageExtendName.get(self.__extendName)