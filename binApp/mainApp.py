from tkinter import *
from tkinter import ttk
from binApp.mainLayout import Layout
import json
from binApp.manageDir import Diretorio as Dir


class Janela:

    def __init__(self) -> None:
        self.window = Tk()
        # self.window.geometry('560x600')
        self.window.anchor('center')
        self.window_root = Canvas(self.window)
        self.window_root.pack(expand=1, fill='both', anchor='center')
        self.window_root.configure(scrollregion=self.window_root.bbox("all"))

        self.noteBook = ttk.Notebook(self.window_root, padding=8)
        self.noteBook.pack(expand=1, fill='both', anchor='center')

        # widgets: este container guardara os frames do notebook para acesso posterior
        self.widgets = dict()  # acesesso: self.widgets['nome do widget']
        # noteNomes: lista os nomes para nomear as abas do notebook.
        self.noteNomes = ['Cobrancas', 'Rotas', 'Cadastros', 'Historico']
        self.functional_widgets = ['entrada', 'botao_entrada']
        # valEntrys: este container guardara as entrys para acesso posterior.
        self.valEntry = dict()
        # percorre os nomes predefinidos em noteNomes, cada nome sera uma aba
        for index in self.noteNomes:
            # cada aba recebera um frame, isso garante que novos widgets possam ser adicionados
            frm = Frame(self.noteBook, relief='flat')
            self.widgets[index] = frm  # adiciona o frame ao conteiner
            # cria a aba no notebook com o nome predefinido na lista de nomes
            self.noteBook.add(self.widgets[index], text=index)
            # text=index-> |index: nome predefinido na lista de nomes, \
            # a celula recebe a chave do widget como nome|


# ESTA CLASSE E RESPONSAVEL POR CRIAR UMA GRADE DINAMICA DE |FRAMES|WIDGETS|
class SubGrade:
    message = 'VERIFIQUE OS DADOS ANTES \nDE SALVAR.'

    def __init__(self, notebook, t_widget, dados=None) -> None:

        self.tipoWidget = t_widget
        self.widgetPack = dict()
        self.vtext = dados
        self.data_obj = ['Campina', 'Itaporanga']
        if dados:
            self.data_obj = dados.keys()
        self.view = ViewCard()

        # Frame dos cards
        self.framePai0 = Frame(notebook)
        self.get_table_names = Menu(self.framePai0, )
        # self.get_table_names.pack()
        self.widgetPack.update(self.create_card(self.framePai0, self.tipoWidget, dados))
        self.framePai0.grid(row=1, column=0)

        self.framePai4 = Frame(notebook, relief='groove')

        # OS WIDGETS DESTA FRAME SERAO POSTOS NA FUNCAO typeWidget
        self.framePai4.grid(row=4, column=0, )

    def create_card(self, container, widget_type, _data=None):
        dict_widgets = dict()
        for _card in self.view.layers_:
            frame = Frame(container)
            if _card != 'notebookNames':
                _temp: dict = self.view.ret_card(_card)
                frame.pack()
                dict_widgets.update(
                    Layout.creat_lay(
                        pai=frame,
                        celulas=_temp,
                        type_wid=widget_type,
                        desc=str(_card).lower(),
                        data=_data))

        return dict_widgets

    @staticmethod
    def create_button(container, text, ):
        button = Button(container, text=text, bg='orange')
        return button.pack(side='left', pady=2, ipadx=2, ipady=2)

    def type_widget(self, sub_widget):
        # ESTA CONDICAO VERIFICA O TIPO DE WIDGET REQUERIDO
        if sub_widget == 'text':
            return self.pack_widget(
                widgets=[
                    Text(self.framePai4, width=100, height=4),
                    Label(self.framePai4, text='OBSERVACOES:'),
                ]
            )

        elif sub_widget == 'botao':  # Neste caso "botao" adiciona os
            # botoes no espaco reservado do layout
            frm_btt = Frame(self.framePai4)
            self.pack_widget(
                widgets=[
                    Label(frm_btt, text=self.message, fg='green', width=34, height=4)],
                type='pack')

            self.widgetPack['btts'] = {
                'btt0': Button(
                    frm_btt, text='Limpar Campos', bg='orange'),
                'btt1': Button(
                    frm_btt, text='Cadastrar Valores', bg='green')}

            self.pack_widget(
                widgets=[
                    frm_btt,
                    self.widgetPack['btts']['btt0'],
                    self.widgetPack['btts']['btt1']
                ],
            )
            return self.widgetPack
            # Empacotando os widgets criados pela classe Layout

        else:  # por fim se nenhuma destes foi solicitado, o espaco reservado permanece vazio
            # Empacotando os widgets criados pela classe Layout
            lay2 = Layout.creat_lay(self.framePai4, self.view.ret_card("celNomesL4"),
                                    type_wid=self.tipoWidget)
            self.widgetPack.update(lay2)
        # por fim o configurador retorna os devidos widgets empacotados em self.widgetPack.
        return self.widgetPack

    @staticmethod
    def pack_widget(**kwargs):
        for widget in kwargs.get('widgets'):
            widget.pack(side='right', expand=1, fill='none', pady=2, padx=2, ipadx=2, ipady=2)


class ViewCard:
    json_file: str = f"{Dir()}/cellNames.json"
    with open(json_file, "r") as cell_names:
        layers = json.load(cell_names)

    def ret_card(self, card: str, celula: str = None) -> [dict, list]:
        if celula:
            return self.layers[card][celula]
        return self.layers[card]

    @property
    def layers_(self):
        return self.layers


if __name__ == "__main__":
    view = ViewCard()
    for _card_ in view.layers_:
        temp: dict = dict(view.ret_card(_card_))
        print(*temp.values())
