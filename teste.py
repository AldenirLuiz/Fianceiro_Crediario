import sqlite3
from sqlite3 import Error


banco = 'teste.db'
conn = sqlite3.connect(banco)
cursor = conn.cursor()


dictDados = {
    'nome da rota:': 'Campina', 'data da rota:': '21072022', 'dataretorno': '21032022',
    'valcobrado': '10000', 'repcobrado': '1000', 'totcobrado': '11000',
    'repnovo': '1000', 'reptotal': '2000', 'fxnova': '40',
    'fxbranco': '1', 'fxrepasse': '2', 'fxtotal': '43',
    'vndanterior': '30000', 'devrua': '10000', 'totvendido': '20000',
    'cmpdeposito': '30000', 'entdeposito': '10000', 'vndnova': '30000',
    'brindes': '1000', 'flfxbranco': '1000', 'totrua': '31000',
    'desprota': '1000', 'dspextra': '1000'}

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
    

gerBanco(**dictDados)
#xtractKeys(dictDados)

