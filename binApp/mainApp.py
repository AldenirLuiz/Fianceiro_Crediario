from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, WARNING, showwarning
from binApp.manageBd import Gerente as Gb



######SIMULACAO DE UMA ENTRADA DE DADOS PADRAO#######
dictDados = {
    'nome da rota:': 'Campina', 
    'data da rota:': '21072022', 
    'dataretorno': '21032022',
    'valcobrado': '10000', 
    'repcobrado': '1000', 
    'totcobrado': '11000',
    'repnovo': '1000', 
    'reptotal': '2000', 
    'fxnova': '40',
    'fxbranco': '1', 
    'fxrepasse': '2', 
    'fxtotal': '43',
    'vndanterior': '30000', 
    'devrua': '10000', 
    'totvendido': '20000',
    'cmpdeposito': '30000', 
    'entdeposito': '10000', 
    'vndnova': '30000',
    'brindes': '1000', 
    'flfxbranco': '1000', 
    'totrua': '31000',
    'desprota': '1000', 
    'dspextra': '1000'}
########################<---->########################

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
        # valEntrys: este container guardara os as entrys para acesso posterior.
        self.valEntry = dict()
        # percorre os nomes predefinidos em noteNomes, cada nome sera uma aba
        for index in self.noteNomes:
            # cada aba recebera um frame, isso garante que novos widgets possam ser adicionados
            frm = Frame(self.noteBook, relief='flat')
            self.widgets[index] = frm # adiciona o frame ao conteiner
            # cria a aba no notebook com o nome predefinido na lista de nomes
            self.noteBook.add(self.widgets[index], text=index) # text=index> index: nome predefinido na lista de nomes
        
####### ESTA CLASSE E RESPONSAVEL POR CRIAR UMA GRADE DINAMICA DE |FRAMES|WIDGETS| ####### 
class subGrade:
    def __init__(self, notebook, tWidget) -> None:
        self.message = 'Testando: Os alores \nForam Gravados com Sucesso!'
        self.tipoWidget = tWidget
        self.widgetPack = dict()

        self.celNomesL0 = { # estes dicionarios predefinidos formam as celulas ou 'CARDS' dos widgets,
            'data da rota':['nome da rota\t\t:', 'data da rota\t\t:'], 
            'retorno':['data para retorno\t:']}
        self.celNomesL1 = { # a posicao dos widgets depende da ordem dos itens
            'cobranca':['saldo cobrado\t:', 'repasse cobrado\t:', 'total cobrado\t:'], 
            'capital de giro':['venda anterior\t:', 'devolucao de rua\t:', 'total vendido\t\t:']}
        self.celNomesL2 = { # a distribuicao dos cards se faz por meio das chaves
            'saldo devedor':['repasse novo\t\t:', 'repasse total\t\t:'], 
            'deposito':['compra deposito\t:', 'entrega deposito\t:']}
        self.celNomesL3 = { # cada lista como [valor] contem os nomes dos widgets a serem criados.
            'fichas':['fichas novas\t\t:', 'fichas  repasse\t\t:', 'fichas em branco\t:', 'total fichas\t\t:'], 
            'mercadoria na rua':['venda nova\t\t:', 'brindes\t\t\t:', 'vl fichas branco\t:', 'total na rua\t\t:']}
        self.celNomesL4 = {
            'despesas':['despesa rota\t\t:', 'despesa extra\t\t:']}

    ####################### |CARDS DO LAYOUT| #######################
        # Frame data da rota e retorno
        self.framePai0 = Frame(notebook)
        self.widgetPack.update(Layout.dispense(self, pai=self.framePai0, celulas=self.celNomesL0, tWid=self.tipoWidget, desc='dados da cobranca'))
        self.framePai0.grid(row=0, column=0)

        # Frame dos cards cobranca e capitial se giro
        self.framePai0 = Frame(notebook)
        self.widgetPack.update(Layout.dispense(self, self.framePai0, self.celNomesL1, self.tipoWidget))
        self.framePai0.grid(row=1, column=0)

        # Frame dos cards dados da rota e capitial se giro
        self.framePai2 = Frame(notebook)
        self.widgetPack.update(Layout.dispense(self, self.framePai2, self.celNomesL2, self.tipoWidget))
        self.framePai2.grid(row=2, column=0)

        # Frame dos cards saldo devedor e deposito
        self.framePai3 = Frame(notebook)
        self.widgetPack.update(Layout.dispense(self, self.framePai3, self.celNomesL3, self.tipoWidget))
        self.framePai3.grid(row=3, column=0)

        # Frame dos cards fichas e mercadoria na rua
        self.framePai4 = Frame(notebook, relief='groove')
        # OS WIDGETS DESTA FRAME SERAO POSTOS NA FUNCAO typeWidget
        self.framePai4.grid(row=4, column=0,) 

    #######CONFIGURACOES DA GRADE DO LAYOUT (TIPOS DE WIDGET SECUNDARIOS)#######
    def typeWidget(self, subWidget):

        # ESTA CONDICAO VERIFICA O TIPO DE WIDGET REQUERIDO
        if subWidget == 'text': # Neste caso "text" adiciona widget de caixa de texto no espaco reservado do layout
            self.subCellWid = Text(self.framePai4, width=36, height=8)
            self.subCellWid.insert(0.0, 'OBSERVACOES:') # textbox para observacoes
            
            self.widgetPack.update(Layout.dispense(self, self.framePai4, self.celNomesL4, self.tipoWidget, subwidget=self.subCellWid))
        
        elif subWidget == 'botao':
            self.frmBtt = Frame(self.framePai4)

            self.subCellWid = Label(self.frmBtt, text=self.message, fg='green', width=34, height=4)
            self.subCellWid.pack(expand='yes', fill='both', pady=2, ipadx=2, ipady=2)

            self.subButonWid0 = Button(self.frmBtt, text='Limpar Campos',bg='orange')
            self.subButonWid0.pack(side='left', pady=2, ipadx=2, ipady=2)

            self.subButonWid1 = Button(self.frmBtt, text='Cadastrar Valores',bg='green')
            self.subButonWid1.pack(side='right', pady=2, ipadx=2, ipady=2)

            self.widgetPack['btts'] = {'btt1': self.subButonWid1, 'btt0' : self.subButonWid0}
            self.widgetPack.update(Layout.dispense(self, self.framePai4, self.celNomesL4, tWid=self.tipoWidget, subwidget=self.frmBtt))
        else:
            self.widgetPack.update(Layout.dispense(self, self.framePai4, self.celNomesL4, tWid=self.tipoWidget))
        
        return self.widgetPack


