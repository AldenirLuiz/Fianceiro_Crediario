import sqlite3 as db
from sqlite3 import OperationalError, Connection, Cursor

try:
    from binApp.manageDir import Diretorio
    from binApp.loging import Logger as Log
except ModuleNotFoundError:
    from manageDir import Diretorio


class HandlerDB:
    __ROOT_DIR__: str = Diretorio()
    __DATABASE__: str = 'dadosCobranca.db'

    _query_table_exists: str = "SELECT name FROM sqlite_master WHERE type='table';"
    _query_table_check: str = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';"
    _temp_query_columns: str = "PRAGMA table_info({})"
    _request_data_from: str = "SELECT * FROM '{}'"
    _error_code_table: str = "Tabela Inexistente"

    def __init__(self) -> None:
        try:
            self.banco: Connection = db.connect(
                f'{self.__ROOT_DIR__}/dataBase/{self.__DATABASE__}')
            self.cursor: Cursor = self.banco.cursor()
        except OperationalError as _erro:
            message: str = f"""Problema ao Conectar com o Banco de dados.\n
                ->Possivel erro de permissao de leitura/gravacao, 
                Contate o administrador do Sistema.
                ERRO:{_erro}"""
            Log.retListApp(message)
            self.ErrConnectDB(message)

    def query_add(self, _data: dict[str, str]) -> str:
        _table_: str = f"{_data['nome da rota:']}{_data['data da rota:']}"
        temp_table_create: str = f"CREATE TABLE {_table_} {tuple(_data.keys())};"
        temp_data_adict: str = f"INSERT INTO {_table_} VALUES{tuple(_data.values())};"

        if self.verify_tables(_table=_table_):
            self.cursor.execute(temp_table_create)
            self.banco.commit()
            self.cursor.execute(temp_data_adict)
            self.banco.commit()
            return "All data are aded"
        else:
            return f"A tabela {_table_} ja existe no banco de dados!"

    def query_request_tables(self, _table: str = None) -> list:
        print(f"query request: {_table}")

        if not self.verify_tables(_table):
            return [self._error_code_table, _table]
        else:
            try:
                return self.cursor.execute(self._request_data_from.format(_table)).fetchall()
            except db.Error as _erro:
                raise _erro

    def query_request_columns(self, _table: str) -> list:

        if self.verify_tables(_table):
            return [
                column[1] for column 
                in self.cursor.execute(self._temp_query_columns.format(_table)).fetchall()]
        else:
            return [self._error_code_table, _table]

    def verify_tables(self, _table: str) -> bool:

        _query_check = self.cursor.execute(self._query_table_check.format(_table)).fetchall()
        if _query_check != list():
            return False
        else:
            return True

    def check_table(self):
        _query_exists = self.cursor.execute(self._query_table_exists).fetchall()
        if _query_exists:
            return _query_exists
        else:
            return []
    
    class ErrConnectDB(Exception):
        pass


if __name__ == "__main__":
    from teste import dictDados
    hand = HandlerDB()
    print(hand.verify_tables('Itaporanga28_2_2023'))
    # print(Diretorio.retWayFile('dataBase', 'dadosCobranca.db'))
    # print(hand.query_add(dictDados))
    # temp = hand.queryRequestTables(_table='Campina21_07_2022', _last=False)
    # print(temp)
    # table = hand.queryRequestTables(_last=True)
    # print(hand.queryRequestTables(_table=table[0][0]))
