
import os
import sqlite3
from sqlite3 import Error

''' Aldenir luiz| 22/07/2022
    Prezado Contribuidor, por favor nao remover funcos nao utilizadas!
    todas as ferramentas serao implementadas nas screens 
    posteriormente quando as mesmas forem criadas, desde ja agradecemos.'''

class Diretorio:
    """ |retDirApp>retorna o caminho absoluto da pasta de execucao do script<|retDirApp|
        |retListApp>cria um log com os dados detalhados do diretorio atual<|retListApp|
        |retListApp retorna o nome do arquivo .log criado<|"""
    @staticmethod
    def retDirApp( ) -> str :
        dados = str( os.path.dirname( __file__ ) )
        return dados
    @staticmethod
    def retListApp( ) -> str :
        dirName = str( 'dirLog.log' )
        os.system( f'python --version >{dirName} & dir >>{ dirName }' )
        return dirName


class BancoDados:
    def __init__( self, banco ) -> None:
        ### obtendo o caminho de execucao do script ###
        self.execDir = str( Diretorio.retDirApp( ) )
        ### obtendo o caminho do log do diretorio ###
        self.logDir = str( Diretorio.retListApp( ) )
        ### obtendo o nome do banco de dados solicitado ###
        self.nomeBanco = banco
        self.bancoDados = sqlite3.connect( f'{ self.execDir }\\{ self.nomeBanco }.db', )
        self.bancoDados.row_factory = sqlite3.Row # <-|todas as requisicoes serao retornadas como dict()|
        self.cursor = self.bancoDados.cursor( )
    
           
    ####FUNCAO RESPONSAVEL POR GRAVAR OS DADOS NO BANCO DE DADOS#### #IMPLEMENTADA!#
    def inserirDados( self,nomeTabela, **kwargs ) -> str:
        '''obs: O argumento (dados) deve conter um dicionario com dados validos para o banco de dados. 
        EX: {Nome: Aldenir, Idade: 22, Sexo: Masculino}'''
        
        try: 
            # As colunas a serem criadas tem como base as chaves do dicionario passado
            self.cursor.execute( f"CREATE TABLE { nomeTabela } { tuple( kwargs.keys( ) ) }")
            # Os valores a serem gravados tem como base os values do dicionario passado
            self.cursor.execute( f'INSERT INTO { nomeTabela } VALUES{ tuple( kwargs.values( ) ) }' )
            # Usando o cursor, commit é obrigatorio para confirmar as alteracoes.
            self.bancoDados.commit( )
            # o return é uma string apenas para confirmar que as alteracoes foram feitas
            return 'Os Dados Foram Inseridos'
        except Error as erro: # tratamento em caso de erros nos dados, como uma tabela ja existente. 
            print(erro)
            # retorna uma string alertando que as alteracoes nao foram feitas, a descricao do erro vai anexada.
            return f'Erro! Os Dados Nao Foram Inseridos\n{ erro }'


    #### ESTA FUNCAO E RESPONSAVEL PELAS CONSULTAS AO BANCO DE DADOS #### #NAO IMPLEMENTADA NA GUI!#
    def pegarDados( self, nomeTabela, dado=None ):
        try:
            # selecionando a tabela requisitada, caso exista.
            tables = self.cursor.execute( f"SELECT '{ nomeTabela }' FROM sqlite_master" ).fetchall( )
            # condicao que verifica se o BD esta vazio
            if str( tables ) == '[]':
                return { "erro":'Banco de Dados Vazio!' }
            if dado: # se o argumento dado for passado, uma busca e executada
                self.consultaDados( nomeTabela, dado )
                retData = self.cursor.execute( f"SELECT * FROM { nomeTabela } where { dado }" )
                return retData.fetchall()
            else: # se o argumento dado nao for passado, uma busca geral e executada
                retData = self.cursor.execute( f"SELECT * FROM '{ nomeTabela }'" )
                return retData.fetchall()
        except Error as erro: # em caso de erro, a funcao nao continua.
            print(erro)
            # retorna uma string alertando que aconsulta nao pode ser feita, a descricao do erro vai anexada.
            return f'Erro! Os Dados Nao Foram Inseridos\n{ erro }'


    # ESTA FUNCAO DEVE SER USADA APENAS PELA CLASS DO BANCO E DEVE SER USADA COM CUIDADO! #NAO IMPLEMENTADA NA GUI!#
    def apagarBanco( self, nomeTabela ): 
        self.cursor.execute( f"DELETE FROM { nomeTabela }" )
        self.bancoDados.commit( )

    # ESTA FUNCAO DEVE SER USADA APENAS PELA CLASS DO BANCO! #NAO IMPLEMENTADA NA GUI!#
    def apagarDados( self, nomeTabela, dados ):
        self.cursor.execute( f"DELETE from { nomeTabela } where { dados }" )
        self.bancoDados.commit( )
        print( 'dados apagados' )

    # A FUNCAO DE CONSULTA DE SER USADA APENAS PELA CLASS DO BANCO! #NAO IMPLEMENTADA NA GUI!#
    def consultaDados( self, nomeTabela, dados=None ):
        #print( f'Banco: {self.nomeBanco}\nTabela: {nomeTabela}')
        try:
            tables = self.cursor.execute( f"SELECT '{ nomeTabela }' FROM sqlite_master" )
            mapper = [x for x in map(dict, tables.fetchall())]
            if nomeTabela in str(mapper ):
                if dados:
                    retData = self.cursor.execute( f"SELECT * FROM { nomeTabela } where { dados }" )
                    if len( retData.fetchall() ) == 0:
                        return False
                    else:
                        return True
            else: 
                return 'SFalse'
        except sqlite3.OperationalError:
            return False
    
    
    
