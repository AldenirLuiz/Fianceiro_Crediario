import os
from posixpath import dirname


class Diretorio:
    """|retDirApp>retorna o caminho absoluto da pasta de execucao do script<|retDirApp|"""
    def retDirApp( ) -> str :
        dados = os.path.dirname( f"{__file__}" )
        return dados
    
    def retWayApp( file=None ) -> str:
        pasta="./"
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                temp = f"{os.path.join(os.path.realpath(diretorio), arquivo)}"
                if str(file) in temp:
                    return temp
                else: continue
            else: return f"{os.path.join(os.path.realpath(diretorio))}\\dataBase\\{file}"
            
    
class Logger:
    '''|retListApp>cria um log com os dados detalhados do diretorio atual e o retorna<|retListApp|'''
    global dirName
    dirName = "dirLog.log"
    def retListApp( ) -> str :
        os.system( f'python --version >{Diretorio.retWayApp(dirName)} & dir >>{Diretorio.retWayApp(dirName)}' )
        logWay = Diretorio.retWayApp(dirname)
        return logWay
    
    def retTextApp( ):
        os.system( f'type { dirName }' )
        
