import sqlite3 as db
try:
    from binApp.manageDir import Diretorio
except ModuleNotFoundError:
    from manageDir import Diretorio


class HandlerDB:
    __ROOT_DIR__ = Diretorio()
    __DATABASE__ = 'dadosCobranca.db'

    def __init__(self) -> None:
        try:
            self.banco = db.connect(self.__ROOT_DIR__.retWayPath(f'dataBase/{self.__DATABASE__}'))
        except Diretorio.ErrDir:
            raise self.ErrConnectDB(
                """Problema ao Conectar com o Banco de dados.\n
                ->Possivel erro de permissao de leitura/gravacao, 
                Contate o administrador do Sistema."""
            )
        self.cursor = self.banco.cursor()

    def queryAdd(self, _data:dict):
        print(_data.keys())
        _table_ = f"{_data['nome da rota:']}{_data['data da rota:']}"
        temp_table_create = f"CREATE TABLE {_table_} {tuple(_data.keys())};"
        temp_data_adict = f"INSERT INTO {_table_} VALUES{tuple(_data.values())};"

        if not self.verifyTable(_table_):
            self.cursor.execute(temp_table_create)
            self.banco.commit()
            self.cursor.execute(temp_data_adict)
            self.banco.commit()
            return "All data are aded"
        else:
            return f"A tabela {_table_} ja existe no banco de dados!"


    def queryRequestTables(self, _table:str=None, _last:bool=False) -> list:
        
        temp_request_table = "SELECT name FROM sqlite_master WHERE type='table';"
        temp_request_data = f"SELECT * FROM '{_table}'"

        if _last:
            try:
                temp = self.cursor.execute(temp_request_table).fetchall()
                return temp
            except db.Error as _erro:
                raise _erro

        if not self.verifyTable(_table):
            return "Tabela Inexistente"
        else:
            try:
                temp = self.cursor.execute(temp_request_data)
                return temp.fetchall()
            except db.Error as _erro:
                raise _erro
    

    def queryRequestColumns(self, _table:str) -> list:
        temp_query_columns = f"PRAGMA table_info({_table})"
        
        if self.verifyTable(_table):
            temp_data = self.cursor.execute(temp_query_columns).fetchall()
            return [column[1] for column in temp_data]
        else:
            return "Tabela Inexistente"


    def verifyTable(self, _table:str) -> bool:
        temp_check_table = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{_table}';"
        if self.cursor.execute(temp_check_table).fetchone():
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


