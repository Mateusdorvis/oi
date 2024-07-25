import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#objeto menu
class CriarMenus(tk.Menu):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
    
    

    def adiciona_menu_na_barra(self,nome_menu, menu_pai : tk.Menu, menu_fllho : tk.Menu):
        menu_pai.add_cascade(label=nome_menu, menu=menu_fllho)

    def adiciona_comando_no_menu(self,menu_que_add_comando : tk.Menu,elementos_do_menu):
        for elements in elementos_do_menu:
            menu_que_add_comando.add_command(label= elements ['label'], command= elements['command'])
#objeto botao
class CriarBotao(tk.Button):
      def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.posicao_grid_button
    
      def posicao_grid_button(self,linha_grid, coluna_grid, **args):
        self.grid(row=linha_grid, column=coluna_grid, **args)

#obejto label
class LabelPronta(tk.Label):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.posicao_grid_label

    def posicao_grid_label(self,linha_label, coluna_label, **args):
        self.grid(row=linha_label, column=coluna_label, **args)

class EntradaTexto(tk.Text):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.posicao_grid_text

    def posicao_grid_text(self,linha_text, coluna_text, **args):
        self.grid(row=linha_text, column=coluna_text, **args)

class Entrada(tk.Entry):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.posicao_grid_entry

    def posicao_grid_entry(self,linha_entry, coluna_entry, **args):
        self.grid(row=linha_entry, column=coluna_entry, **args)
        
#objeto janela     
class JanelaPronta:
    def __init__(self, nome_da_janela ):
        self.nome_da_janela = nome_da_janela
        self.principal = tk.Tk()
        self.contar_click = 0
        self.iniciar_janela
        self.principal.title(self.nome_da_janela)
    
    def iniciar_janela(self):
        self.principal.mainloop()

