#importando a biblioteca tkinter 
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import crud
from tkinter import messagebox
import os
import sqlite3
import pandas as pd
from banco import deletar_form
from banco import inserir_dados
import banco




#cores 
cor_1 = "#F36F20" #laranja
cor_2 = "#00ABCC" #azul 
cor_3 = "#00C2C1" #azul claro 
cor_4 = "#E86B2F" #vermelho 
cor_5 = "#FFFFFF" #branca
cor_6 = "#0B1734" #azul escuro 
cor_7 = "#000000" #preto
cor_8 = "#e9edf5" #verde Claro

#janela Maior
root = Tk()
root.title("")
root.geometry("900x600") #largura x altura
root.configure(background= cor_3)  # background
root.resizable(width=False, height=False)

#estilo da janela
style = ttk.Style(root)
style.theme_use("clam")
#__________________________________janela maior até aqui





#linha superior 
FrameCima = Frame(root, width=1043, height=50, bg=cor_5, relief=FLAT) #Largura = width altura= height 
FrameCima.grid(row=0, column=0)
#linha Meio
FrameMeio = Frame(root, width=1043, height=303, pady=20, bg=cor_5, relief=FLAT)
FrameMeio.grid(row=1, column=0, pady=1 ,padx=0, sticky=NSEW)
#linha Baixo
FrameBaixo = Frame(root, width=1043, height=300, bg=cor_5,relief=FLAT)
FrameBaixo.grid(row=2, column=0, pady=0 ,padx=1, sticky=NSEW)



#abrindo imagem 
app_img = Image.open("image.png")
app_img = app_img.resize((120,60))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(FrameCima, image=app_img, text= "Controle de Estoque",width=900, compound=LEFT, relief= RAISED, anchor= NW, font=("Helvetica 25 bold"), bg=cor_5, fg= cor_7)
app_logo.place(x=0, y=0)

global tree

# Criando funções
# Adicione as variáveis globais para os widgets de entrada
global e_nome, e_local, e_descricao, e_serie, e_data_entrada, e_data_saida, e_codigo_barras, salvar

# Adicione a função inserir dados () para atualizar a Treeview


def inserir_dados(tree):
    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    serie = e_serie.get()
    data_entrada = e_data_entrada.get()
    data_saida = e_data_saida.get()
    codigo_barras = e_codigo_barras.get()

    
    # Verificar se algum campo está vazio
    if nome == '' or local == '' or descricao == '' or serie == '' or data_entrada == '' or data_saida == '' or codigo_barras== '':
        print("Preencha todos os itens")

    banco = sqlite3.connect('pydados.db')
    cursor = banco.cursor()

    # Inserindo os dados na tabela
    cursor.execute("INSERT INTO ener (nome, local, descricao, serie, data_entrada, data_saida, codigo_barras) VALUES (?, ?, ?, ?, ?, ?,?)", (nome, local, descricao, serie, data_entrada, data_saida, codigo_barras))

    # Exibindo todos os dados na tabela
    cursor.execute("SELECT * FROM ener")
    rows = cursor.fetchall()

    # Limpando a Treeview antes de inserir os novos dados
    tree.delete(*tree.get_children())

    # Inserindo os novos dados na Treeview
    for row in rows:
        tree.insert('', 'end', values=row)

    banco.commit()

    # Limpar os campos de entrada
    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_serie.delete(0, 'end')
    e_data_entrada.delete(0, 'end')
    e_data_saida.delete(0, 'end')
    e_codigo_barras.delete(0,'end')
    banco.close()
#___________________________________FUNÇÃO DELETAR ____________

# Alterações no botão de deletar
def deletar_form():
    try:
        # Obtendo o ID do item selecionado na Treeview
        tree_dados = tree.focus()
        # Obtendo os valores do item selecionado na Treeview
        tree_dicionario = tree.item(tree_dados)
        tree_lista = tree_dicionario['values']
        # Extrair o valor chave (ID) do primeiro elemento da lista de valores
        valor = tree_lista[0]

        # Conectando ao banco de dados
        banco = sqlite3.connect('pydados.db')
        cursor = banco.cursor()

        # Deletando o item do banco de dados
        cursor.execute("DELETE FROM ener WHERE id = ?", (valor,))
        
        # Deletando o item da Treeview
        tree.delete(tree_dados)

        # Confirmar a operação no banco de dados
        banco.commit()

        # Exibindo mensagem de sucesso
        messagebox.showinfo('Sucesso', 'O item foi deletado com sucesso.')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao tentar deletar o item: {e}')






