
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
    def __init__( self, **kwargs ) -> None:
        
        ### obtendo o caminho de execucao do script ###
        self.execDir = str( Diretorio.retDirApp( ) )
        ### obtendo o caminho do log do diretorio ###
        self.logDir = str( Diretorio.retListApp( ) )

        ### obtendo o nome do banco de dados solicitado ###
        self.nomeBanco = kwargs.get( 'banco' )
        self.bancoDados = sqlite3.connect( f'{ self.execDir }\\{ self.nomeBanco }.db' )
        self.bancoDados.row_factory = sqlite3.Row # <-|todas as requisicoes serao retornadas como dict()|
        self.cursor = self.bancoDados.cursor( )

    #### ESTA FUNCAO DEVE SER CAPAZ DE GERNCIAR TODAS AS REQUISICOES FEITAS AO BAQNCO DE DADOS ####
    def gerente( self, **kwargs ):

        self.dadosEntrada = kwargs.get( 'dados' ) # <-|representacao dos dados de entrada a serem processados|
        print( self.nomeBanco ) # <-|codigo moleta, exibe no terminal os dados a serem gravados|
        print( self.execDir )

        with open(f'{self.execDir}\\{str(self.logDir)}', 'r') as caminho:
            
            logLines = caminho.readlines() #<- representacao das linhas do arquivo .log
            #<- percorrendo linhas no log
            if f'{self.nomeBanco}.db' in str(logLines):
                print( 'banco existe' ) # <-|codigo moleta, exibe no terminal os dados a serem gravados|
            else:
                print( 'banco inexistente' ) # <-|codigo moleta, exibe no terminal os dados a serem gravados|


    def criarTabela(self, nomeTabela,  dados):
        '''obs: O argumento (dados) deve conter dados validos para o banco de dados. 
        EX: nomeRota text, dataRota, text, dataRetorno, text, quantidade, integer'''
        try:
            self.cursor.execute(f'CREATE TABLE {nomeTabela} ({dados})')
            self.bancoDados.commit()
        except sqlite3.OperationalError as erro:
            return erro


    def inserirDados(self, nomeTabela, dados):
        '''obs: O argumento (dados) deve conter um dicionario com dados validos para o banco de dados. 
        EX: {Nome: Aldenir, Idade: 22, Sexo: Masculino}'''
        if self.consultaDados(nomeTabela, dados):
            self.cursor.execute(f'INSERT INTO {nomeTabela} VALUES{tuple(dados.values())}')
            self.bancoDados.commit()
            return 'Os Dados Foram Inseridos'
        else:
            return 'ERRO!! Os Dados Inseridos ja Estao no Banco.'
    

    def pegarDados(self, nomeTabela, dado=None):
        if dado:
            self.cursor.execute(f"SELECT * FROM {nomeTabela} where {dado}")
            if len(self.cursor.fetchall()) == 0:
                return {'erro':'Nenhum dado Corresponde!'}
            else:
                self.cursor.execute(f"SELECT * FROM {nomeTabela} where {dado}")
                return dict(self.cursor.fetchall()[0])
        else:
            self.cursor.execute(f"SELECT * FROM '{nomeTabela}'")
            if str(self.cursor.fetchall()) == '[]':
                return {"erro":'Banco de Dados Vazio!'}
            else:
                self.cursor.execute(f"SELECT * FROM '{nomeTabela}'")
                return list(x for x in self.cursor.fetchall())


    def apagarBanco(self, nomeTabela):
        self.cursor.execute(f"DELETE FROM {nomeTabela}")
        self.bancoDados.commit()


    def apagarDados(self, nomeTabela, dados):
        self.cursor.execute(f"DELETE from {nomeTabela} where {dados}")
        self.bancoDados.commit()
        print('dados apagados')

    @classmethod
    def consultaDados(self, nomeTabela, dados):
        for x in self.pegarDados(nomeTabela):
            try:
                if str(dados) in str(dict(x)):
                    return False
                else: continue
            except ValueError:
                return True
        else: return True


#teste = BancoDados('teste')

#teste.criarTabela('Vendedores', "'Nome', 'Idade', 'Sexo'")
#print((teste.inserirDados("Vendedores", {'Nome':'Aldenir', 'Idade':28, 'Sexo':'Masculino'})))

#teste.apagarBanco("Vendedores")
#teste.apagarDados("Vendedores", "Nome='Aldenir'")


#print(teste.pegarDados('Vendedores', dado="Nome='Aldenir'"))
'''for dado in teste.pegarDados('Vendedores'):
    try:
        for key, value in dict(dado).items():
            print(f'|\t{key}\t: {value}')
    except ValueError as erro:
        print(dado)
        print(erro)'''
