import tkinter as tk

def ler_caracteres(event):
    texto = text.get(1.0, 22.0)
    print(f'O tem {len(texto)} caractere')
    label.config(text=f'O tem {len(texto)} caractere')

root = tk.Tk()
text = tk.Text(root)
label = tk.Label(root)
label.pack()
text.pack()
text.bind('<KeyRelease>', ler_caracteres)

root.mainloop()
