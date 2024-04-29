from datetime import datetime
import sqlite3
from PyQt5 import QtWidgets, uic


# Função para inserir um novo item no banco de dados
def inserir(nome, localizacao, descricao, serie, entrada, saida, codigo_barras):
    conn = sqlite3.connect('pydados.db')
    cursor = conn.cursor()
    query = "INSERT INTO ener(nome, localizacao, descricao, serie, entrada, saida, codigo_barras) VALUES (?,?,?,?,?,?,?)"
    cursor.execute(query, (nome, localizacao, descricao, serie, entrada, saida, codigo_barras))
    conn.commit()
    conn.close()


    # Função para deletar um item do banco de dados
def deletar_dados(nome, localizacao, descricao, serie, entrada, saida, codigo_barras):
    try:
        conn = sqlite3.connect('pydados.db')
        cursor = conn.cursor()
        query = "DELETE FROM ener WHERE nome = ? AND localizacao = ? AND descricao = ? AND serie = ? AND data_entrada = ? AND data_saida = ? AND codigo_barras = ?"
        cursor.execute(query, (nome, localizacao, descricao, serie, entrada, saida,codigo_barras))
        conn.commit()
    except Exception as e:
        print("Ocorreu um erro ao tentar excluir os dados:", e)
    finally:
        conn.close()

# Função para carregar os dados do banco de dados na Treeview
def carregar_do_bd(tree):
    conn = sqlite3.connect('pydados.db')
    cursor = conn.cursor()
    query = "SELECT * FROM ener"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        tree.insert('', 'end', values=row)
    conn.close()



# Atualizar inventário
def atualizar_form(i):
    conn = sqlite3.connect("pydados.db")
    with conn:
        cur = conn.cursor()
        query = "UPDATE ener SET nome=?, local=?, descricao=?, numero_serie=?, data_da_compra=?, data_saida=?, serie=?, codigo_barras=? WHERE id=?"
        cur.execute(query, i)

# Ver item no inventário
def ver_item(id):
    lista_itens = []
    conn = sqlite3.connect('pydados.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM ener WHERE id=?", (id,))
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

# Função para salvar dados na tabela ener
def salvar(nome, local, descricao, marca, data_da_compra, valor_da_compra, codigo_barras):
    conn = sqlite3.connect("pydados.db")
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO ener (nome, local, descricao, marca, data_da_compra, valor_da_compra, codigo_barras) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (nome, local, descricao, marca, data_da_compra, valor_da_compra, codigo_barras))


def listar_dados(tela_2):
    tela_2.show()

    # Conectar ao banco de dados
    conexao = sqlite3.connect("pydados.db")
    cursor = conexao.cursor()

    # Executar a consulta SQL
    cursor.execute("SELECT * FROM ener")
    dados_lidos = cursor.fetchall()

    # Definir o número de linhas e colunas da tabela na tela_2
    tela_2.tableWidget.setRowCount(len(dados_lidos))
    tela_2.tableWidget.setColumnCount(3)

    # Preencher a tabela com os dados lidos do banco de dados
    for i in range(len(dados_lidos)):
        for j in range(3):  # 3 colunas
            tela_2.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    # Fechar a conexão com o banco de dados
    conexao.close()
