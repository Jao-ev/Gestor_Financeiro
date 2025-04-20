import json
from pathlib import Path
from datetime import datetime
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

ARQUIVO_DADOS = Path("financas.json")

def inicializar_arquivo():
    if not ARQUIVO_DADOS.exists():
        with open(ARQUIVO_DADOS, "w") as f:
            json.dump({"transacoes": []}, f)

def carregar_dados():
    with open(ARQUIVO_DADOS, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w") as f:
        json.dump(dados, f, indent=4)

def calcular_saldo():
    dados = carregar_dados()
    saldo = 0
    for t in dados["transacoes"]:
        if t["tipo"] == "receita":
            saldo += t["valor"]
        else:
            saldo -= t["valor"]
    return saldo

def adicionar_transacao_gui(tipo, categoria, valor, descricao):
    dados = carregar_dados()
    transacao = {
        "tipo": tipo,
        "categoria": categoria,
        "valor": float(valor),
        "data": datetime.now().strftime("%Y-%m-%d"),
        "descricao": descricao
    }
    dados["transacoes"].append(transacao)
    salvar_dados(dados)

def atualizar_interface():
    saldo = calcular_saldo()
    cor = "success" if saldo >= 0 else "danger"
    saldo_label.config(text=f"Saldo atual: R$ {saldo:.2f}", bootstyle=cor)
    transacoes_list.delete(*transacoes_list.get_children())
    dados = carregar_dados()
    for t in dados["transacoes"]:
        transacoes_list.insert("", "end", values=(t["data"], t["tipo"], t["categoria"], f"R$ {t['valor']:.2f}", t["descricao"]))

def janela_adicionar(tipo):
    win = ttk.Toplevel(root)
    win.title(f"Adicionar {tipo.capitalize()}")
    win.geometry("300x250")
    win.resizable(False, False)

    ttk.Label(win, text="Categoria:").pack(pady=5)
    entry_categoria = ttk.Entry(win)
    entry_categoria.pack()

    ttk.Label(win, text="Valor:").pack(pady=5)
    entry_valor = ttk.Entry(win)
    entry_valor.pack()

    ttk.Label(win, text="Descrição:").pack(pady=5)
    entry_descricao = ttk.Entry(win)
    entry_descricao.pack()

    def confirmar():
        try:
            adicionar_transacao_gui(tipo, entry_categoria.get(), 
            float(entry_valor.get()),
            entry_descricao.get())
            win.destroy()
            atualizar_interface()
        except ValueError:
            ttk.Messagebox.show_error("Erro", "Valor inválido")

    ttk.Button(win, text="Salvar", bootstyle="primary", command=confirmar).pack(pady=10)

# === GUI com ttkbootstrap ===
inicializar_arquivo()
root = ttk.Window(themename="superhero")  # dark theme
root.title("Gestor de Finanças Pessoal")
root.geometry("700x500")

saldo_label = ttk.Label(root, text="", font=("Segoe UI", 16))
saldo_label.pack(pady=10)

frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=5)

ttk.Button(frame_botoes, text="Adicionar Receita", bootstyle="success", command=lambda: janela_adicionar("receita")).grid(row=0, column=0, padx=10)
ttk.Button(frame_botoes, text="Adicionar Despesa", bootstyle="danger", command=lambda: janela_adicionar("despesa")).grid(row=0, column=1, padx=10)

colunas = ("Data", "Tipo", "Categoria", "Valor", "Descrição")
transacoes_list = ttk.Treeview(root, columns=colunas, show="headings", bootstyle="info")
for col in colunas:
    transacoes_list.heading(col, text=col)
    transacoes_list.column(col, width=120)
transacoes_list.pack(fill="both", expand=True, padx=10, pady=10)

atualizar_interface()
root.mainloop()