# ler codigo de barras --------------------
def ler_barras():
    item_selecionado = tree.selection()
    if item_selecionado:
        # Obter os valores dos campos de entrada
        nome = e_nome.get()
        localidade = e_local.get()
        descricao = e_descricao.get()
        serie = e_serie.get()
        entrada = e_data_entrada.get()
        saida = e_data_saida.get()

        # Verificar se algum campo está preenchido
        if nome or localidade or descricao or serie or entrada or saida:
            # Atualizar o item selecionado na Treeview
            tree.item(item_selecionado, values=(nome, localidade, descricao, serie, entrada, saida))

            # Limpar os campos de entrada
            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_serie.delete(0, 'end')
            e_data_entrada.delete(0, 'end')
            e_data_saida.delete(0, 'end')

            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')
        else:
            messagebox.showerror('Erro', 'Preencha pelo menos um campo antes de atualizar.')
    else:
        messagebox.showerror('Erro', 'Selecione um item na tabela para atualizar.')








#frame meio
#criando entradas  nome/ localização/ descrição do item / numero de série/ data de entrada/ data de saída / codigo de barras 

#nome: 
l_nome = Label(FrameMeio, text= "Nome", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_nome.place(x=10, y=10)

e_nome = Entry(FrameMeio, width=30, justify="left", relief=SOLID)
e_nome.place(x=130, y=11)

#localização: 
l_local = Label(FrameMeio, text="Localização", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_local.place(x=10, y=40)

e_local = Entry(FrameMeio, width=30, justify="left", relief=SOLID)
e_local.place(x=130, y=41)

#descrição do item

#Descrição: 
l_descricao = Label(FrameMeio, text= "Descrição", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_descricao.place(x=10, y=70)

e_descricao = Entry(FrameMeio, width=30, justify="left", relief=SOLID)
e_descricao.place(x=130, y=71)

#NÚMERO DE SÉRIE
l_serie = Label(FrameMeio, text= "Número de série", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_serie.place(x=10, y=100)

e_serie = Entry(FrameMeio, width=30, justify="left", relief=SOLID)
e_serie.place(x=130, y=101)

#DATA DE ENTRADA 
l_data_entrada = Label(FrameMeio, text= "Data de Entrada", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_data_entrada.place(x=10, y=130)

e_data_entrada = DateEntry(FrameMeio, width=12, background= "darkblue", bordewidth=2,year=2022, locale='pt_BR')
e_data_entrada.place(x=130, y=131)

#DATA DE SAÍDA
l_data_saida = Label(FrameMeio, text= "Data de Saída", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_data_saida.place(x=10, y=160)

e_data_saida = DateEntry(FrameMeio, width=12,background= "darkblue", bordewidth=2,year=2022, locale='pt_BR')
e_data_saida.place(x=130, y=161)

#Codigo de Barras
l_barras = Label(FrameMeio, text="Código de barras", height=1, anchor=NW, font=("Ivy 10 bold"), bg=cor_5, fg=cor_7)
l_barras.place(x=10, y=190)

e_codigo_barras = Entry(FrameMeio, width=30, justify="left", relief=SOLID)
e_codigo_barras.place(x=130, y=191)

#Importar excel
l_carregar = Label(FrameMeio, text= "Importar Excel", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_carregar.place(x=10, y=220)

b_carregar = Button(FrameMeio, width=30, text= "Carregar".upper(),compound=CENTER, anchor=CENTER, overrelief=RIDGE, font= ("Ivy 8"), bg= cor_5, fg=cor_7)
b_carregar.place(x=130, y=221)

#----------------------------------------------------------------Criando Botões----------------------------

#Botão importar excell
l_carregar = Label(FrameMeio, text= "Importar Excel", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_carregar.place(x=10, y=220)

botao_carregar = Button(FrameMeio, compound=CENTER, anchor=CENTER, text="carregar".upper(),
width=30, overrelief=RIDGE, font=('ivy 8'),bg=cor_5, fg=cor_7)
botao_carregar.place(x=130, y=221)



#botão inserir 
img_add = Image.open("adc.png")
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)


b_inserir= Button(FrameMeio, image=img_add, width=95, text="  ADICIONAR".upper(), compound=LEFT, overrelief=RIDGE,
                   anchor=NW, font=("Helvetica 9 bold"), bg=cor_5, fg=cor_7, command=lambda:inserir_dados(tree))
b_inserir.place(x=330, y=10)



#botão barras
img_up = Image.open("barras.png")
img_up = img_up.resize((20,20))
img_up = ImageTk.PhotoImage(img_up)

b_atualizar = Button(FrameMeio, image=img_up, width=95, text="Ler código".upper(), compound=LEFT, overrelief=RIDGE,
                     anchor=NW, font=("Helvetica 9 bold"), bg=cor_5, fg=cor_7, command=ler_barras)
b_atualizar.place(x=330, y=110)


#botão DELETAR 
img_del = Image.open("deletar.png")
img_del = img_del.resize((20,20))
img_del = ImageTk.PhotoImage(img_del)

b_deletar = Button(FrameMeio, image=img_del, width=95, text="  DELETAR".upper(), compound=LEFT, overrelief=RIDGE,
                   anchor=NW, font=("Helvetica 9 bold"), bg=cor_5, fg=cor_7, command=deletar_form)
b_deletar.place(x=330, y=60)



#botão importar excell
img_past = Image.open("excell.png")
img_past = img_past.resize((20,21))
img_past = ImageTk.PhotoImage(img_past)

b_inserir = Button(FrameMeio, image= img_past, width=95, text= "  Importar".upper(), compound=LEFT, overrelief=RIDGE , anchor= NW, font=("Helvetica 9 bold"), bg=cor_5, fg= cor_7)
b_inserir.place(x=330, y=220)


#------------------------------------------------------------Labels Quantidade ---------------------------


l_qtd1 = Label(FrameMeio, text="", height=2, width=35, anchor=CENTER, font=("Ivy 10 bold"), bg=cor_2, fg=cor_7)
l_qtd1.place(x=540, y=25)

l_qtd2 = Label(FrameMeio, text="          Quantidade de itens     ", height=1, anchor=NW, font=("Ivy 15 bold"), bg=cor_2, fg=cor_5)
l_qtd2.place(x=540, y=20)


#---------------------------------                        criando tabela inferior
# Adicionando Scrollbars

# Inicializando a janela


root = Tk()

# Lista de itens e cabeçalhos da tabela
tabela_head = ['Número', 'Nome', 'Localização', 'Descrição', 'Número de série', 'Data de entrada', 'Data de saída', 'Código d/Barras']
lista_itens = []

# Criando a Treeview e os scrollbars

# Criando a Treeview e os scrollbars
tree = ttk.Treeview(FrameBaixo, selectmode="extended", columns=tabela_head, show="headings")
vsb = ttk.Scrollbar(FrameBaixo, orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(FrameBaixo, orient="horizontal", command=tree.xview)

# Configurando os scrollbars na Treeview
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

# Posicionando os widgets na tela
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

# Configurando pesos das linhas e colunas no grid
FrameBaixo.grid_rowconfigure(0, weight=1)
FrameBaixo.grid_columnconfigure(0, weight=1)
FrameBaixo.grid_rowconfigure(0, weight=12)

# Configurando cabeçalhos e largura das colunas
hd = ["center", "center", "center", "center", "center", "center", "center", "center"]
h = [40, 40, 60, 100, 130, 100, 100, 290]
n = 0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
# adjust the column's width to the header strin # Usando a lista de âncoras 'hd'
    tree.column(col, width=h[n], anchor=hd[n])
    n += 1




for item in lista_itens:

    tree.insert('', 'end', values=item)
quantidade = []
for id in lista_itens:
    quantidade.append(id[6])
id = len(quantidade)
l_qtd1['text'] = id


root.mainloop()