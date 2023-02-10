import sqlite3
from sqlite3 import Error
from random import randint

banco = 'teste.db'
conn = sqlite3.connect(banco)
cursor = conn.cursor()


cityNames = ["Campina", "Patos", "Itaporanga", "Juazeirinho", "Brejo",]

dictDados = {
    'nome da rota:': f'Campina', 
    'data da rota:': f'{randint(1, 31)}_{randint(1, 12)}_2023', 
    'data para retorno:': f'{randint(1,31)}_{1,12}_2023',
    'saldo cobrado:': f'{randint(5500, 12000)}', 
    'repasse cobrado:': f'{randint(300, 1200)}', 
    'total cobrado:': f'{randint(600, 13000)}',
    'repasse novo:': f'{randint(800, 1500)}', 
    'repasse total:': f'{randint(1000, 2000)}', 
    'fichas novas:': f'{randint(34,44)}',
    'fichas em branco:': f'{randint(0,6)}', 
    'fichas repasse:': f'{randint(2, 12)}', 
    'total fichas:': f'{randint(35, 47)}',
    'venda anterior:': f'{randint(28000, 36000)}', 
    'devolucao de rua:': f'{randint(8769, 12540)}', 
    'total vendido:': f'{randint(24000, 32530)}',
    'compra deposito:': f'{randint(29440, 32400)}', 
    'entrega deposito:': f'{randint(12580, 16678)}', 
    'venda nova:': f'{randint(18890, 36783)}',
    'brindes:': f'{randint(112, 323)}', 
    'vl fichas branco:': f'{randint(0, 1000)}', 
    'total na rua:': f'{randint(28746, 40453)}',
    'despesa rota:': f'{randint(600, 1000)}', 
    'despesa extra:': f'{(0, 1000)}'}


def gerBanco(**kwargs):
    
    nTable = f"{kwargs.get('nome da rota:')}{kwargs.get('data da rota:')}"
    try:
        cursor.execute(f"CREATE TABLE {nTable} {tuple(kwargs.keys())}")
        cursor.execute(f"INSERT INTO {nTable} VALUES{tuple(kwargs.values())}")
        conn.commit()
    except Error as erro:
        print(erro)
        cursor.execute(f"INSERT INTO {nTable} VALUES{tuple(kwargs.values())}")
        conn.commit()





if __name__ == '__main__':
    tempString = dict()
    for city in cityNames:
        tempString.update(dictDados)
        gerBanco(**tempString)

