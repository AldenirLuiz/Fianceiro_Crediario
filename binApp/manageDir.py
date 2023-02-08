import os
import sys
import logging

app_root_dir = os.path.dirname(os.path.dirname(f"{__file__}"))

class Diretorio:
    
    def retWayPath(self, _path):
        if not os.path.exists(f'{app_root_dir}/{_path}'):
            self.createDir(app_root_dir, _path)

        return os.path.join(f"{app_root_dir}\\{_path}")
        
    
    def createDir(self, _s_dir, _c_dir):
        try:
            os.makedirs(_c_dir)
        except OSError as _erro:
            print(
                f'''
                    Um erro ocoreu ao tentar criar o diretorio: {_c_dir} 
                    No destino: {_s_dir}
                    ERRO: {_erro}
                '''
            )

            
    def __str__(self) -> str:
        return app_root_dir
    
    class ErrDir(Exception):
        pass




class Logger:
    def __init__(self, dir_name="dirLog.log"):
        self.dir_name = dir_name

        log_path = Diretorio().retWayApp(file=self.dir_name, _path="logDir")
        logging.basicConfig(filename=log_path, level=logging.INFO)

    def retListApp(self):
        logging.info("Python version: {}".format(sys.version))
        logging.info("Current directory contents: {}".format(os.listdir(".")))
        
    def retTextApp(self):
        temp_text = ''
        with open(logging.getLogger().handlers[0].baseFilename, "r") as text_read:
            for line in text_read:
                temp_text += line
            return temp_text
    
    def __str__(self):
        return self.retTextApp()


if __name__ == "__main__":
    log = Diretorio()
    print(f"Resultado: {log.retWayFile(file='dadosCobranca.db')}")
