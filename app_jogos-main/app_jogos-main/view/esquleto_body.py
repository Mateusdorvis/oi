from tkinter import ttk
import tkinter as tk
from elementos_tkinter import Buttoncustomizado, Framecustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens

class Header:
    pass

class CardFrame:
    def __init__(self, frame, linha_card, coluna_card):
        self.frame = frame
        self.card_box = Framecustomizado(self.frame, width=200, height=300, bg='blue')
        self.card_box.grid(row=linha_card, column=coluna_card, pady=5, padx=5)
class Body:
    def __init__(self, root):
        self.root = root
        self.container_frame = Framecustomizado(self.root, bg='red', width=600, height=600)
        self.container_frame.grid_propagate(False)
        self.container_frame.grid(row=0, column=0)
        self.card_frame()
        
        
    def card_frame(self):
        CardFrame(self.container_frame, 0, 0)
        CardFrame(self.container_frame, 0, 1)
        CardFrame(self.container_frame, 0, 2)
        pass
    
        
    
    
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
        
        
    