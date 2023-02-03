import sqlite3
from sqlite3 import Error
try:
    from binApp import manageDir as mdir
except ModuleNotFoundError:
    import manageDir as mdir

''' Aldenir luiz| 22/07/2022
    Prezado Contribuidor, por favor nao remover funcoes nao utilizadas!
    todas as ferramentas serao implementadas nas screens 
    posteriormente quando as mesmas forem criadas, desde ja agradecemos.'''


class BancoDados:
    def __init__( self, banco ) -> None:
        ### obtendo o caminho de execucao do script ###
        self.execDir = str( mdir.Diretorio )
        ### obtendo o caminho do log do diretorio ###
        #self.logDir = str( mdir.Logger.retListApp(self) )
        ### obtendo o nome do banco de dados solicitado ###
        self.nomeBanco = banco
        ### criando conexao com o banco###
        self.bancoDados = sqlite3.connect( banco )
        ### setando os retornos para o formato de chave|valor
        self.bancoDados.row_factory = sqlite3.Row # <-|todas as requisicoes serao retornadas como dict()|
        ### criando cursor
        self.cursor = self.bancoDados.cursor( )
    
           
    #### FUNCAO RESPONSAVEL POR GRAVAR OS DADOS NO BANCO DE DADOS #### #IMPLEMENTADA!#
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
            print(f"Erro Ao inserir dados: ErrValue: {erro}")
            # retorna uma string alertando que as alteracoes nao foram feitas, a descricao do erro vai anexada.
            return f'Erro! Os Dados Nao Foram Inseridos\n{ erro }'


    #### ESTA FUNCAO E RESPONSAVEL PELAS CONSULTAS AO BANCO DE DADOS #### |NAO IMPLEMENTADA NA GUI!|
    def pegarDados( self, nomeTabela, dado=None ):
        try: # selecionando a tabela requisitada, caso exista.
            tables = self.cursor.execute( f"SELECT '{ nomeTabela }' FROM sqlite_master" ).fetchall( )
            # condicao que verifica se o BANCO esta vazio
            if str( tables ) == '[]':
                return { "erro":'Banco de Dados Vazio!' }
            # se o argumento dado for passado, uma busca e executada
            if dado: 
                # o fluxo do programa sera desviada para consultaDados(), 
                if self.consultaDados( nomeTabela, dado ): # o fluxo retorna confirmando ou nao a existencia dos dados
                    retData = self.cursor.execute( f"SELECT * FROM { nomeTabela } where { dado }" )
                    return retData.fetchall() # Retorno com o dado requisitado
                else: # Retorno de dados inexistentes
                    return "Os dados nao foram encontrados"
            else: # se o argumento dado nao for passado, uma busca geral e executada
                retData = self.cursor.execute( f"SELECT * FROM '{ nomeTabela }'" )
                return retData.fetchall()
        except Error as erro: # em caso de erro, a funcao nao continua.
            print(f"O seguinte Erro ocorreu ao consultar os dados: {erro}")
            # retorna uma string alertando que aconsulta nao pode ser feita, a descricao do erro vai anexada.
            return f'Erro! \n{ erro }'


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
                return False
        except sqlite3.OperationalError:
            return False
    

if __name__ == '__main__':
    ######## MANTER ESTAS LINHAs COMO TEST DRIVER DO BANCO ########
    dataTest = {'Nome': 'Aldenir', 'Idade': 22, 'Sexo': 'Masculino'}
    teste = BancoDados( 'teste.db' )
    #teste.inserirDados('Teste', **dataTest)
    
    #teste.apagarDados("Vendedores", "Nome='Aldenir'")
    retorno = teste.pegarDados('Teste', dado="Nome='Aldenir'")
    print(f"Resultado da Consulta: {dict(retorno[0])}")
    #print( teste.consultaDados( 'Teste', dados="Nome='Aldenir'" ) )
