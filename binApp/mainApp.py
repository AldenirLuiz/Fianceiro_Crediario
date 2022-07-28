from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, WARNING, showwarning
from binApp.manageBd import Gerente as Gb
from teste import dictDados
from binApp.mainLayout import Layout

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
    def __init__(self, notebook, tWidget) -> None:
        self.message = 'VERIFIQUE OS DADOS ANTES \nDE SALVAR.'
        self.tipoWidget = tWidget
        self.widgetPack = dict()
        # A substituicao dos dados nestes dicionarios implica diretamente no aspecto geral do programa. 
        self.celNomesL0 = { # estes dicionarios predefinidos formam as celulas ou 'CARDS' dos widgets,
            'data da rota':['nome da rota\t\t:', 'data da rota\t\t:'], 
            'retorno':['data para retorno\t:']}
        self.celNomesL1 = { # a posicao dos widgets depende da ordem dos itens
            'cobranca':[
                'saldo cobrado\t:', 'repasse cobrado\t:', 'total cobrado\t:'], 
            'capital de giro':[
                'venda anterior\t:', 'devolucao de rua\t:', 'total vendido\t\t:']}
        self.celNomesL2 = { # a distribuicao dos cards se faz por meio das chaves
            'saldo devedor':[
                'repasse novo\t\t:', 'repasse total\t\t:'], 
            'deposito':[
                'compra deposito\t:', 'entrega deposito\t:']}
        self.celNomesL3 = { # cada lista como [valor] contem os nomes dos widgets a serem criados.
            'fichas':[
                'fichas novas\t\t:', 'fichas  repasse\t\t:', 'fichas em branco\t:', 'total fichas\t\t:'], 
            'mercadoria na rua':[
                'venda nova\t\t:', 'brindes\t\t\t:', 'vl fichas branco\t:', 'total na rua\t\t:']}
        self.celNomesL4 = {
            'despesas':['despesa rota\t\t:', 'despesa extra\t\t:']}
    ####################### |CARDS DO LAYOUT| #######################
        # Frame data da rota e retorno
        self.framePai0 = Frame(notebook)
        self.widgetPack.update(Layout.creatLay( pai=self.framePai0, 
                          celulas=self.celNomesL0, 
                          tWid=self.tipoWidget, desc='dados da cobranca'))
        self.framePai0.grid(row=0, column=0)
        # Frame dos cards cobranca e capitial se giro
        self.framePai0 = Frame(notebook)
        lay1 = Layout.creatLay(self.framePai0, self.celNomesL1, self.tipoWidget)
        self.widgetPack.update(lay1)
        self.framePai0.grid(row=1, column=0)
        # Frame dos cards dados da rota e capitial se giro
        self.framePai2 = Frame(notebook)
        lay2 = Layout.creatLay(self.framePai2, self.celNomesL2, self.tipoWidget)
        self.widgetPack.update(lay2)
        self.framePai2.grid(row=2, column=0)
        # Frame dos cards saldo devedor e deposito
        self.framePai3 = Frame(notebook)
        lay3 = Layout.creatLay(self.framePai3, self.celNomesL3, self.tipoWidget)
        self.widgetPack.update(lay3)
        self.framePai3.grid(row=3, column=0)
        # Frame dos cards fichas e mercadoria na rua
        self.framePai4 = Frame(notebook, relief='groove')
        # OS WIDGETS DESTA FRAME SERAO POSTOS NA FUNCAO typeWidget
        self.framePai4.grid(row=4, column=0,) 
        
    ####### CONFIGURACOES DA GRADE DO LAYOUT (TIPOS DE WIDGET SECUNDARIOS) #######
    def typeWidget(self, subWidget):
        # ESTA CONDICAO VERIFICA O TIPO DE WIDGET REQUERIDO
        if subWidget == 'text': # Neste caso "text" adiciona widget de caixa de texto \
                                    # no espaco reservado do layout
            self.subCellWid = Text(self.framePai4, width=34, height=4)
            self.subCellWid.insert(0.0, 'OBSERVACOES:') # textbox para observacoes
            # o widget gerado nesta condicao e adicionado ao container de widgets
            lay0 = Layout.creatLay( # Empacotando os widgets criados pela classe Layout
                    self.framePai4, self.celNomesL4, 
                    self.tipoWidget, subwidget=self.subCellWid)
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
            lay1 = Layout.creatLay(self.framePai4, self.celNomesL4, 
                          tWid=self.tipoWidget, subwidget=self.frmBtt)
            self.widgetPack.update(lay1)
        else: #por fim se nenhuma destes foi solicitado, o espaco reservado permanece vazio
             # Empacotando os widgets criados pela classe Layout
            lay2 = Layout.creatLay(self.framePai4, self.celNomesL4, 
                          tWid=self.tipoWidget)
            self.widgetPack.update(lay2)
        # por fim o configurador retorna os devidos widgets empacotados em self.widgetPack.
        return self.widgetPack


class Manipulador(Janela, subGrade, Layout):
    def __init__(self) -> None:
        super().__init__()
        # definindo o nome do banco de dados
        self.gerente = Gb( banco='dadosCobranca.db' )
        # criando a janela de cobrancas
        self.janelaCob = subGrade(self.widgets['Cobrancas'], 'label')
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
        if queryState != 'dados inseridos':
            warningWindow = showwarning(
                title="ATENÇÃO!", message=f'{queryState}', icon=WARNING)
            pass
        else:
            warningWindow = showinfo(title="TUDO OK", message=f'{queryState}')
        #PARA USAR OS DADOS DE ENTRADA DA GUI SUBSTITUIR (dictDados) POR (dictValues)
        #PARA USAR OS DADOS DE ENTRADA DE TESTE SUBSTITUIR (dictValues) POR (dictDados)
        