class Gerente( BancoDados ):
    def __init__( self, **kwargs ) -> None:
        ### obtendo o caminho de execucao do script ###
        self.execDir = str( Diretorio.retDirApp( ) )
        ### obtendo o caminho do log do diretorio ###
        self.logDir = str( Diretorio.retListApp( ) )
        self.nomeBanco = str( kwargs.get( 'banco' ) )
        self.banco = BancoDados( self.nomeBanco )
       

    #### ESTA FUNCAO DEVE SER CAPAZ DE GERNCIAR TODAS AS REQUISICOES FEITAS AO BAQNCO DE DADOS ####
    def gerente(self, **kwargs):
        dados = kwargs.get('dados')
        query = kwargs.get('query')
        
        # A tabela sera nomeada com base em ( nome e data ) vindo dos dados.
        tabela = f"{dados['nome da rota:']}{dados['data da rota:']}"
        if query == 'add':
            if self.verBanco( self.nomeBanco ):# verificando se o banco de dados foi criado.
                if self.verTabela( tabela ): # Verificando se a tabela ja existe.
                    print( f'A Tabela { self.nomeTabela } ja existe no banco de dados: { self.nomeBanco }' )
                else:
                    if self.banco.inserirDados( tabela, **dados) == 'Os Dados Foram Inseridos':
                        print('dados inseridos')
                    else:
                        print('erro! os dados ja estao no banco de dados!')
                    
                    
    ### CONSULTOR BANCO DE DADOS##              
    def verBanco(self, nomebanco) -> bool:
        with open(f'{ self.execDir }\\{ str( self.logDir ) }', 'r' ) as caminho:
            logLines = caminho.readlines( ) #<- representacao das linhas do arquivo .log
            #<- percorrendo linhas no log
            if f'{ nomebanco }.db' in str( logLines ): # condicao verifica se ha um arquivo com nome do banco de dados
                print( 'banco existe' ) # <-|exibe no terminal o estado do bancocomo existente|
                return True
            else:
                print( 'banco inexistente' ) # <-|exibe no terminal o estado do bancocomo inexistente|
                return False
                
    
    ### CONSULTOR TABELA###         
    def verTabela( self, nometabela ) -> bool:
        if self.banco.consultaDados( nometabela ):
            return True
        else:
            return False
        
    def extractTables(self):
        for key in BancoDados:
            pass


######## MANTER ESTAS LINHAs COMO TEST DRIVER DO BANCO ########
dataTest = {'Nome': 'Aldenir', 'Idade': 22, 'Sexo': 'Masculino'}
teste = BancoDados( 'teste' )
teste.inserirDados('Teste', **dataTest)
#teste.apagarBanco("Vendedores")
#teste.apagarDados("Vendedores", "Nome='Aldenir'")
retorno = teste.pegarDados('Teste', dado="Nome='Aldenir'")
print( dict(retorno[0]) )
print( teste.consultaDados( 'Teste', dados="Nome='Aldenir'" ) )
"""for dado in teste.pegarDados('Vendedores'):
    try:
        for key, value in dict(dado).items():
            print(f'|\t{key}\t: {value}')
    except ValueError as erro:
        print(dado)
        print(erro)"""
