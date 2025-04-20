💰 Gestor de Finanças Pessoal
Um aplicativo simples feito com Python e ttkbootstrap para ajudar você a controlar receitas e despesas, visualizar o saldo atual e manter um histórico de transações.

🖼️ Interface
![screenshot opcional aqui, se quiser adicionar depois com imagem]

📦 Funcionalidades
Adicionar receitas e despesas

Visualizar o saldo total

Histórico de transações com:

Data

Tipo (Receita/Despesa)

Categoria

Valor

Descrição

🚀 Tecnologias Utilizadas
Python 3

ttkbootstrap – biblioteca de GUI moderna baseada em tkinter

json – para persistência de dados local

🛠️ Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/gestor-financas.git
cd gestor-financas
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
Instale as dependências:

bash
Copiar código
pip install ttkbootstrap
Execute o aplicativo:

bash
Copiar código
python main.py
📁 Estrutura do Projeto
bash
Copiar código
gestor-financas/
│
├── main.py              # Código principal do app
├── financas.json        # Arquivo gerado automaticamente para armazenar as transações
└── README.md            # Este arquivo
