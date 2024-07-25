from datetime import date
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

label = tk.Label(root, text='Escreva sua idade :')
label.pack()

entrada_data_ano = tk.Entry()
entrada_data_ano.pack()


def pegue_o_texto():
  

    ano_str = str(entrada_data_ano.get())

    if ano_str.isdigit():
        ano_entry = int(ano_str)

    else:
         messagebox.showinfo('Informação', 'Digite um número')
    #data = date(ano_entry,mes_entry,dia_entry)
    #formato = '%d / %m / %Y'
    #data_formatada = data.strftime(formato)
   
    ano_atual = datetime.now().year
    if ano_entry > ano_atual:
        mostra_idade =  ano_entry - ano_atual
        if mostra_idade>=18:

            label.config(text=f'Você é maior de idade , pois tem {mostra_idade} anos')

        elif mostra_idade<=1:
              label.config(text=f'Você é menor de idade , pois tem {mostra_idade} ano')

            
        else:
            label.config(text=f'Você é menor de idade , pois tem {mostra_idade}')
      


    else:
        mostra_idade = ano_atual - ano_entry
        if mostra_idade>=18:
            label.config(text=f'Você é maior de idade , pois tem {mostra_idade} anos')
        
        elif mostra_idade<=1:
              label.config(text=f'Você é menor de idade , pois tem {mostra_idade} ano')

        else:
            label.config(text=f'Você é menor de idade , pois tem {mostra_idade} anos')

button = tk.Button(root, text='Enviar', command=pegue_o_texto)
button.pack()

root.mainloop()