from tkinter.messagebox import showinfo, WARNING, showwarning
from tkinter import END

from .dataHandler import HandlerDB
from .teste import dictDados
from .mainApp import Janela, SubGrade, Layout, ViewCard
from .loging import Logger as log



class LastTable(HandlerDB):

    def __init__(self) -> None:
        super().__init__()
        self.log = log()
        self.values = dictDados
        try:
            if self.verifyTable(_verify_all=True):
                self.tableRequest: list = self.queryRequestTables(_last=True)
                self.keysRequest: list = self.queryRequestColumns(self.tableRequest[-1][0])
                self.dataRequest: list = self.queryRequestTables(_table=self.tableRequest[-1][0])
                self.values = dict(zip(self.keysRequest, self.dataRequest[0]))
            
        except IndexError as _erro:
            log.retListApp(_erro)

    def _dictValues(self) -> dict:
        values = self.values
        return values
        


class Manipulador(Janela, SubGrade, Layout, LastTable):
    def __init__(self) -> None:
        super().__init__()
        # criando a janela de cobrancas
        self.dataQuery = LastTable()
        self.last_data = self.dataQuery._dictValues()
        
        self.janelaCob = SubGrade(self.widgets['Cobrancas'], 'label', dados=self.last_data)
        self.valText = self.janelaCob.type_widget('text', dados=self.last_data)
        # criando a janela de cadastros
        self.janelaCad = SubGrade(self.widgets['Cadastros'], 'entry')
        self.valEntry = self.janelaCad.type_widget('botao')
        # adicionando os comandos aos botoes
        self.valEntry['btts']['btt1'].configure(
            command=lambda: self.comander('add'))
        self.valEntry['btts']['btt0'].configure(
            command=lambda: self.comander('delete'))

    
    # funcao de comando dos botoes
    def comander(self, command) -> None:
        # dicionario para empacotar os valores das entrys
        dictValues = dict()
        # condicao para o comando do botao de limpar
        if command == 'delete':
            for keyWidget in self.valEntry.keys():
                if keyWidget != 'btts': # filtra os widgets 
                    # se o widget for um botao, a condicao passa
                    self.valEntry[keyWidget].delete(0, END)
                else: continue
            else: return 0
        else: # condicao para o comando de gravar dados
            for keyWidget in self.valEntry.keys():
                if keyWidget != 'btts': # filtra os widgets
                    # se o widget for um botao, a condicao passa
                    widgetText = self.valEntry[keyWidget].get()
                    dictValues[keyWidget] = widgetText
                    
                else: continue
        # cria uma requisicao no gerente do banco de dados para adicionar os dados
        queryState =  self.dataQuery.queryAdd(_data=dictValues)
        #PARA USAR OS DADOS DE ENTRADA DA GUI SUBSTITUIR (dictDados) POR (dictValues)
        #PARA USAR OS DADOS DE ENTRADA DE TESTE SUBSTITUIR (dictValues) POR (dictDados)

        if queryState != 'dados inseridos':
            showwarning(
                title="ATENÇÃO!", message=f'{queryState}', icon=WARNING)
            pass
        else:
            showinfo(title="TUDO OK", message=f'{queryState}')


        
if __name__ == "__main__":
    temp = LastTable()
    print(temp)
