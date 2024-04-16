import sqlite3

# Conectando ao banco de dados
con = sqlite3.connect('estoque.db')

# Dados para inserção
dados = ['nome_do_item', 'localizacao', 'descricao_do_item',
         'numero_de_serie', 'data_de_entrada', 'data_de_saida', 'imagem_em_blob']

# Criando uma função para inserir dados


def inserir_dados(dados):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Controle_de_Estoque(nome, localidade, descricao, numero_de_serie, data_de_entrada, data_de_saida, imagem) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, dados)


# Chamando a função para inserir dados
inserir_dados(dados)
