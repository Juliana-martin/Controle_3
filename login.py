import customtkinter
from tkinter import messagebox
import sqlite3

class BackEnd():
    def __init__(self):
        self.conn = None
        self.cursor = None

    def conectar_db(self):
        self.conn = sqlite3.connect('pydados.db')
        print("Banco conectado")
        self.cursor = self.conn.cursor()

    def desconectar_db(self):
        self.conn.close()
        print("Banco de dados desconectado")

    def tabela_usuarios(self):
        self.conectar_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirmar_Senha TEXT NOT NULL
            );
        """)
        print("Tabela criada com sucesso!")
        self.desconectar_db()

    def cadastrar(self):
        self.email_cadastro = self.email_cadastro_entry.get() 
        self.senha_cadastro = self.senha_cadastro_entry.get()
        self.confirmar_senha_cadastro = self.Confirmar_senha_entry.get()

        self.conectar_db()

        try:
            if len(self.email_cadastro) < 4:
                messagebox.showwarning(title="Sistema de Login", message="O email deve ter pelo menos 4 caracteres.")
            elif len(self.senha_cadastro) < 4:
                messagebox.showwarning(title="Sistema de Login", message="A senha deve ter pelo menos 4 caracteres.")
            elif self.senha_cadastro != self.confirmar_senha_cadastro:
                messagebox.showerror(title="Sistema de Login", message="Erro!\nSenha e Confirmar Senha precisam ser iguais.")
            else:
                self.cursor.execute("""
                        INSERT INTO Usuarios (email, Senha, Confirmar_Senha)
                        VALUES (?, ?, ?)""", (self.email_cadastro, self.senha_cadastro, self.confirmar_senha_cadastro))
                self.conn.commit()
                messagebox.showinfo(title="Sistema de Login", message=f"Usuário: {self.email_cadastro}\nCadastrado com sucesso!")
                self.desconectar_db()
                self.limpar_entry_cadastro()
        except Exception as e:
            messagebox.showerror(title="Sistema de Login", message="Erro no cadastro. \nPor favor, tente novamente!")
            print(e)
            self.desconectar_db()

    def verificar_login(self):
        self.email_login = self.email_login_entry.get()
        self.senha_login = self.senha_login_entry.get()

        self.conectar_db()

        self.cursor.execute("""SELECT * FROM Usuarios WHERE (email = ? AND Senha = ?)""", (self.email_login, self.senha_login))

        self.verificar_dados = self.cursor.fetchone()

        try:
            if (self.email_login == "" or self.senha_login == ""):
                messagebox.showwarning(title="Sistema de Login", message="Preencha todos os campos!")
            elif (self.email_login in self.verificar_dados and self.senha_login in self.verificar_dados):
                messagebox.showinfo(title="Sistema de Login", message=f"Iniciando sessão!\nUsuário: {self.email_login}")
                self.desconectar_db()
                self.limpar_entry_login()
        except Exception as e:
            messagebox.showerror(title="Sistema de Login", message="Erro!\nUsuário ou Senha incorreto.\nTente novamente!")
            print(e)
            self.desconectar_db()


# Frontend

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

backend = BackEnd()

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="E-mail")
email.pack(padx=10, pady=10)
backend.email_login_entry = email

senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)
backend.senha_login_entry = senha

botao = customtkinter.CTkButton(janela, text="Login", command=backend.verificar_login)
botao.pack(padx=10, pady=10)

cadastrar = customtkinter.CTkButton(janela, text="Cadastrar", command=backend.cadastrar)
cadastrar.pack(padx=10, pady=10)

janela.mainloop()
