import sqlite3 as db
from sqlite3 import OperationalError, Connection, Cursor
from typing import Union
try:
    from binApp.manageDir import Diretorio
    from binApp.loging import Logger as log
except ModuleNotFoundError:
    from manageDir import Diretorio


class HandlerDB:
    __ROOT_DIR__:str = Diretorio()
    __DATABASE__:str = 'dadosCobranca.db'

    _query_table_exists:str = "SELECT name FROM sqlite_master WHERE type='table';"
    _query_table_check:str = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';"
    _temp_query_columns:str = "PRAGMA table_info({})"
    _request_data_from:str = "SELECT * FROM '{}'"
    _error_code_table:str = "Tabela Inexistente"

    def __init__(self) -> None:
        try:
            self.banco:Connection = db.connect(
                f'{self.__ROOT_DIR__}/dataBase/{self.__DATABASE__}')
            self.cursor:Cursor = self.banco.cursor()
        except OperationalError as _erro:
            message:str = f"""Problema ao Conectar com o Banco de dados.\n
                ->Possivel erro de permissao de leitura/gravacao, 
                Contate o administrador do Sistema.
                ERRO:{_erro}"""
            log.retListApp(message)
            self.ErrConnectDB(message)


    def queryAdd(self, _data:dict[str, str]) -> str:
        _table_:str = f"{_data['nome da rota:']}{_data['data da rota:']}"
        temp_table_create:str = f"CREATE TABLE {_table_} {tuple(_data.keys())};"
        temp_data_adict:str = f"INSERT INTO {_table_} VALUES{tuple(_data.values())};"

        if self.verifyTable(_table=_table_):
            self.cursor.execute(temp_table_create)
            self.banco.commit()
            self.cursor.execute(temp_data_adict)
            self.banco.commit()
            return "All data are aded"
        else:
            return f"A tabela {_table_} ja existe no banco de dados!"


    def queryRequestTables(self, _table:str=None, _last:bool=False) -> list:

        if _last:
            try:
                return self.cursor.execute(self._query_table_exists.format(_table)).fetchall()
            except db.Error as _erro:
                raise _erro

        if not self.verifyTable(_table):
            return [self._error_code_table, _table]
        else:
            try:
                return self.cursor.execute(self._request_data_from.format(_table)).fetchall()
            except db.Error as _erro:
                raise _erro
    

    def queryRequestColumns(self, _table:str) -> list:

        if self.verifyTable(_table):
            return [
                column[1] for column 
                in self.cursor.execute(self._temp_query_columns.format(_table)).fetchall()]
        else:
            return [self._error_code_table, _table]


    def verifyTable(self, _table:str=None, _verify_all=False) -> bool:
        
        if _verify_all:
            if self.cursor.execute(self._query_table_exists.format(_table)).fetchall() != None:
                return True
            else: return False

        if self.cursor.execute(self._query_table_check.format(_table)).fetchone() != tuple():
            return True
        else:
            return False
    
    class ErrConnectDB(Exception):
        pass


if __name__ == "__main__":
    from teste import dictDados
    hand = HandlerDB()
    #print(hand.verifyTable('Campina'))
    #print(Diretorio.retWayFile('dataBase', 'dadosCobranca.db'))
    print(hand.queryAdd("campina19_02_2023", dictDados))
    #temp = hand.queryRequestTables(_table='Campina21_07_2022', _last=False)
    #print(temp)
    #table = hand.queryRequestTables(_last=True)
    #print(hand.queryRequestTables(_table=table[0][0]))


