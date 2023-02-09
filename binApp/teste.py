import sqlite3
from sqlite3 import Error


banco = 'teste.db'
conn = sqlite3.connect(banco)
cursor = conn.cursor()


dictDados = {
    'nome da rota:': 'Campina', 'data da rota:': '2_03_2023', 'data para retorno:': '21_03_2022',
    'saldo cobrado:': '10000', 'repasse cobrado:': '1000', 'total cobrado:': '11000',
    'repasse novo:': '1000', 'repasse total:': '2000', 'fichas novas:': '40',
    'fichas em branco:': '1', 'fichas repasse:': '2', 'total fichas:': '43',
    'venda anterior:': '3000', 'devolucao de rua:': '10000', 'total vendido:': '20000',
    'compra deposito:': '30000', 'entrega deposito:': '10000', 'venda nova:': '30000',
    'brindes:': '1000', 'vl fichas branco:': '1000', 'total na rua:': '31000',
    'despesa rota:': '1000', 'despesa extra:': '1000'}

def gerBanco(**kwargs):
    
    nTable = f"{kwargs.get('nome')}{kwargs.get('datarota')}"
    try:
        cursor.execute(f"CREATE TABLE {nTable} {tuple(kwargs.keys())}")
        cursor.execute(f"INSERT INTO {nTable} VALUES{tuple(kwargs.values())}")
        conn.commit()
    except Error as erro:
        print(erro)
        cursor.execute(f"INSERT INTO {nTable} VALUES{tuple(kwargs.values())}")
        conn.commit()
    
if __name__ == '__main__':
    gerBanco(**dictDados)
    #xtractKeys(dictDados)

