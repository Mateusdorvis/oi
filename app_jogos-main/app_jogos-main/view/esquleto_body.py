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
        self.card_()
        
        
    def card_(self):
        for x in range(6):
             CardFrame(self.root, 0, x)
        
    
        
    
    
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
        
        
    