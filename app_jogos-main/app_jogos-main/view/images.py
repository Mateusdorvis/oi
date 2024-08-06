from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from elementos_tkinter import LabelImage
class CarregaImagens:
    def __init__(self, url_img, root):
        self.url_img = url_img
        self.root = root
        self.altura_padrao = 120
        self.largura_padrao = 120
        self.image = Image.open(self.url_img).resize((self.largura_padrao, self.altura_padrao))
        self.photo = ImageTk.PhotoImage(self.image)
    
    
    def aparecer_imagem(self, linha, coluna):
        self.carrega_img = LabelImage(self.root, self.photo)
        self.carrega_img.grid(row=linha, column=coluna)
        