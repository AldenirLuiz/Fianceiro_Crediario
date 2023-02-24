import sqlite3
from sqlite3 import Error
from random import randint

banco = 'dadosCobranca.db'
conn = sqlite3.connect(banco)
cursor = conn.cursor()


cityNames = ["Campina", "Patos", "Itaporanga", "Juazeirinho", "Brejo"]
dictDados = dict()


def ger_banco(**kwargs):

    table_name = f"{kwargs.get('nome da rota:')}{kwargs.get('data da rota:')}"
    try:
        cursor.execute(f"CREATE TABLE {table_name} {tuple(kwargs.keys())}")
        cursor.execute(f"INSERT INTO {table_name} VALUES{tuple(kwargs.values())}")
        conn.commit()
    except Error as erro:
        print(erro)
        cursor.execute(f"INSERT INTO {table_name} VALUES{tuple(kwargs.values())}")
        conn.commit()


def dict_dados():
    global dictDados
    for city in cityNames:
        temp_data = {
            'nome da rota:': f'{city}',
            'data da rota:': f'{randint(1, 31)}_{randint(1, 12)}_2023',
            'data para retorno:': f'{randint(1, 31)}_{1, 12}_2023',
            'saldo cobrado:': f'{randint(5500, 12000)}',
            'repasse cobrado:': f'{randint(300, 1200)}',
            'repasse novo:': f'{randint(800, 1500)}',
            'fichas novas:': f'{randint(34, 44)}',
            'fichas em branco:': f'{randint(0, 6)}',
            'fichas repasse:': f'{randint(2, 12)}',
            'venda anterior:': f'{randint(28000, 36000)}',
            'devolucao de rua:': f'{randint(8769, 12540)}',
            'compra deposito:': f'{randint(29440, 32400)}',
            'venda nova:': f'{randint(18890, 36783)}',
            'brindes:': f'{randint(112, 323)}',
            'vl fichas branco:': f'{randint(0, 1000)}',
            'despesa rota:': f'{randint(600, 1000)}',
            'despesa extra:': f'{randint(0, 1000)}'}
        dictDados.update({f'{city}': temp_data})
    return dictDados


if __name__ == '__main__':

    tempString = dict()
    tempString.update(dictDados)
    ger_banco(**tempString)
