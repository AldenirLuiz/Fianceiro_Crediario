import os


class Diretorio:
    """|retDirApp>retorna o caminho absoluto da pasta de execucao do script<|retDirApp|"""
    def retWayApp(file=None, path=None ) -> str:
        mainPath = "./"
        for diretorio, subpastas, arquivos in os.walk(mainPath):
            for arquivo in arquivos:
                temp = f"{os.path.join(os.path.realpath(diretorio), arquivo)}"
                if str(file) in temp:
                    return temp
                else: continue
            else: return f"{os.path.join(os.path.realpath(diretorio))}\\{path}\\{file}"
        else: return False


    def __str__(self) -> str:
        return os.path.dirname( f"{__file__}" )
            
    
class Logger:
    '''|retListApp>cria um log com os dados detalhados do diretorio atual e o retorna<|retListApp|'''
    global dirName
    dirName = "dirLog.log"
    
    def retListApp(self) -> str :
        os.system( f"python --version >{Diretorio.retWayApp(file=dirName, path='logDir')} & dir >>{Diretorio.retWayApp(file=dirName,path='logDir')}" )
        logWay = Diretorio.retWayApp(file=dirName, path='logDir')
        return logWay
    
    def retTextApp(self) -> str:
        logWay = Diretorio.retWayApp(file=dirName, path='logDir')
        retText = os.system( f"type {Diretorio.retWayApp(file=dirName, path='logDir')}" )
        return retText


    def __str__(self) -> str:
        return self.retListApp()


if __name__ == "__main__":
    log = Logger()
    print(f"Resultado: {log}")
