from tkinter.messagebox import showinfo, WARNING, showwarning
from tkinter import END
from binApp.dataHandler import HandlerDB
from binApp.teste import dictDados
from .mainApp import Janela, subGrade, Layout


class Manipulador(Janela, subGrade, Layout):
    def __init__(self) -> None:
        super().__init__()
        # criando a janela de cobrancas

        self.data = HandlerDB()
        self.tableRequest:list = self.data.queryRequestTables(_last=True)
        self.keysRequest:list = self.data.queryRequestColumns(self.tableRequest[-1][0])
        self.dataRequest:list = self.data.queryRequestTables(_table=self.tableRequest[-1][0])
        self.dictValues = dict(zip(self.keysRequest, self.dataRequest[0]))

        self.janelaCob = subGrade(self.widgets['Cobrancas'], 'label', dados=self.dictValues)
        self.valText = self.janelaCob.typeWidget('text')
        # criando a janela de cadastros
        self.janelaCad = subGrade(self.widgets['Cadastros'], 'entry')
        self.valEntry = self.janelaCad.typeWidget('botao')
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
        queryState = self.data.queryAdd(self, dictDados['nome da rota:'], dictDados)
        #PARA USAR OS DADOS DE ENTRADA DA GUI SUBSTITUIR (dictDados) POR (dictValues)
        #PARA USAR OS DADOS DE ENTRADA DE TESTE SUBSTITUIR (dictValues) POR (dictDados)

        if queryState != 'dados inseridos':
            showwarning(
                title="ATENÇÃO!", message=f'{queryState}', icon=WARNING)
            pass
        else:
            showinfo(title="TUDO OK", message=f'{queryState}')


        
        