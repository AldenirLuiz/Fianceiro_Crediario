
import os
import sqlite3
from sqlite3 import Error


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
        os.system( f'dir >>{ dirName }' )
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
    

    def criarTabela( self, nomeTabela):
        '''obs: O argumento (dados) deve conter dados validos para o banco de dados. 
        EX: nomeRota text, dataRota, text, dataRetorno, text, quantidade, integer'''
        try:
            self.cursor.execute( f'CREATE TABLE { nomeTabela }' )
            self.bancoDados.commit()
        except sqlite3.OperationalError as erro:
            return erro

    def inserirDados( self, nomeTabela, dados ):
        '''obs: O argumento (dados) deve conter um dicionario com dados validos para o banco de dados. 
        EX: {Nome: Aldenir, Idade: 22, Sexo: Masculino}'''
        
        self.cursor.execute( f'INSERT INTO { nomeTabela } VALUES{ tuple( dados.values( ) ) }' )
        self.bancoDados.commit( )
        return 'Os Dados Foram Inseridos'

    def pegarDados( self, nomeTabela, dado=None ):
        tables = self.cursor.execute( f"SELECT '{ nomeTabela }' FROM sqlite_master" )
        
        if nomeTabela in str( dict( tables.fetchall( ) ) ):
            print( 'Tabela existe' )
        else: 
            return { 'erro': 'Tabela inexistente!' }

        if dado:
            self.consultaDados( nomeTabela, dado )
        else:
            self.cursor.execute( f"SELECT * FROM '{ nomeTabela }'" )
            if str( self.cursor.fetchall( ) ) == '[]':
                return { "erro":'Banco de Dados Vazio!' }
            else:
                self.cursor.execute( f"SELECT * FROM '{ nomeTabela }'" )
                return list( x for x in self.cursor.fetchall( ) )

    # ESTA FUNCAO DEVE SER USADA APENAS PELA CLASS DO BANCO E DEVE SER USADA COM CUIDADO!
    def apagarBanco( self, nomeTabela ): 
        self.cursor.execute( f"DELETE FROM { nomeTabela }" )
        self.bancoDados.commit( )

    # ESTA FUNCAO DEVE SER USADA APENAS PELA CLASS DO BANCO!
    def apagarDados( self, nomeTabela, dados ):
        self.cursor.execute( f"DELETE from { nomeTabela } where { dados }" )
        self.bancoDados.commit( )
        print( 'dados apagados' )

    # A FUNCAO DE CONSULTA DE SER USADA APENAS PELA CLASS DO BANCO!
    def consultaDados( self, nomeTabela, dados=None ):
        print( f'Banco: {self.nomeBanco}\nTabela: {nomeTabela}')
        tables = self.cursor.execute( f"SELECT '{ nomeTabela }' FROM sqlite_master" )
        print(tables.fetchall())
        rTables = dict( tables.fetchall( ) )
        #print( rTables, nomeTabela )
        
        if nomeTabela in str( rTables ):
            print( 'Tabela existe' )
            if dados:
                self.cursor.execute( f"SELECT * FROM { nomeTabela } where { dados }" )
            if len( self.cursor.fetchall( ) ) == 0:
                False
            else:
                return True
        else: 
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
    def gerente( self, **kwargs ):

        self.nomeTabela = kwargs.get( 'tabela' ) # <-|representacao da tabela a ser processada/criada|
        self.dadosEntrada = kwargs.get( 'dados' ) # <-|representacao dos dados de entrada a serem processados|
        self.tipoQuery = kwargs.get( 'query' ) # <-|representacao do tipo da solicitacao|
        
        ## Verificacao de dados, evita criar dados duplicados ##
        if self.verBanco( self.nomeBanco ):# verificando se o banco de dados foi criado.
            if self.verTabela( self.nomeTabela ): # Verificando se a tabela ja existe.
                print( f'A Tabela { self.nomeTabela } ja existe no banco de dados: { self.nomeBanco }' )
            else:
                self.banco.criarTabela( self.nomeTabela )
                if self.banco.inserirDados( self.nomeTabela, self.dadosEntrada, ) == 'Os Dados Foram Inseridos':
                    print('dados inseridos')
                else:
                    print('erro! os dados ja estao no banco de dados!')
                
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
                
                
    def verTabela( self, nometabela ) -> bool:
        if self.banco.consultaDados( nometabela ):
            return True
        else:
            return False


######## MANTER ESTAS LINHA COMO TEST DRIVER DO BANCO ########
#teste = BancoDados( 'teste' )
#print( teste.consultaDados( 'Vendedores' ) )
#teste.criarTabela('Vendedores', "'Nome', 'Idade', 'Sexo'")
#print((teste.mapper("Vendedores", {'Nome':'Aldenir', 'Idade':28, 'Sexo':'Masculino'})))
#teste.apagarBanco("Vendedores")
#teste.apagarDados("Vendedores", "Nome='Aldenir'")
#print(teste.pegarDados('Vendedores', dado="Nome='Aldenir'"))
#for dado in teste.pegarDados('Vendedores'):
#    try:
#        for key, value in dict(dado).items():
#            print(f'|\t{key}\t: {value}')
#    except ValueError as erro:
#        print(dado)
#        print(erro)


"""for x in self.pegarDados( nomeTabela ):
                    try:
                        if str( dados ) in str( dict( x ) ):
                            return False
                        else: continue
                    except ValueError:
                        return True
                    else: return True
            else: return True"""