
import tkinter as tk

# Criar a janela principal
root = tk.Tk()
root.title("Sistema de Cadastro de Funcionários")

# Definir o tamanho da janela
root.geometry("600x400")

# Adicionar os botões
btn_cadastrar = tk.Button(root, text="Cadastrar", width= 40, height= 2)
btn_cadastrar.pack(pady=10)

btn_listar = tk.Button(root, text="Listar", width=40, height=2)
btn_listar.pack(pady=10)

btn_pesquisar = tk.Button(root, text="Pesquisar", width=40, height=2)
btn_pesquisar.pack(pady=10)

btn_deletar = tk.Button(root, text="Deletar", width=40, height=2)
btn_deletar.pack(pady=10)

btn_sair = tk.Button(root, text="Sair", width=40, height=2)
btn_sair.pack(pady=10)

teste = tk.Button(root, text='Seilá', width=40, height=2)
teste.pack(pady=10)

# Iniciar o loop principal
root.mainloop()
