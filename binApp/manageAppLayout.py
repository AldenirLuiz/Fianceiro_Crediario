import tkinter.messagebox
from tkinter import END
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
            if self.verifyTable(_verify_all=True):
                self.tableRequest: list = self.queryRequestTables(_last=True)
                self.keysRequest: list = self.queryRequestColumns(self.tableRequest[-1][0])
                self.dataRequest: list = self.queryRequestTables(_table=self.tableRequest[-1][0])
                self.values = dict(zip(self.keysRequest, self.dataRequest[0]))
            
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
        self.valText = self.janelaCob.type_widget('text')

        # criando a janela de cadastros
        self.janelaCad = SubGrade(self.widgets['Cadastros'], 'entry')
        self.valEntry = self.janelaCad.type_widget('botao')

        # adicionando os comandos aos botoes
        self.valEntry['btts']['btt1'].configure(
            command=lambda: self.colect_data())
        self.valEntry['btts']['btt0'].configure(
            command=lambda: self.command_delete())

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
        query_state = self.dataQuery.queryAdd(_data=values)

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
