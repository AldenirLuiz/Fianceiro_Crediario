from tkinter import *
from tkinter import ttk
from binApp.mainLayout import Layout
import json
from binApp.manageDir import Diretorio as _DIR_



class Janela:
    def __init__(self) -> None:
        self.window = Tk()
        #self.window.geometry('560x600')
        self.window.anchor('center')
        self.frameLogin = Frame(self.window, relief='flat')
        self.frameLogin.pack(expand='yes', fill='both', anchor='center')
        self.noteBook = ttk.Notebook(self.frameLogin, padding=8)
        self.noteBook.pack(expand='yes', fill='both', anchor='center')
        # widgets: este container guardara os frames do notebook para acesso posterior
        self.widgets = dict() # acesesso: self.widgets['nome do widget']
        # noteNomes: lista os nomes para nomear as abas do notebook.
        self.noteNomes = ['Cobrancas', 'Rotas', 'Cadastros', 'Historico']
        # valEntrys: este container guardara as entrys para acesso posterior.
        self.valEntry = dict()
        # percorre os nomes predefinidos em noteNomes, cada nome sera uma aba
        for index in self.noteNomes:
            # cada aba recebera um frame, isso garante que novos widgets possam ser adicionados
            frm = Frame(self.noteBook, relief='flat')
            self.widgets[index] = frm # adiciona o frame ao conteiner
            # cria a aba no notebook com o nome predefinido na lista de nomes
            self.noteBook.add(self.widgets[index], text=index) 
            # text=index-> |index: nome predefinido na lista de nomes, \
                # a celula recebe a chave do widget como nome|
        
####### ESTA CLASSE E RESPONSAVEL POR CRIAR UMA GRADE DINAMICA DE |FRAMES|WIDGETS| ####### 
class subGrade:

    def __init__(self, notebook, tWidget, dados=None) -> None:
        self.message = 'VERIFIQUE OS DADOS ANTES \nDE SALVAR.'
        self.tipoWidget = tWidget
        self.widgetPack = dict()
        self.vtext = dados
        self.propert_layers = viewCard()

    ####################### |CARDS DO LAYOUT| #######################
        # Frame data da rota e retorno
        self.framePai0 = Frame(notebook)
        self.widgetPack.update(
            Layout.creatLay(
                pai=self.framePai0, 
                celulas=self.propert_layers.retCard('celNomesL0'), 
                tWid=self.tipoWidget, 
                desc='dados da cobranca',
                data=dados
            )
        )

        self.framePai0.grid(row=0, column=0)
        # Frame dos cards cobranca e capitial se giro
        self.framePai0 = Frame(notebook)
        lay1 = Layout.creatLay(self.framePai0, self.propert_layers.retCard("celNomesL1"), self.tipoWidget, data=dados)
        self.widgetPack.update(lay1)
        self.framePai0.grid(row=1, column=0)
        # Frame dos cards dados da rota e capitial se giro
        self.framePai2 = Frame(notebook)
        lay2 = Layout.creatLay(self.framePai2, self.propert_layers.retCard("celNomesL2"), self.tipoWidget, data=dados)
        self.widgetPack.update(lay2)
        self.framePai2.grid(row=2, column=0)
        # Frame dos cards saldo devedor e deposito
        self.framePai3 = Frame(notebook)
        lay3 = Layout.creatLay(self.framePai3, self.propert_layers.retCard("celNomesL3"), self.tipoWidget, data=dados)
        self.widgetPack.update(lay3)
        self.framePai3.grid(row=3, column=0)
        # Frame dos cards fichas e mercadoria na rua
        self.framePai4 = Frame(notebook, relief='groove')
        # OS WIDGETS DESTA FRAME SERAO POSTOS NA FUNCAO typeWidget
        self.framePai4.grid(row=4, column=0,) 
        
    ####### CONFIGURACOES DA GRADE DO LAYOUT (TIPOS DE WIDGET SECUNDARIOS) #######
    def typeWidget(self, subWidget, dados=None):
        # ESTA CONDICAO VERIFICA O TIPO DE WIDGET REQUERIDO
        if subWidget == 'text': # Neste caso "text" adiciona widget de caixa de texto \
                                    # no espaco reservado do layout
            self.subCellWid = Text(self.framePai4, width=34, height=4)
            self.subCellWid.insert(0.0, 'OBSERVACOES:') # textbox para observacoes
            # o widget gerado nesta condicao e adicionado ao container de widgets
            lay0 = Layout.creatLay( # Empacotando os widgets criados pela classe Layout
                    self.framePai4, self.propert_layers.retCard("celNomesL4"), 
                    self.tipoWidget, subwidget=self.subCellWid, data=dados)
            self.widgetPack.update(lay0)
        elif subWidget == 'botao': # Neste caso "botao" adiciona os
                                    # botoes no espaco reservado do layout
            self.frmBtt = Frame(self.framePai4)
            self.subCellWid = Label(
                    self.frmBtt, text=self.message, fg='green', width=34, height=4)
            self.subCellWid.pack(expand='yes', fill='both', pady=2, ipadx=2, ipady=2)
            self.subButonWid0 = Button(
                    self.frmBtt, text='Limpar Campos',bg='orange')
            self.subButonWid0.pack(side='left', pady=2, ipadx=2, ipady=2)
            self.subButonWid1 = Button(
                    self.frmBtt, text='Cadastrar Valores',bg='green')
            self.subButonWid1.pack(side='right', pady=2, ipadx=2, ipady=2)
            self.widgetPack['btts'] = {
                    'btt1': self.subButonWid1, 'btt0' : self.subButonWid0}
             # Empacotando os widgets criados pela classe Layout
            lay1 = Layout.creatLay(self.framePai4, self.propert_layers.retCard("celNomesL4"), 
                          tWid=self.tipoWidget, subwidget=self.frmBtt)
            self.widgetPack.update(lay1)
        else: #por fim se nenhuma destes foi solicitado, o espaco reservado permanece vazio
             # Empacotando os widgets criados pela classe Layout
            lay2 = Layout.creatLay(self.framePai4, self.propert_layers.retCard("celNomesL4"), 
                          tWid=self.tipoWidget)
            self.widgetPack.update(lay2)
        # por fim o configurador retorna os devidos widgets empacotados em self.widgetPack.
        return self.widgetPack



class viewCard:

    def __init__(self) -> None:
        self.config_json = f"{_DIR_()}/cellNames.json"
    
    def retCard(self, card:str, celula:str=None) -> list:
        with open(self.config_json, "r") as cell_names:
            self.propert_layers = json.load(cell_names)

        if celula:
            return self.propert_layers[card][celula]
        
        return self.propert_layers[card]