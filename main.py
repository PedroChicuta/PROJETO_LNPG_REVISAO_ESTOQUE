from tkinter import *
from tkinter import ttk
from datetime import date

# Variables
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500

"""

Desenvolver uma interface gráfica para o controle de estoque.
A interface deve ter campos para inserir nome do produto, quantidade em estoque,  preço unitário e um campo de seleção se o produto é gelado ou não.  Um botão para adicionar ao estoque e outro para limpar o formulário.
Implemente a validação para garantir que:
Todos os campos são obrigatórios;
A quantidade seja um número inteiro positivo
O preço seja um valor com ponto flutuante e maior que zero.
Os dados dos produtos devem ser armazenados em um arquivo chamado "estoque.txt", cada produto em uma linha no formato: Nome,Quantidade,Preco,Gelado.

"""
# function
def save_db(name, quantity, price, cold):
    with open("estoque.txt","a",encoding="utf-8") as file:
        file.write(f'{name},{quantity},{price},{cold}\n')


def submit(name, quantity, price, cold):
    name_value = name.get()
    quantity_value = quantity.get()
    price_value = price.get()
    cold_value = cold.get()
    save_db(name_value,quantity_value,price_value,cold_value)


# Window Config
root = Tk()
root.title("Controle de Estoque")
root.resizable(False, False)
root.attributes('-topmost', 0)
# Center window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (WINDOW_WIDTH/2))
y_cordinate = int((screen_height/2) - (WINDOW_HEIGHT/2))
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_cordinate}+{y_cordinate}")
# Theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

#variables
is_cold = StringVar()
is_cold.set('sim')


#Labels
product_name_label = ttk.Label(text="Nome do Produto")
product_name = ttk.Entry()
quantity_storage_label = ttk.Label(text="Quantidade")
quantity_storage = ttk.Entry()
price_label = ttk.Label(text="Preço")
price = ttk.Entry()
cold_label = ttk.Label(text="ta frio?")
radio_s = ttk.Radiobutton(text="Sim", variable=is_cold, value='sim')
radio_n = ttk.Radiobutton(text="Nao", variable=is_cold, value='nao')
btn_submit = ttk.Button(text="Cadastrar", command=lambda: submit(product_name,quantity_storage,price,is_cold))



product_name_label.pack()
product_name.pack()
quantity_storage_label.pack()
quantity_storage.pack()
price_label.pack()
price.pack()
cold_label.pack()
radio_s.pack()
radio_n.pack()
btn_submit.pack()
if __name__ == "__main__":
    root.mainloop()
