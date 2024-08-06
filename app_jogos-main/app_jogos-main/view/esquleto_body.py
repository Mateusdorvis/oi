from tkinter import ttk
import tkinter as tk
from elementos_tkinter import Buttoncustomizado, Framecustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens
class Header:
    pass

class Body:
    def __init__(self, root):
        self.root = root
        self.container_frame = Framecustomizado(self.root, bg='red', width=600, height=600)
        self.container_frame.grid_propagate(False)
        self.container_frame.grid(row=0, column=0)
        
        
    def card_frame(self):
        self.card = Framecustomizado(self.container_frame)
        self.card.grid(row=0, column=0)
        
    
    
class App:
    def __init__(self, root):
        self.root = root
        self.body()
    
    def body(self):
        pass
        
        
        
    