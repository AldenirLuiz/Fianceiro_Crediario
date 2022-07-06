
from tkinter import *
from tkinter import ttk

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
        

class subGrade:
    def __init__(self, notebook, tWidget) -> None:
        self.message = 'Testando: Os alores \nForam Gravados com Sucesso!'
        self.tipoWidget = tWidget
        self.celNomesL0 = { # estes dicionarios predefinidos formam as celulas ou 'CARDS' dos widgets,
            'data da rota':['nome darota\t\t:', 'data da rota\t\t:'], 
            'retorno':['data para retorno\t:']}
        self.celNomesL1 = { # a posicao dos widgets depende da ordem dos itens
            'cobranca':['saldo cobrado\t:', 'repasse. cobrado\t:', 'total cobrado\t:'], 
            'capital de giro':['venda anterior\t:', 'devolucao de rua\t:', 'total vendido\t\t:']}
        self.celNomesL2 = { 
            'saldo devedor':['repasse novo\t\t:', 'repasse total\t\t:'], 
            'deposito':['compra deposito\t:', 'entrega deposito\t:']}
        self.celNomesL3 = {
            'fichas':['fichas novas\t\t:', 'fichas repasse\t\t:', 'fichas em branco\t:', 'total fichas\t\t:'], 
            'mercadoria na rua':['venda nova\t\t:', 'brindes\t\t\t:', 'vl fichas branco\t:', 'total na rua\t\t:']}
        self.celNomesL4 = {
            'despesas':['despesa rota\t\t:', 'despesa extra\t\t:']}
        # Frame data da rota e retorno
        self.framePai0 = Frame(notebook)
        Layout.dispense(self.framePai0, self.celNomesL0, self.tipoWidget, desc='dados da cobranca')
        self.framePai0.grid(row=0, column=0)
        # Frame dos cards cobranca e capitial se giro
        self.framePai0 = Frame(notebook)
        Layout.dispense(self.framePai0, self.celNomesL1, self.tipoWidget)
        self.framePai0.grid(row=1, column=0)
        # Frame dos cards dados da rota e capitial se giro
        self.framePai2 = Frame(notebook)
        Layout.dispense(self.framePai2, self.celNomesL2, self.tipoWidget)
        self.framePai2.grid(row=2, column=0)
        # Frame dos cards saldo devedor e deposito
        self.framePai3 = Frame(notebook)
        Layout.dispense(self.framePai3, self.celNomesL3, self.tipoWidget)
        self.framePai3.grid(row=3, column=0)
        # Frame dos cards fichas e mercadoria na rua
        self.framePai4 = Frame(notebook, relief='groove')
        self.framePai4.grid(row=4, column=0,)


    def typeWidget(self, subWidget):
        if subWidget == 'text':
            self.subCellWid = Text(self.framePai4, width=36, height=8)
            self.subCellWid.insert(0.0, 'OBSERVACOES:') # textbox para observacoes
            
            return Layout.dispense(self.framePai4, self.celNomesL4, self.tipoWidget, subwidget=self.subCellWid)
        elif subWidget == 'botao':
            self.frmBtt = Frame(self.framePai4)

            self.subCellWid = Label(self.frmBtt, text=self.message, fg='green', width=34, height=4)
            self.subCellWid.pack(expand='yes', fill='both', pady=4, ipadx=2, ipady=2)

            self.subButonWid0 = Button(self.frmBtt, text='Limpar Campos',bg='orange')
            self.subButonWid0.pack(side='left', pady=4, ipadx=2, ipady=2)

            self.subButonWid1 = Button(self.frmBtt, text='Cadastrar Valores',bg='green')
            self.subButonWid1.pack(side='right', pady=4, ipadx=2, ipady=2)
            
            return Layout.dispense(self.framePai4, self.celNomesL4, self.tipoWidget, subwidget=self.frmBtt)
        else:
            return Layout.dispense(self.framePai4, self.celNomesL4, self.tipoWidget)
        

class Layout:
    def dispense(pai, celulas, tWid, desc=None, subwidget=None):
        dictWidgets = dict()
        if desc:
            labelCobranca = Label(pai, text=desc.upper(), anchor='center')
            labelCobranca.pack()
        for desc, celula in celulas.items():
            frm0 = Frame(pai, relief='groove', bd=2)
            label = Label(frm0, text=desc.upper())
            label.pack()
            for widget in celula:
                frm1 = Frame(frm0)
                textoStatico = Label(frm1, text=widget.upper(),width=20, relief='flat')
                textoStatico.grid(row=1, column=0, padx=4, pady=4, ipadx=2, ipady=2)
                textoEntrada = tWid(frm1, text='000000',width=16, relief='groove')
                textoEntrada.grid(row=1, column=1, padx=4, pady=4, ipadx=2, ipady=2)
                dictWidgets[f'{tWid}{widget}'] = textoEntrada
                frm1.pack(anchor='w')
            if subwidget:
                subwidget.pack(side='right', expand='yes', fill='both', padx=4, pady=4, ipadx=2, ipady=2)
            frm0.pack(side='left', padx=4, pady=4, ipadx=2, ipady=2,anchor='n')
        return dictWidgets


class Manipulador(Janela):
    def __init__(self) -> None:
        super().__init__()
        self.janelaCob = subGrade(self.widgets['Cobrancas'], Label)
        self.valEntry = self.janelaCob.typeWidget('text')
        self.janelaCad = subGrade(self.widgets['Cadastros'], Entry)
        self.valEntry = self.janelaCad.typeWidget('botao')


if __name__ == '__main__':
    main = Manipulador()
    main.window.mainloop()