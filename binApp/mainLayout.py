from tkinter import Label, Entry, Frame

### ESTA CLASSE E RESPONSAVEL POR DISTRIBUIR O LAYOUT DINAMICAMENTE ###
class Layout:
    dictEntryWidget = dict()
    # define o tipo de widget para os dados como do tipo entrada
    def retEntry( nome, pai ):
        widget = Entry( # configuracoes do Entry
                pai, width=16, relief='groove', name=nome)
        widget.grid( # posicao de alocamento do widget na grade
                row=1, column=1, padx=2, pady=2, ipadx=2, ipady=2)
        return widget
    # define o tipo de widget para os dados como do tipo texto
    def retLabel( nome, pai):
        widget = Label( # configuracoes do Label
                pai, text='100000',width=16, 
                relief='groove', name=nome)
        widget.grid( # posicao de alocamento na grade
                row=1, column=1, padx=2, pady=2, ipadx=2, ipady=2)
        return widget
    # cria um widget opcional (usado para preencher o espaco reservado)
    def subWidget( sbWidget):
        sbWidget.pack( # alocando o subwidget na grade
                side='right', expand='yes', fill='both', 
                padx=2, pady=2, ipadx=2, ipady=2)
    # cria o card a receber os widgets
    def creatCard( pai, desc ):
        # container de disposicao da grade frm0
        label = Label(pai, text=desc.upper())
        label.pack() # esta Label descreve o card
    # cria uma tarja de descricao acima do card quando solicitado   
    def descWidget( pai, descricao ):
        labelCobranca = Label(pai, text=descricao.upper(), anchor='center')
        labelCobranca.pack()
    # cria o texto a ser exibido ao lado do widget de dados
    def retStaticVar( pai, textVar):
        textoStatico = Label( # configuracoes do Label
                pai, text=textVar,width=20, relief='flat')
        textoStatico.grid( # posicao de alocamento do widget na grade
                row=1, column=0, padx=2, pady=2, ipadx=2, ipady=2)
    
    def creatLay(pai, celulas, tWid, desc=None, subwidget=None) -> dict:
        # percorre as celulas presentes no pacote
        for desc, celula in celulas.items():
            frm0 = Frame(pai, relief='groove', bd=2)
            Layout.creatCard(frm0, desc)
            # percorre os widgets presentes no pacote
            for widget in celula:
                # removendo caracteres desnecessarios
                nome = str(widget).replace('\t', '')
                frm1 = Frame(frm0) # criando container da grade
                Layout.retStaticVar(frm1, widget.upper())
                # filtro de tipo de widget para Entry
                if tWid == 'entry':
                    Layout.dictEntryWidget[f'{nome}'] = Layout.retEntry( nome=nome, pai=frm1 )
                else: # filtro de tipo de widget para Label
                    Layout.dictEntryWidget[f'{nome}'] = Layout.retLabel( nome=nome, pai=frm1 )
                frm1.pack(anchor='w', expand='yes', fill='both') # alocando do container da grade
            if subwidget: # aqui sera alocado um subwidget caso for solicitado.
                Layout.subWidget( subwidget )
            frm0.pack(side='left', expand='yes', fill='both')
        # retorna os widgets configurados e enpacotados para uso
        return Layout.dictEntryWidget
    
    