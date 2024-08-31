import sys
sys.path.append('.')
import tkinter as tk
from tkinter import messagebox
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from PIL import Image, ImageTk


# EVENTUAL DESENVOLVIMENTO DE UMA INTERFACE GRAFICA PARA O MENU DE LOGIN!

def realizar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "admin" and senha == "admin":  # mudar depois
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        sair()
        from ProjetoConsultorio.View.menu import mostrar_menu
        mostrar_menu()
    elif usuario == "" or senha == "":
        messagebox.showerror("Erro", "Preencha todos os campos.")
        
    elif BancoDadosController.buscarUsuario(usuario, senha) is not None:
        messagebox.showinfo("Login", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

def abrir_janela_cadastro():
    
    janela_cadastro = tk.Toplevel()
    janela_cadastro.geometry("500x450")
    janela_cadastro.title("Cadastro de Usuário")
    
    imagem = Image.open("ProjetoConsultorio/Util/logo.jpg")  
    imagem = imagem.resize((150, 150))  
    imagem_tk = ImageTk.PhotoImage(imagem)

    label_imagem = tk.Label(janela_cadastro, image=imagem_tk)
    label_imagem.image = imagem_tk
    label_imagem.pack(pady=10)
    
    lbl_novo_usuario = tk.Label(janela_cadastro, text="Novo Usuário:")
    lbl_novo_usuario.pack(pady=5)
    entry_novo_usuario = tk.Entry(janela_cadastro)
    entry_novo_usuario.pack(pady=5)
    
    lbl_nova_senha = tk.Label(janela_cadastro, text="Nova Senha:")
    lbl_nova_senha.pack(pady=5)
    entry_nova_senha = tk.Entry(janela_cadastro, show="*")
    entry_nova_senha.pack(pady=5)
    
    btn_cadastrar = tk.Button(janela_cadastro, text="Cadastrar", command=lambda: cadastrar_usuario(entry_novo_usuario, entry_nova_senha, janela_cadastro))
    btn_cadastrar.pack(pady=20)

def cadastrar_usuario(entry_novo_usuario, entry_nova_senha, janela_cadastro):
    novo_usuario = entry_novo_usuario.get()
    nova_senha = entry_nova_senha.get()
    
    BancoDadosController.cadastrarUsuario (novo_usuario, nova_senha)
    messagebox.showinfo("Cadastro", f"Usuário {novo_usuario} cadastrado com sucesso!")

    janela_cadastro.destroy()

def sair():
    janela.destroy()

# Janela Principal de Login
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("500x450")

imagem = Image.open("ProjetoConsultorio/Util/logo.jpg")  
imagem = imagem.resize((150, 150))  
imagem_tk = ImageTk.PhotoImage(imagem)

label_imagem = tk.Label(janela, image=imagem_tk)
label_imagem.pack(pady=10)

lbl_usuario = tk.Label(janela, text="Usuário:")
lbl_usuario.pack(pady=5)
entry_usuario = tk.Entry(janela)
entry_usuario.pack(pady=5)

lbl_senha = tk.Label(janela, text="Senha:")
lbl_senha.pack(pady=5)
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack(pady=5)

btn_login = tk.Button(janela, text="Login", command=realizar_login)
btn_login.pack(pady=10)

btn_cadastrar = tk.Button(janela, text="Cadastrar", command=abrir_janela_cadastro)
btn_cadastrar.pack(pady=10)

janela.mainloop()
