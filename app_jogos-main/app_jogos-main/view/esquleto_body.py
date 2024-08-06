from tkinter import ttk
import tkinter as tk
from elementos_tkinter import Buttoncustomizado, Framecustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens

class Header:
    pass

class CardFrame:
    def __init__(self, frame):
        self.frame = frame
    
    def card(self):
        self.card = Framecustomizado(self.frame, width=200, height=300, bg='blue')
        self.card.grid(row=0, column=0, pady=5, padx=5)
class Body:
    def __init__(self, root):
        self.root = root
        self.container_frame = Framecustomizado(self.root, bg='red', width=600, height=600)
        self.container_frame.grid_propagate(False)
        self.container_frame.grid(row=0, column=0)
        self.card_frame1()
        
        
    def card_frame1(self):
        self.oi = CardFrame(self.container_frame)
        self.oi2 = CardFrame(self.container_frame)
        pass
    
    def card_frame1(self):
        self.oi = CardFrame(self.container_frame)
        self.oi2 = CardFrame(self.container_frame)
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
        
        
    