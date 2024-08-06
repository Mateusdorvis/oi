from tkinter import ttk
import tkinter as tk
from elementos_tkinter import Buttoncustomizado, Framecustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens
from images import CarregaImagens
class Header:
    pass

class Body:
    def __init__(self, root):
        self.root = root
        self.container_frame = Framecustomizado(self.root, bg='red', width=600, height=600)
        self.container_frame.grid_propagate(False)
        self.container_frame.grid(row=0, column=0)
        self.card_frame()
        
        
    def card_frame(self):
        self.card = Framecustomizado(self.container_frame, width=200, height=300, bg='blue')
        self.card.grid(row=0, column=0)
        self.img = CarregaImagens("imagens/bloons.jpg", self.card)
        self.img.aparecer_imagem(0,0)
        
    
    
class App:
    def __init__(self, root):
        self.root = root
        self.body()
    
    def body(self):
        self.body = Body(self.root)
        pass
    


root=  tk.Tk()
app = App(root)
root.mainloop()
        
        
    