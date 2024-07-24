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
        self.label_nome_cad = LabelPronta(self.principal, text='Insira seu nome : ')
        self.label_nome_cad.configgrid_label(1,0, pady=5, padx=5)
        
        self.entrada_nome_cad = EntradaTexto(self.principal, width=50, height=0)
        self.entrada_nome_cad.configgrid_text(1,1, pady=5, padx=5)

        self.label_data_de_nascimento_cad = LabelPronta(self.principal, text='Insira sua data de nascimento por completo ex: 12/07/2007 :')
        self.label_data_de_nascimento_cad.configgrid_label(5,0, pady=5, padx=5)
        
        self.entrada_data_cad = EntradaTexto(self.principal, width=20, height=0)
        self.entrada_data_cad.configgrid_text(5,1, pady=5, padx=5)
        
        
        #verifica condição nome
        def verificar_entrada_nome(event):
            label_mensagem_nome = LabelPronta(self.principal)
            label_mensagem_nome.configgrid_label(3,0)
            
            pegue_nome =self.entrada_nome_cad.get(1.0, tk.END)
            numero_de_caracteres = len(pegue_nome)
            
            if numero_de_caracteres==1:
                label_mensagem_nome.config(text='Tem um caractere. Por favor escreva mais !')
                
            elif numero_de_caracteres<=12:
                label_mensagem_nome.config(text=f'Tem {numero_de_caracteres} caracteres. Por favor escreva mais ! ')
            
            elif numero_de_caracteres>=13 and numero_de_caracteres<=100:
                label_mensagem_nome.config(text=f'Seu nome passou de {numero_de_caracteres} caracteres, já está no número de caractere mínimo !')
                
            else:
                 label_mensagem_nome.config(text=f'Seu nome passou de {numero_de_caracteres} caracteres, já está no número de caractere máximo!')
                 self.entrada_nome_cad.config(state='disabled')
                
                
        self.entrada_nome_cad.bind('<KeyRelease>', verificar_entrada_nome)
        
        #verifica condição data 
        def verificar_entrada_nome(event):
            label_mensagem_data = LabelPronta(self.principal)
            label_mensagem_data.configgrid_label(3,0)
            
            pegue_data =self.entrada_data_cad.get(1.0, tk.END)
            numero_de_caracteres = len(pegue_data)
            
            try:
                if isinstance(numero_de_caracteres):
                  label_mensagem_data.config(text='Tem um caractere. Por favor Insira mais !')
                
                elif numero_de_caracteres<=12:
                    label_mensagem_data.config(text=f'Tem {numero_de_caracteres} caracteres. Por favor escreva mais ! ')
                
                elif numero_de_caracteres>=13 and numero_de_caracteres<=100:
                    label_mensagem_data.config(text=f'Seu nome passou de {numero_de_caracteres} caracteres, já está no número de caractere mínimo !')
                    
                else:
                    label_mensagem_data.config(text=f'Seu nome passou de {numero_de_caracteres} caracteres, já está no número de caractere máximo!')
                    self.entrada_nome_cad.config(state='disabled')
            except:
                 label_mensagem_data.config(text='Este caractere não é número')
            
            
                
                
        self.entrada_nome_cad.bind('<KeyRelease>', verificar_entrada_nome)
        

        
        

class JanelaLogin(JanelaPronta):
    def __init__(self, nome_da_janela):
        super().__init__(nome_da_janela)
        self.principal.resizable(False, False)
        self.inicio_login()
        self.iniciar_janela
    
    def inicio_login(self):
       
            
        #nome
        self.label_nome_login = LabelPronta(self.principal, text='Digite nome cadastrado')
        self.label_nome_login.configgrid_label(1,0, pady=5, padx=5)
        self.entrada_nome_login = EntradaTexto(self.principal, width=20, height=0)
        self.entrada_nome_login.configgrid_text(1,1,  pady=5, padx=5)
        #senha
        self.label_senha_login = LabelPronta(self.principal, text='Digite nome cadastrado')
        self.label_senha_login.configgrid_label(4,0, pady=5, padx=5)
        self.entrada_senha_login = EntradaTexto(self.principal, width=20, height=0)
        self.entrada_senha_login.configgrid_text(4,1,  pady=5, padx=5)
        #verifica condição
      
                
        
        
