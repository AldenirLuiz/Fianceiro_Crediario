from tkinter.messagebox import showinfo, WARNING, showwarning
from tkinter import END
from binApp.manageBd import Gerente as Gb
from binApp.manageQuery import BancoDados as bd
from teste import dictDados
from .mainApp import Janela, subGrade, Layout


class Manipulador(Janela, subGrade, Layout):
    def __init__(self) -> None:
        super().__init__()
        # definindo o nome do banco de dados
        self.gerente = Gb( banco='dadosCobranca.db' )
        self.queryData = bd.pegarDados(self.gerente.banco, "Campina")
        # criando a janela de cobrancas
        self.janelaCob = subGrade(self.widgets['Cobrancas'], 'label', dados=self.queryData[0])
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
        queryState = self.gerente.gerenteBd(dados=dictDados, query='add')
        #PARA USAR OS DADOS DE ENTRADA DA GUI SUBSTITUIR (dictDados) POR (dictValues)
        #PARA USAR OS DADOS DE ENTRADA DE TESTE SUBSTITUIR (dictValues) POR (dictDados)

        if queryState != 'dados inseridos':
            warningWindow = showwarning(
                title="ATENÇÃO!", message=f'{queryState}', icon=WARNING)
            pass
        else:
            warningWindow = showinfo(title="TUDO OK", message=f'{queryState}')
        
        