import tkinter as tk
from tkinter import ttk
from login import JanelaCadastro, JanelaLogin
from tkinter import messagebox
from elementos_tkinter import JanelaPronta, LabelPronta, EntradaTexto, CriarMenus


class JanelaPrincipal(JanelaPronta):
  def __init__(self,nome_da_janela):
        super().__init__(nome_da_janela)
        self.menu_inicio()
        self.iniciar_janela()
  
  def menu_inicio(self):
    #funcões para abrir outras janelas
    #janela cadastro
    def abrir_janela_cadastro():
      self.janela_cadastro = JanelaCadastro('Novo cadastro')
    #janela login
    def abrir_janela_login():
      self.janela_login = JanelaLogin('Entrar')
    #criação da barra
    self.menu_bar = CriarMenus(self.principal, tearoff=0)
    self.principal.config(menu=self.menu_bar)
 
    def Sair():
      resposta = messagebox.askyesno('Fechar o aplicativo', 'Deseja sair do aplicativo?')
      if resposta:
           self.principal.quit()
           
    #menu configurações
    self.menu_configuracao = [{'label': 'Sair', 'command' : Sair}]
    self.submenu_opcao = CriarMenus(self.menu_bar, tearoff=0)

    self.submenu_opcao.adiciona_comando_no_menu(self.submenu_opcao,self.menu_configuracao)
    self.menu_bar.adiciona_menu_na_barra('Configurações',self.menu_bar,self.submenu_opcao )
    
    #submenu opções alterar cor
    def alterarCor(cor):
      self.principal.config(bg=cor)
      
    self.cores_disponievis = [
      {'label': 'Azul', 'command' : lambda :  alterarCor('blue')},
      {'label': 'Amarelo', 'command' : lambda :  alterarCor('#E6D130')}, 
      {'label': 'Laranja', 'command' : lambda :  alterarCor('#E58E00')}, 
       {'label': 'Normal', 'command' : lambda :  alterarCor('white')}, 
      {'label': 'Preto', 'command' : lambda :  alterarCor('black')}, 
      {'label': 'Verde', 'command' : lambda :  alterarCor('#7DE657')},
      {'label': 'Vermelho', 'command' : lambda :  alterarCor('#E6412A')}
      
      ]
    self.background = CriarMenus(self.submenu_opcao, tearoff=0)
    #adicona comandos no submenu Mudar de cor
    self.submenu_opcao.adiciona_comando_no_menu(self.background, self.cores_disponievis)
    #adcionar no menu opcao
    self.submenu_opcao.adiciona_menu_na_barra('Mudar cor de fundo para...', self.submenu_opcao, self.background)
    
    #menu login
    self.menu_login = [
      {'label': 'Reallizar novo cadastro', 'command' : abrir_janela_cadastro},
      {'label': 'Entrar', 'command' : abrir_janela_login}
                       ]
    self.submenu_login = CriarMenus(self.menu_bar, tearoff=0)

    self.submenu_login.adiciona_comando_no_menu(self.submenu_login,self.menu_login)

    self.menu_bar.adiciona_menu_na_barra('Login',self.menu_bar,self.submenu_login )







  
  






    
  