import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk
from elementos_tkinter import JanelaPronta, LabelPronta, EntradaTexto, CriarMenus, CriarBotao, Entrada

#filhas da classe janela
class JanelaCadastro(JanelaPronta):
    def __init__(self, nome_da_janela ):
        super().__init__(nome_da_janela)
        self.principal.resizable(False, False)
        self.inicio_janela()
        self.iniciar_janela
        

    def inicio_janela(self):
        #titulo nome
        self.titulo_label_nome = LabelPronta(self.principal, text='Nome de usuário', font=('Impact',12))
        self.titulo_label_nome.posicao_grid_label(0,0, sticky='ew')
        #entrada nome
        self.label_nome_cad = LabelPronta(self.principal, text='Digite  seu nome de usuário para entrar no app : ')
        self.label_nome_cad.posicao_grid_label(1,0, pady=2, padx=2, sticky='ew')
        self.entrada_nome_cad = EntradaTexto(self.principal, width=25, height=0)
        self.entrada_nome_cad.posicao_grid_text(1,1, pady=5, padx=5)
        #criação de uma label que mostra status
        self.label_status_nome = LabelPronta(self.principal)
        self.label_status_nome.posicao_grid_label(2,0)
      
    


       # titulo data
        self.titulo_label_data = LabelPronta(self.principal, text='Data de nascimento', font=('Impact',12))
        self.titulo_label_data.posicao_grid_label(3,0, sticky='ew')
        #entrada data
        self.label_ano_entrada = LabelPronta(self.principal, text='Digite o ano que você nasceu :')
        self.label_ano_entrada.posicao_grid_label(4,0)
        self.ano_entrada = Entrada(self.principal)
        self.ano_entrada.posicao_grid_entry(4,1)
        #config colunas 
        self.principal.grid_columnconfigure(0, weight=0)
        self.principal.grid_columnconfigure(1, weight=0)
        

        
        
       
       
        #verifica condição nome
        def verificar_entrada_nome(event):
            pegue_nome =self.entrada_nome_cad.get(1.0, tk.END).strip()
            numero_de_caracteres = len(pegue_nome)
            
            if numero_de_caracteres<=1:
                self.label_status_nome.config(text=f'Tem {numero_de_caracteres} caractere. Por favor escreva mais !', fg='red')
                  
            elif numero_de_caracteres<=12:
                self.label_status_nome.config(text=f'Tem {numero_de_caracteres} caracteres. Por favor escreva mais ! ', fg='red')
                
            
            elif  13<= numero_de_caracteres <=20:
                self.label_status_nome.config(text=f'Número de caracteres no mínimo, pois tem {numero_de_caracteres} caracteres !', fg='green')
                
            else:
                 self.label_status_nome.config(text=f' Número de caracteres no máximo! Pois tem {numero_de_caracteres} caracteres. ', fg='red')
                 self.entrada_nome_cad.config(state='disabled')
                 pergunta = messagebox.askyesno('Pergunta', 'Deseja resetar a entrada ?')
                 if pergunta:
                    self.entrada_nome_cad.config(state='normal')
                    self.label_status_nome.config(text='')
                    self.entrada_nome_cad.delete(1.0, tk.END).strip()
        #tecla solta do nome
        self.entrada_nome_cad.bind('<KeyRelease>', verificar_entrada_nome)
        #verifica a entrada data
        


                
        
        
        
        
        

class JanelaLogin(JanelaPronta):
    def __init__(self, nome_da_janela):
        super().__init__(nome_da_janela)
        self.principal.resizable(False, False)
        self.inicio_login()
        self.iniciar_janela
    
    def inicio_login(self):
       pass
    
      
                
        
        
