from tkinter import Label, Entry, Frame, Widget


# ESTA CLASSE E RESPONSAVEL POR DISTRIBUIR O LAYOUT DINAMICAMENTE
class Layout:
    dictEntryWidget = dict()

    # define o tipo de widget para os dados como do tipo entrada
    @staticmethod
    def ret_entry(nome: str, pai: Widget):
        widget = Entry(  # configuracoes do Entry
                pai, width=16, relief='groove', name=nome)
        widget.grid(  # posicao de alocamento do widget na grade
                row=1, column=1, padx=2, pady=2, ipadx=2, ipady=2)
        return widget

    # define o tipo de widget para os dados como do tipo texto
    @staticmethod
    def ret_label(nome: str, pai: Widget, vtext: str):
        widget = Label(  # configuracoes do Label
                pai, font=("arial", 12), text=vtext, width=14,
                relief='groove', name=nome)
        widget.grid(  # posicao de alocamento na grade
                row=1, column=1, padx=2, pady=2, ipadx=2, ipady=2)
        return widget

    # cria um widget opcional (usado para preencher o espaco reservado)
    @staticmethod
    def sub_widget(sb_widget: Widget):
        sb_widget.pack(  # alocando o subwidget na grade
                side='right', expand=1, fill='both',
                padx=2, pady=2, ipadx=2, ipady=2)

    # cria o card a receber os widgets
    @staticmethod
    def creat_card(pai: Widget, desc: str):
        # container de disposicao da grade frm0
        label = Label(pai, text=desc.upper())
        label.pack()

    # cria uma tarja de descricao acima do card quando solicitado
    @staticmethod
    def desc_widget(pai: Widget, descricao: str):
        label_cobranca = Label(pai, text=descricao.upper(), anchor='center')
        label_cobranca.pack()

    # cria o texto a ser exibido ao lado do widget de dados
    @staticmethod
    def ret_static_var(pai: Widget, text_var: str):
        texto_statico = Label(  # configuracoes do Label
                pai, text=text_var, font=("arial", 12), width=20, relief='groove', anchor='ne')
        texto_statico.grid(  # posicao de alocamento do widget na grade
                row=1, column=0, padx=2, pady=2, ipadx=2, ipady=2)

    @staticmethod
    def creat_lay(
        pai: Widget,
        celulas: dict,
        type_wid: str,
        desc: str = None,
        subwidget: Widget = None,
        data: dict = None
    ) -> dict:

        data_frames = data
            
        #  percorre as celulas presentes no pacote
        for desc, celula in celulas.items():
            frm0 = Frame(pai, relief='flat', bd=2)
            Layout.creat_card(frm0, desc)
            # percorre os widgets presentes no pacote
            for widget in celula:
                # removendo caracteres desnecessarios
                nome = str(widget).replace('\t', '')
                if data_frames:
                    data_names = data_frames[nome]
                else:
                    data_names = ""
                frm1 = Frame(frm0, relief='groove')  # criando container da grade
                Layout.ret_static_var(frm1, str(widget).upper())
                # filtro de tipo de widget para Entry
                if type_wid == 'entry':
                    Layout.dictEntryWidget[f'{nome}'] = Layout.ret_entry(nome=nome, pai=frm1)
                else:  # filtro de tipo de widget para Label
                    Layout.dictEntryWidget[f'{nome}'] = Layout.ret_label(nome=nome, pai=frm1, vtext=data_names)
                frm1.pack(anchor='w', expand=1, fill='both')  # alocando do container da grade
            if subwidget:  # aqui sera alocado um subwidget caso for solicitado.
                Layout.sub_widget(subwidget)
            frm0.pack(side='left', expand=1, fill='both', padx=4, pady=4)
        # retorna os widgets configurados e enpacotados para uso
        return Layout.dictEntryWidget
    
    