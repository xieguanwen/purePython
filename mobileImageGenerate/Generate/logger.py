
import logging
import os

def test():
    logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.WARN, filemode = 'w', format = '%(asctime)s - %(levelname)s: %(message)s')  
    logging.debug('debug')  #被忽略  
    logging.info('info')    #被忽略  
    logging.warning('warn')  
    logging.error('error')  