import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def clique(): 
    print("Fazer Login")

def teste():
    # Código do segundo sistema
    janela2 = customtkinter.CTk()
    janela2.geometry("500x300")

    texto2 = customtkinter.CTkLabel(janela2, text="teste")
    texto2.pack(padx=10, pady=10)   
    teste.mainloop() 

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="E-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
