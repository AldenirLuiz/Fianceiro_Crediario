from binApp.manageDir import Diretorio
import sys, os
import logging


class Logger:
    __DIRNAME__ = Diretorio()
    dir_name = "dirLog.log"

    log_path = __DIRNAME__.retWayPath(_path="logDir", _file="log.inf")
    logging.basicConfig(filename=log_path, level=logging.INFO)

    def retListApp(_error:str=None):
        if _error:
            logging.info("Python version: {}".format(sys.version))
            logging.info(_error)
        else:
            logging.info("Python version: {}".format(sys.version))
            logging.info("Current directory contents: {}".format(os.listdir(".")))
        
    def retTextApp():
        temp_text = ''
        with open(logging.getLogger().handlers[0].baseFilename, "r") as text_read:
            for line in text_read:
                temp_text += line
            return temp_text
    
    def __str__(self):
        return self.retTextApp()