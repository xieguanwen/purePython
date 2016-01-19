import pyinotify
import os
import logging
import datetime
from Generate import GenerateImage

class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        pathAndName = os.path.join(event.path,event.name)
        if(os.path.isfile(pathAndName)):
            generateImage = GenerateImage()
            if(generateImage.create(pathAndName)==3):
                logging.info(pathAndName)

def generate(listenPath,logging):
    wm = pyinotify.WatchManager()
    eh = MyEventHandler()
    notifier = pyinotify.Notifier(wm,eh)
    wm.add_watch(listenPath, pyinotify.EventsCodes.FLAG_COLLECTIONS['OP_FLAGS']['IN_CREATE'],auto_add=True,rec=True)
    try:
        notifier.loop()
    except pyinotify.NotifierError, err:
        logging.info(pyinotify.NotifierError.__str__())
        logging.info(err.__str__())

if __name__ == '__main__':
    fileName = "log/"+datetime.date.today().__str__()+"monitor.log"
    path = os.path.join(os.getcwd(),fileName)
    logging.basicConfig(level=logging.INFO,filename=path)
    generate('/data/www/xiaolajiao8181/images',logging)


