from tkinter import ttk
import tkinter as tk
from elementos_tkinter import Buttoncustomizado, Framecustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Canvaspersonalizado
from PIL import Image, ImageTk
class CarregaImagens:
    def __init__(self, url_img, root):
        self.url_img = url_img
        self.root = root
        self.altura_padrao = 200
        self.largura_padrao = 200
        self.image = Image.open(self.url_img).resize((self.largura_padrao, self.altura_padrao))
        self.photo = ImageTk.PhotoImage(self.image)
    
    
    def aparecer_imagem(self):
        self.carrega_img = tk.Label(self.root, image=self.photo, bg='blue')
        self.carrega_img.image = self.photo
        self.carrega_img.grid(row=0, column=0)
        

        



class Card:
    def __init__(self, root, linha_card, coluna_card, img_card):
        self.root = root
        self.img_card = img_card
        self.card_box = Canvaspersonalizado(self.root, width=200, height=300, bg='blue')
        self.card_box.grid_propagate(False)
        self.card_box.grid(row=linha_card, column=coluna_card, pady=5, padx=5)
       
        self.img_()
    
        
    
    #metodos de card:
    def img_(self):
        self.img = CarregaImagens(self.img_card, self.card_box)
        self.img.aparecer_imagem()
    
        
        
class Container:
    def __init__(self, root):
        self.root = root
        self.canvas_box = Canvaspersonalizado(self.root, width=1000, height=320, bg='green')
        self.canvas_box.grid_propagate(False)
        self.canvas_box.grid(row=1, column=0)
        self.card_()
        
        
    def card_(self):
        self.card = Card(self.canvas_box, 0, 0, 'C:/Users/182400253/Downloads/Mateus da silva dorvis/oi/oi/app_jogos-main/app_jogos-main/imagens/terra.jpg')
        self.card2 = Card(self.canvas_box, 0, 1, 'C:/Users/182400253/Downloads/Mateus da silva dorvis/oi/oi/app_jogos-main/app_jogos-main/imagens/terra.jpg')
        
        
    

        
    
        
    
    
class App:
    def __init__(self, root):
        self.root = root
        self.box()
    
    def box(self):
        self.container = Container(self.root)
        
        
    


root=  tk.Tk()
app = App(root)
root.mainloop()
        
        
    