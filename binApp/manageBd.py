from binApp.manageQuery import BancoDados
from binApp import manageDir


class Gerente():
    
    def __init__( self, **kwargs ) -> None:
        ### definindo o gerenciador de diretorios ###
        self._diretorio = manageDir.Diretorio
        ### definindo o log de pasta ###
        self._logger = manageDir.Logger
        ### obtendo o caminho do log do diretorio ###
        self.logDir = f"{self._logger.retListApp( )}"
        ### obtendo o nome do Banco ###
        self.nomeBanco = f"{kwargs.get( 'banco' )}"
        ### verificando banco de dados ###
        self.absPathBd = self.verBanco(self.nomeBanco)
        ### definindo banco de dados ###
        self.banco = BancoDados(self.absPathBd)
       
    #### ESTA FUNCAO DEVE SER CAPAZ DE GERNCIAR TODAS AS REQUISICOES FEITAS AO BANCO DE DADOS ####
    def gerenteBd(self, **kwargs):
        ### recuperando dados da requisicao ###
        dados = kwargs.get('dados')
        query = kwargs.get('query') # Tipo de requisicao.
        # A tabela sera nomeada com base em ( nome e data ) vindo dos dados.
        tabela = f"{dados['nome da rota:']}{dados['data da rota:']}"
        if query == 'add': # se o tipo da query for adicionar.
            if self.verTabela( tabela ): # Verificando se a tabela ja existe.
                return f'A Tabela { tabela } ja existe no banco de dados: { self.nomeBanco }'
            else: # atende ao caso da tabela nao estar no banco de dados.
                statusQuery = self.banco.inserirDados( tabela, **dados)
                if statusQuery == 'Os Dados Foram Inseridos':
                    return 'dados inseridos' # retorno de operacao bem suscedida
                else: # retorno de operacao mal suscedida
                    return f'ERRO DE OPERACAO! \n{statusQuery}'
                    
    ### CONSULTOR BANCO DE DADOS##              
    def verBanco(self, nomebanco) -> bool:
        try: # buscando no gerenciador de diretorios pelo banco de dados.
            absPathBd = manageDir.Diretorio.retWayApp(file=nomebanco, path='dataBase')
            if absPathBd: # 
                return absPathBd
            else:
                raise 'ERRO!! Nao foi Possivel Criar um Banco de dados'
        except:
            print('Bd nao encontrado')
            pass
                
    ### CONSULTOR TABELA###         
    def verTabela( self, nometabela ) -> bool:
        if self.banco.consultaDados( nometabela ):
            return True
        else:
            return False
    