import tkinter as tk
from tkinter import ttk

# Função para calcular a média e determinar a situação
def calcular_media():
    nome = entry_nome.get()
    try:
        nota1 = float(entry_nota1.get())
        nota2 = float(entry_nota2.get())
    except ValueError:
        label_erro['text'] = "Insira valores válidos para as notas."
        return

    label_erro['text'] = ""  # Limpa a mensagem de erro, se houver
    media = (nota1 + nota2) / 2
    situacao = "Aprovado" if media >= 7 else "Em Recuperação" if media >= 5 else "Reprovado"

    # Adiciona os dados na tabela
    treeview.insert("", "end", values=(nome, f"{nota1:.1f}", f"{nota2:.1f}", f"{media:.1f}", situacao))

    # Limpa os campos de entrada
    entry_nome.delete(0, tk.END)
    entry_nota1.delete(0, tk.END)
    entry_nota2.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Média dos alunos")
root.geometry("600x400")

# Título
label_titulo = tk.Label(root, text="Média dos alunos", font=("Arial", 14, "bold"))
label_titulo.pack(pady=10)

# Área de entrada de dados
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

label_nome = tk.Label(frame_entrada, text="Nome do Aluno:")
label_nome.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
entry_nome = tk.Entry(frame_entrada, width=25)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_nota1 = tk.Label(frame_entrada, text="Nota 1:")
label_nota1.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
entry_nota1 = tk.Entry(frame_entrada, width=10)
entry_nota1.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

label_nota2 = tk.Label(frame_entrada, text="Nota 2:")
label_nota2.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
entry_nota2 = tk.Entry(frame_entrada, width=10)
entry_nota2.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

# Botão para calcular a média
btn_calcular = tk.Button(root, text="Calcular Média", command=calcular_media)
btn_calcular.pack(pady=10)

# Mensagem de erro
label_erro = tk.Label(root, text="", fg="red")
label_erro.pack()

# Tabela de resultados
frame_tabela = tk.Frame(root)
frame_tabela.pack(pady=10)

treeview = ttk.Treeview(frame_tabela, columns=("nome", "nota1", "nota2", "media", "situacao"), show="headings", height=10)
treeview.pack(side=tk.LEFT)

# Configuração das colunas
treeview.heading("nome", text="Aluno")
treeview.heading("nota1", text="Nota 1")
treeview.heading("nota2", text="Nota 2")
treeview.heading("media", text="Média")
treeview.heading("situacao", text="Situação")

treeview.column("nome", width=150)
treeview.column("nota1", width=50, anchor="center")
treeview.column("nota2", width=50, anchor="center")
treeview.column("media", width=50, anchor="center")
treeview.column("situacao", width=100, anchor="center")

# Scrollbar para a tabela
scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Executar a aplicação
root.mainloop()
