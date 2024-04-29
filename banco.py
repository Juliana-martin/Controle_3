import sqlite3
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

def inserir_dados(nome, local, descricao, serie, data_entrada, data_saida, codigo_barras):
    # Conectando ao banco de dados
    banco = sqlite3.connect('pydados.db')
    
    # Criando o cursor
    cursor = banco.cursor()

    # Verificando se a tabela já existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ener'")
    tabela_ener = cursor.fetchone()

    # Se a tabela não existir, então criamos ela
    if tabela_ener is None:
        cursor.execute("CREATE TABLE ener( id INTEGER PRIMARY KEY, nome TEXT, local TEXT, descricao TEXT, serie INTEGER, data_entrada DATE, data_saida DATE, codigo_barras TEXT)")
        print("Tabela 'ener' criada com sucesso.")
    else:
        print("A tabela 'ener' já existe. Não é necessário criar novamente.")

    # Inserindo os dados na tabela
    cursor.execute("INSERT INTO ener (nome, local, descricao, serie, data_entrada, data_saida, codigo_barras) VALUES (?, ?, ?, ?, ?, ?, ?)", (nome, local, descricao, serie, data_entrada, data_saida, codigo_barras))

    # Exibindo todos os dados na tabela
    cursor.execute("SELECT * FROM ener")
    print(cursor.fetchall())

    banco.commit()

def deletar_form(nome, local, descricao, serie, data_entrada, data_saida, codigo_barras):
    # Conectando ao banco de dados
    banco = sqlite3.connect('pydados.db')

    try:
        # Criando o cursor
        cursor = banco.cursor()

        # Executando a query para deletar os dados
        query = "DELETE FROM ener WHERE nome = ? AND local = ? AND descricao = ? AND serie = ? AND data_entrada = ? AND data_saida = ? AND codigo_barras = ?"
        cursor.execute(query, (nome, local, descricao, serie, data_entrada, data_saida, codigo_barras))
        banco.commit()
    except sqlite3.Error as e:
        print("Ocorreu um erro ao tentar excluir os dados:", e)
    finally:
        # Fechando a conexão com o banco de dados
        banco.close()

def adicionar_coluna_codigo_barras():
    try:
        # Conectando ao banco de dados
        banco = sqlite3.connect('pydados.db')
        cursor = banco.cursor()

        # Verificando se a coluna já existe
        cursor.execute("PRAGMA table_info(ener)")
        colunas = cursor.fetchall()
        colunas_existentes = [coluna[1] for coluna in colunas]
        
        if 'codigo_barras' not in colunas_existentes:
            # Adicionando a coluna codigo_barras à tabela ener
            cursor.execute("ALTER TABLE ener ADD COLUMN codigo_barras TEXT")
            print("Coluna 'codigo_barras' adicionada com sucesso.")
        else:
            print("A coluna 'codigo_barras' já existe na tabela 'ener'.")

        banco.commit()
    except sqlite3.Error as e:
        print("Ocorreu um erro ao adicionar a coluna:", e)
    finally:
        # Fechando a conexão com o banco de dados
        banco.close()

# Chamando a função para adicionar a coluna
adicionar_coluna_codigo_barras()
