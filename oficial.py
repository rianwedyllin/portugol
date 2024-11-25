import tkinter as tk
from tkinter import messagebox


janela = tk.Tk()
janela.title("Lista de Tarefas")


entrada_tarefa = tk.Entry(janela, width=50)
entrada_tarefa.pack(pady=10)


def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa != "":
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Você precisa escrever uma tarefa.")


def marcar_concluida():
    try:
        index = lista_tarefas.curselection()[0]
        tarefa = lista_tarefas.get(index)
        lista_tarefas.delete(index)
        lista_tarefas.insert(index, tarefa + " - Concluído")
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para marcar como concluída.")


def remover_tarefa():
    try:
        index = lista_tarefas.curselection()[0]
        lista_tarefas.delete(index)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")



botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=5)

lista_tarefas = tk.Listbox(janela, width=50, height=10, selectmode=tk.SINGLE)
lista_tarefas.pack(pady=10)


botao_concluir = tk.Button(janela, text="Marcar como Concluída", command=marcar_concluida)
botao_concluir.pack(pady=5)


botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
botao_remover.pack(pady=5)


janela.mainloop()
