import os


class Diretorio:
    """|retDirApp>retorna o caminho absoluto da pasta de execucao do script<|retDirApp|"""
    def retDirApp( ) -> str :
        dados = os.path.dirname( f"{__file__}" )
        return dados
    
    def retWayApp( file=None, path=None ) -> str:
        mainPath = "./"
        for diretorio, subpastas, arquivos in os.walk(mainPath):
            for arquivo in arquivos:
                temp = f"{os.path.join(os.path.realpath(diretorio), arquivo)}"
                if str(file) in temp:
                    return temp
                else: continue
            else: return f"{os.path.join(os.path.realpath(diretorio))}\\{path}\\{file}"
        else: return False
            
    
class Logger:
    '''|retListApp>cria um log com os dados detalhados do diretorio atual e o retorna<|retListApp|'''
    global dirName
    dirName = "dirLog.log"
    
    def retListApp( ) -> str :
        logWay = Diretorio.retWayApp(file=dirName, path='logDir')
        os.system( f"python --version >{Diretorio.retWayApp(file=dirName, path='logDir')} & dir >>{Diretorio.retWayApp(file=dirName,path='logDir')}" )
        return logWay
    
    def retTextApp( ):
        logWay = Diretorio.retWayApp(file=dirName, path='logDir')
        retText = os.system( f"type {Diretorio.retWayApp(file=dirName, path='logDir')}" )
        return retText
