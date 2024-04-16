import sqlite3

# Conectando ao banco de dados
con = sqlite3.connect('estoque.db')

# Criando o cursor
cur = con.cursor()

# Executando a criação da tabela
cur.execute('''CREATE TABLE Controle_de_Estoque (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               localidade TEXT,
               descricao TEXT,
               numero_de_serie TEXT,
               data_de_entrada TEXT,
               data_de_saida TEXT,
               imagem BLOB
               )''')
