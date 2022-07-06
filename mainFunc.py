
import sqlite3
from sqlite3 import Error


class BancoDados:
    def __init__(self, banco) -> None:
        
        self.bancoDados = sqlite3.connect(f'{banco}.db')
        self.bancoDados.row_factory = sqlite3.Row
        self.cursor = self.bancoDados.cursor()

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

    def consultaDados(self, nomeTabela, dados):
        for x in self.pegarDados(nomeTabela):
            try:
                if str(dados) in str(dict(x)):
                    return False
                else: continue
            except ValueError:
                return True
        else: return True


teste = BancoDados('teste')

#teste.criarTabela('Vendedores', "'Nome', 'Idade', 'Sexo'")
#print((teste.inserirDados("Vendedores", {'Nome':'Aldenir', 'Idade':28, 'Sexo':'Masculino'})))

#teste.apagarBanco("Vendedores")
#teste.apagarDados("Vendedores", "Nome='Aldenir'")


#print(teste.pegarDados('Vendedores', dado="Nome='Aldenir'"))
for dado in teste.pegarDados('Vendedores'):
    try:
        for key, value in dict(dado).items():
            print(f'|\t{key}\t: {value}')
    except ValueError as erro:
        print(dado)
        print(erro)
