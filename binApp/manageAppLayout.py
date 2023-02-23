import tkinter.messagebox
from tkinter import *
from .dataHandler import HandlerDB
from .teste import dictDados
from .mainApp import Janela, SubGrade, Layout
from .loging import Logger as Log


class LastTable(HandlerDB):
    def __init__(self) -> None:
        super().__init__()
        self.log = Log()
        self.values = dictDados
        try:
            if self.check_table():
                self.tableRequest: str = self.check_table()[-1][0]
                # print(f"tableRequest: {self.tableRequest}")
                self.keysRequest: list = self.query_request_columns(_table=self.tableRequest)
                # print(f"keysRequest: {self.keysRequest}")
                self.dataRequest: list = self.query_request_tables(_table=self.tableRequest)
                # print(f"dataRequest: {self.dataRequest[0]}")
                self.values = dict(zip(self.keysRequest, self.dataRequest[0]))
            
        except IndexError as _erro:
            Log.retListApp(str(_erro))

    def query_data(self, table):
        # print(f"query_data/table: {table}")
        try:
            if self.check_table():
                values_request: list = self.query_request_tables(table)
                keys_request: list = self.query_request_columns(table)
                values = dict(zip(keys_request, values_request[0]))
                return values

        except IndexError as _erro:
            Log.retListApp(str(_erro))

    def _dict_values(self) -> dict:
        values = self.values
        return values


class Manipulador(Janela, SubGrade, Layout, LastTable):
    def __init__(self) -> None:
        super().__init__()
        # criando a janela de cobrancas
        self.dataQuery = LastTable()
        self.last_data = self.dataQuery._dict_values()
        
        self.janelaCob = SubGrade(self.widgets['Cobrancas'], 'label', dados=self.last_data)

        self.menubar = Menu(self.window_root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(
            label="ROTAS", menu=self.filemenu, command=self.comand_menu
        )
        self.db = HandlerDB()
        self.tables = self.db.check_table()

        self.valText = self.janelaCob.type_widget('text')

        # criando a janela de cadastros
        self.janelaCad = SubGrade(self.widgets['Cadastros'], 'entry')
        self.valEntry = self.janelaCad.type_widget('botao')

        # adicionando os comandos aos botoes
        self.valEntry['btts']['btt1'].configure(
            command=lambda: self.colect_data())
        self.valEntry['btts']['btt0'].configure(
            command=lambda: self.command_delete())
        self.refresh_menu()

    def comand_menu(self, table_name):
        query = self.dataQuery.query_data(f'{table_name}')
        # print(f"command menu: {query}")
        self.janelaCob = SubGrade(
            self.widgets['Cobrancas'], 'label', query)
        self.refresh_menu()

    def refresh_menu(self):
        self.menubar = Menu(self.window_root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(
            label="ROTAS", menu=self.filemenu, command=self.comand_menu
        )
        self.tables = self.db.check_table()
        for table in self.tables:
            # print(f"table_init: {table}")
            self.filemenu.add_command(
                label=table[0], command=lambda x=f'{table[0]}': self.comand_menu(x)
            )
            self.filemenu.add_separator()
        self.window.configure(menu=self.menubar)

    def command_delete(self) -> None:
        for keyWidget in self.valEntry.keys():
            if keyWidget != 'btts':
                self.valEntry[keyWidget].delete(0, END)
            else:
                continue

    def colect_data(self) -> None:
        dict_values: dict = dict()
        for keyWidget in self.valEntry.keys():
            if keyWidget != 'btts':
                widget_text = self.valEntry[keyWidget].get()
                dict_values[keyWidget] = widget_text
        self.data_save(dict_values)

    def data_save(self, values) -> None:
        query_state = self.dataQuery.query_add(_data=values)
        self.refresh_menu()
        if query_state != 'dados inseridos':
            tkinter.messagebox.showwarning(
                title="ATENÇÃO!",
                message=f'{query_state}',
                icon=tkinter.messagebox.WARNING)
        else:
            tkinter.messagebox.showinfo(
                title="TUDO OK",
                message=f'{query_state}'
            )


if __name__ == "__main__":
    temp = LastTable()
    print(temp)
