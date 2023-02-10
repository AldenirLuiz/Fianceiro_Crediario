import os

app_root_dir = os.path.dirname(os.path.dirname(f"{__file__}"))

class Diretorio:
    
    def retWayPath(self, _path:str, _file:str=None):

        if _file and os.path.exists(f'{app_root_dir}/{_path}/{_file}'):
            return os.path.join(f"{app_root_dir}\\{_path}\\{_file}")
        else:
            if not os.path.exists(f'{app_root_dir}/{_path}'):
                self.createDir(app_root_dir, _path)
                return os.path.join(f"{app_root_dir}\\{_path}")
    
    def createDir(self, _s_dir, _c_dir):
        try:os.makedirs(_c_dir)
        except OSError as _erro:
            err_messgae = f'''Um erro ocoreu ao tentar criar o diretorio: {_c_dir} 
                    No destino: {_s_dir}
                    ERRO: {_erro}'''
            self.ErrDir(err_messgae)
            

    def __str__(self) -> str:
        return app_root_dir
    
    class ErrDir(Exception):
        pass


if __name__ == "__main__":
    pass
    
    #print(f"Resultado: {retListApp()}")