class Layout:

    @staticmethod
    def dispense(self, pai, celulas, tWid, desc=None, subwidget=None):

        dictEntryWidget = dict()

        if desc:
            labelCobranca = Label(pai, text=desc.upper(), anchor='center')
            labelCobranca.pack()

        for desc, celula in celulas.items():
            frm0 = Frame(pai, relief='groove', bd=2)

            label = Label(frm0, text=desc.upper())
            label.pack()

            for widget in celula:
                nome = str(widget).replace('\t', '')

                frm1 = Frame(frm0)

                textoStatico = Label(frm1, text=widget.upper(),width=20, relief='flat')
                textoStatico.grid(row=1, column=0, padx=2, pady=2, ipadx=2, ipady=2)

                if tWid == 'entry':
                    widget = Entry(frm1, width=16, relief='groove', name=nome)
                    widget.grid(row=1, column=1, padx=2, pady=2, ipadx=2, ipady=2)

                    dictEntryWidget[f'{nome}'] = widget
                    
                else:
                    widget = Label(frm1, text='100000',width=16, relief='groove', name=nome)
                    widget.grid(row=1, column=1, padx=2, pady=2, ipadx=2, ipady=2)

                    dictEntryWidget[f'{nome}'] = widget
                    
                frm1.pack(anchor='w')

            if subwidget:
                subwidget.pack(side='right', expand='yes', fill='both', padx=2, pady=2, ipadx=2, ipady=2)
            
            frm0.pack(side='left', padx=2, pady=2, ipadx=2, ipady=2,anchor='n')

        return dictEntryWidget


class Manipulador(Janela, subGrade, Layout):
    def __init__(self) -> None:
        super().__init__()

        self.gerente = Gb( banco='dadosCobranca.db' )
        self.janelaCob = subGrade(self.widgets['Cobrancas'], 'label')
        self.valText = self.janelaCob.typeWidget('text')

        self.janelaCad = subGrade(self.widgets['Cadastros'], 'entry')
        self.valEntry = self.janelaCad.typeWidget('botao')
        
        self.valEntry['btts']['btt1'].configure(command=lambda: self.comander('add'))
        self.valEntry['btts']['btt0'].configure(command=lambda: self.comander('delete'))
        
    def comander(self, command) -> None:
        dictValues = dict()

        if command == 'delete':
            for keyWidget in self.valEntry.keys():
                if keyWidget != 'btts':
                    self.valEntry[keyWidget].delete(0, END)
                else: continue
        else:
            for keyWidget in self.valEntry.keys():
                if keyWidget != 'btts':
                    widgetText = self.valEntry[keyWidget].get()
                    dictValues[keyWidget] = widgetText
                else: continue
        
        queryState = self.gerente.gerenteBd( dados=dictValues, query='add' )
        if queryState != 'dados inseridos':
            warningWindow = showwarning(title="ATENÇÃO!", message=f'{queryState}', icon=WARNING)
            pass
        else:
            warningWindow = showinfo(title="TUDO OK", message=f'{queryState}')
        #PARA USAR OS DADOS DE ENTRADA DA GUI SUBSTITUIR (dictDados) POR (dictValues)
        
