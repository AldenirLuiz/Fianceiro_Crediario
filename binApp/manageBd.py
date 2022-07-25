from posixpath import abspath
from manageQuery import BancoDados
import manageDir


class Gerente():
    
    def __init__( self, **kwargs ) -> None:
        self._diretorio = manageDir.Diretorio
        self._logger = manageDir.Logger
        ### obtendo o caminho de execucao do script ###
        self.execDir = f"{self._diretorio.retDirApp( )}"
        ### obtendo o caminho do log do diretorio ###
        self.logDir = f"{self._logger.retListApp( )}"
        ### obtendo o caminho do Banco ###
        self.nomeBanco = f"{kwargs.get( 'banco' )}"
        self.absPathBd = self.verBanco(self.nomeBanco)
        print(f'Caminho: {self.absPathBd}')
        self.banco = BancoDados(self.absPathBd)
       
    #### ESTA FUNCAO DEVE SER CAPAZ DE GERNCIAR TODAS AS REQUISICOES FEITAS AO BAQNCO DE DADOS ####
    def gerenteBd(self, **kwargs):
        dados = kwargs.get('dados')
        query = kwargs.get('query')
        
        # A tabela sera nomeada com base em ( nome e data ) vindo dos dados.
        tabela = f"{dados['nome da rota:']}{dados['data da rota:']}"
        if query == 'add':
            if self.verTabela( tabela ): # Verificando se a tabela ja existe.
                return f'A Tabela { tabela } ja existe no banco de dados: { self.nomeBanco }'
            else:
                if self.banco.inserirDados( tabela, **dados) == 'Os Dados Foram Inseridos':
                    return 'dados inseridos'
                else:
                    return 'erro! os dados ja estao no banco de dados!'
                    
                    
    ### CONSULTOR BANCO DE DADOS##              
    def verBanco(self, nomebanco) -> bool:
        try:
            #print('banco: ',nomebanco)
            absPathBd = manageDir.Diretorio.retWayApp(nomebanco)
            if abspath:
                print(absPathBd)
                return absPathBd
            else:
                absPathBd = manageDir.Diretorio.retWayApp('dataBase')
                BancoDados(f"{absPathBd}\\{nomebanco}")
                
                print("create", absPathBd)
                return absPathBd
        except:
            print('Bd nao encontrado')
            pass
                
    
    ### CONSULTOR TABELA###         
    def verTabela( self, nometabela ) -> bool:
        if self.banco.consultaDados( nometabela ):
            return True
        else:
            return False
    
    def loger(self):
        try:
            absPathLog = manageDir.Diretorio.retWayApp('dirlog.log')
        except:
            pass
    