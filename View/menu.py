import sys
sys.path.append('.')
import tkinter as tk
from tkinter import messagebox
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController


def mostrar_menu():
    # limpa o frame do conteúdo e exibe novamente o menu
    limpar_frame(frame_conteudo)
    
    frame_menu.pack(side="left", fill="y", padx=10, pady=10)
    lbl_menu = tk.Label(frame_menu, text="Menu", font=("Arial", 14))
    lbl_menu.pack(pady=5)
    
    btn_cadastrar_cliente = tk.Button(frame_menu, text="Cadastrar Cliente", command=cadastrarCliente)
    btn_cadastrar_cliente.pack(pady=10)
    
    btn_cadastrar_consulta = tk.Button(frame_menu, text="Cadastrar Consulta", command=cadastrarConsulta)
    btn_cadastrar_consulta.pack(pady=10)
    
    btn_buscar_consulta = tk.Button(frame_menu, text="Buscar Consulta", command=buscarConsulta)
    btn_buscar_consulta.pack(pady=10)
    
    btn_buscar_cliente = tk.Button(frame_menu, text="Buscar Cliente", command=buscarCliente)
    btn_buscar_cliente.pack(pady=10)
    
    btn_sair = tk.Button(frame_menu, text="Sair", command=sair)
    btn_sair.pack(pady=10)

def cadastrarCliente():
    limpar_frame(frame_menu)
    limpar_frame(frame_conteudo)
    
    lbl_nome = tk.Label(frame_conteudo, text="Nome:")
    lbl_nome.pack(pady=5)
    entry_nome = tk.Entry(frame_conteudo)
    entry_nome.pack(pady=5)

    lbl_cpf = tk.Label(frame_conteudo, text="CPF:")
    lbl_cpf.pack(pady=5)
    entry_cpf = tk.Entry(frame_conteudo)
    entry_cpf.pack(pady=5)
    
    def salvar_cliente():
        nome = entry_nome.get()
        cpf = entry_cpf.get()
        if nome == "" or cpf == "":
            messagebox.showerror("Erro", "Preencha todos os campos.")
        else:
            BancoDadosController.cadastrarCliente(nome, cpf)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            mostrar_menu()

    btn_salvar = tk.Button(frame_conteudo, text="Salvar", command=salvar_cliente)
    btn_salvar.pack(pady=10)
    
    btn_voltar = tk.Button(frame_conteudo, text="Voltar", command=voltar)
    btn_voltar.pack(pady=10)

def cadastrarConsulta():
    limpar_frame(frame_menu)
    limpar_frame(frame_conteudo)
    
    
    lbl_descricao = tk.Label(frame_conteudo, text="Descrição:")
    lbl_descricao.pack(pady=5)
    entry_descricao = tk.Entry(frame_conteudo)
    entry_descricao.pack(pady=5)

    lbl_data = tk.Label(frame_conteudo, text="Data:")
    lbl_data.pack(pady=5)
    entry_data = tk.Entry(frame_conteudo)
    entry_data.pack(pady=5)
    
    def salvar_consulta():
        descricao = entry_descricao.get()
        data = entry_data.get()
        
        if descricao == "" or data == "":
            messagebox.showerror("Erro", "Preencha todos os campos.")
        else:
            BancoDadosController.cadastrarConsulta(descricao, data)
            messagebox.showinfo("Sucesso", "Consulta cadastrada com sucesso!")
            mostrar_menu()

    btn_salvar = tk.Button(frame_conteudo, text="Salvar", command=salvar_consulta)
    btn_salvar.pack(pady=10)
    
    btn_voltar = tk.Button(frame_conteudo, text="Voltar", command=voltar)
    btn_voltar.pack(pady=10)

def buscarCliente():
    limpar_frame(frame_menu)
    limpar_frame(frame_conteudo)
    
    lbl_nome = tk.Label(frame_conteudo, text="Nome:")
    lbl_nome.pack(pady=5)
    entry_nome = tk.Entry(frame_conteudo)
    entry_nome.pack(pady=5)

    lbl_cpf = tk.Label(frame_conteudo, text="CPF:")
    lbl_cpf.pack(pady=5)
    entry_cpf = tk.Entry(frame_conteudo)
    entry_cpf.pack(pady=5)
    
    def buscar_cliente():
        nome = entry_nome.get()
        cpf = entry_cpf.get()
        if nome == "" or cpf == "":
            messagebox.showerror("Erro", "Preencha todos os campos.")
        else:
            if BancoDadosController.buscarCliente(nome, cpf) is None:
                messagebox.showerror("Erro", "Cliente não encontrado.")
            else:
                messagebox.showinfo("Sucesso", "Cliente já cadastrado!")
            mostrar_menu()

    btn_buscar = tk.Button(frame_conteudo, text="Buscar", command=buscar_cliente)
    btn_buscar.pack(pady=10)
    
    btn_voltar = tk.Button(frame_conteudo, text="Voltar", command=voltar)
    btn_voltar.pack(pady=10)

def buscarConsulta():
    limpar_frame(frame_menu)
    limpar_frame(frame_conteudo)
    
    dados = BancoDadosController.mostrar_consultas()
    lbl_dados = tk.Label(janela, text="Dados aparecerão aqui", justify="left")
    lbl_dados.pack(pady=20)
    lbl_dados.config(text=dados)
    
    
    def volte():
        lbl_dados.destroy()
        limpar_frame(frame_conteudo)
        limpar_frame(frame_menu)
        mostrar_menu()
    
    btn_voltar = tk.Button(frame_conteudo, text="Voltar", command=volte)
    btn_voltar.pack(pady=10)

def limpar_frame(frame):
    # remove todos os widgets do frame atual
    for widget in frame.winfo_children():
        widget.destroy()
        
def voltar():
        limpar_frame(frame_conteudo)
        limpar_frame(frame_menu)
        mostrar_menu()
        
def sair():
    janela.destroy()

# janela Principal
janela = tk.Tk()
janela.title("Clinitech")
janela.geometry("500x450")

# frame para o menu à esquerda
frame_menu = tk.Frame(janela)
frame_menu.pack(side="left", fill="y", padx=10, pady=10)

# frame para o conteúdo dinâmico
frame_conteudo = tk.Frame(janela)
frame_conteudo.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# inicializa o menu
mostrar_menu()

janela.mainloop()
