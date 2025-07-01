import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

# --- 1. Configurações do Banco de Dados ---
DB_NAME = 'notas.db'

def conectar_db():
    """Conecta ao banco de dados SQLite e retorna a conexão."""
    conn = sqlite3.connect(DB_NAME)
    return conn

def criar_tabela():
    """Cria a tabela 'notas' se ela não existir no banco de dados."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            disciplina TEXT NOT NULL,
            nota REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# --- 2. Backend (Funções Python para CRUD) ---

def inserir_nota(nome, disciplina, nota):
    """Insere uma nova nota no banco de dados."""
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notas (nome, disciplina, nota) VALUES (?, ?, ?)",
                       (nome, disciplina, nota))
        conn.commit()
        # In a non-GUI environment, we might print confirmation instead of using messagebox
        # print("Nota adicionada com sucesso!")
        return True
    except sqlite3.Error as e:
        # In a non-GUI environment, print the error
        print(f"Erro ao inserir nota: {e}")
        # messagebox.showerror("Erro no Banco de Dados", f"Erro ao inserir nota: {e}")
        return False
    finally:
        if conn:
            conn.close()

def buscar_notas():
    """Busca e retorna todas as notas do banco de dados."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, disciplina, nota FROM notas ORDER BY nome, disciplina")
    notas = cursor.fetchall()
    conn.close()
    return notas

def atualizar_nota(id_registro, nova_nota):
    """Atualiza a nota de um registro específico no banco de dados."""
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE notas SET nota = ? WHERE id = ?",
                       (nova_nota, id_registro))
        conn.commit()
        # In a non-GUI environment, print confirmation
        # print("Nota atualizada com sucesso!")
        return True
    except sqlite3.Error as e:
         # In a non-GUI environment, print the error
        print(f"Erro ao atualizar nota: {e}")
        # messagebox.showerror("Erro no Banco de Dados", f"Erro ao atualizar nota: {e}")
        return False
    finally:
        if conn:
            conn.close()

def deletar_nota(id_registro):
    """Deleta um registro de nota do banco de dados."""
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notas WHERE id = ?", (id_registro,))
        conn.commit()
        # In a non-GUI environment, print confirmation
        # print("Nota deletada com sucesso!")
        return True
    except sqlite3.Error as e:
         # In a non-GUI environment, print the error
        print(f"Erro ao deletar nota: {e}")
        # messagebox.showerror("Erro no Banco de Dados", f"Erro ao deletar nota: {e}")
        return False
    finally:
        if conn:
            conn.close()

# --- 3. Interface Gráfica (Tkinter) ---
# This class is for the GUI and cannot run directly in a standard Jupyter notebook cell.
# We will keep the class definition, but the execution part needs to be handled outside the notebook
# or conditioned to run only in a suitable environment.

class NotasApp:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Notas")
        master.geometry("700x500") # Tamanho inicial da janela

        criar_tabela() # Garante que a tabela exista ao iniciar o app

        # Configurar estilo para botões e Treeview
        style = ttk.Style()
        style.configure("TButton",
                        font=("Inter", 10),
                        padding=8,
                        background="#4CAF50",
                        foreground="black",
                        relief="flat")
        style.map("TButton",
                  background=[('active', '#45a049')]) # Cor ao passar o mouse

        style.configure("Treeview.Heading", font=("Inter", 10, "bold"))
        style.configure("Treeview",
                        font=("Inter", 10),
                        rowheight=25,
                        fieldbackground="#e0e0e0",
                        background="#ffffff")

        # Frame para entrada de dados
        self.frame_entrada = ttk.LabelFrame(master, text="Entrada de Dados", padding="10")
        self.frame_entrada.pack(pady=10, padx=10, fill="x")

        # Widgets de entrada
        self.criar_campo(self.frame_entrada, "Nome do Aluno:", 0, 0, "nome_entry")
        self.criar_campo(self.frame_entrada, "Disciplina:", 1, 0, "disciplina_entry")
        self.criar_campo(self.frame_entrada, "Nota:", 2, 0, "nota_entry")

        # Frame para botões de ação
        self.frame_botoes = tk.Frame(master)
        self.frame_botoes.pack(pady=5, padx=10, fill="x")

        # Botões
        self.btn_adicionar = ttk.Button(self.frame_botoes, text="Adicionar Nota", command=self.adicionar_nota_gui)
        self.btn_adicionar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.btn_atualizar = ttk.Button(self.frame_botoes, text="Atualizar Nota", command=self.atualizar_nota_gui)
        self.btn_atualizar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.btn_deletar = ttk.Button(self.frame_botoes, text="Deletar Nota", command=self.deletar_nota_gui)
        self.btn_deletar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        self.btn_limpar = ttk.Button(self.frame_botoes, text="Limpar Campos", command=self.limpar_campos)
        self.btn_limpar.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        # Configurar colunas dos botões para expansão
        self.frame_botoes.grid_columnconfigure(0, weight=1)
        self.frame_botoes.grid_columnconfigure(1, weight=1)
        self.frame_botoes.grid_columnconfigure(2, weight=1)
        self.frame_botoes.grid_columnconfigure(3, weight=1)

        # Treeview para exibir notas
        self.tree = ttk.Treeview(master, columns=("ID", "Nome", "Disciplina", "Nota"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Disciplina", text="Disciplina")
        self.tree.heading("Nota", text="Nota")

        # Ajustar largura das colunas
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Nome", width=200, anchor="w")
        self.tree.column("Disciplina", width=150, anchor="w")
        self.tree.column("Nota", width=80, anchor="center")

        self.tree.pack(pady=10, padx=10, fill="both", expand=True)

        # Add Scrollbar to Treeview
        scrollbar = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Bind Treeview selection to fill fields
        self.tree.bind("<<TreeviewSelect>>", self.selecionar_item)

        self.exibir_notas_gui() # Load notes when the app starts

    def criar_campo(self, parent, label_text, row, col, entry_attr_name):
        """Creates a label and an entry field and packs them."""
        label = ttk.Label(parent, text=label_text, font=("Inter", 10))
        label.grid(row=row, column=col, sticky="w", pady=2, padx=5)
        entry = ttk.Entry(parent, width=40, font=("Inter", 10))
        entry.grid(row=row, column=col+1, sticky="ew", pady=2, padx=5)
        setattr(self, entry_attr_name, entry) # Store the Entry as a class attribute

        # Configure column expansion within the input frame
        parent.grid_columnconfigure(col+1, weight=1)

    def validar_campos(self, nome, disciplina, nota_str):
        """Valida os dados de entrada."""
        if not nome.strip() or not disciplina.strip():
            messagebox.showwarning("Campos Vazios", "Nome do aluno e disciplina não podem ser vazios.")
            return False, None
        try:
            nota = float(nota_str)
            if not (0 <= nota <= 10): # Exemplo de validação de nota entre 0 e 10
                messagebox.showwarning("Nota Inválida", "A nota deve ser um número entre 0 e 10.")
                return False, None
        except ValueError:
            messagebox.showwarning("Nota Inválida", "A nota deve ser um número válido.")
            return False, None
        return True, nota

    def adicionar_nota_gui(self):
        """Pega dados da GUI, insere no DB e atualiza a Treeview."""
        nome = self.nome_entry.get()
        disciplina = self.disciplina_entry.get()
        nota_str = self.nota_entry.get()

        valido, nota = self.validar_campos(nome, disciplina, nota_str)
        if not valido:
            return

        if inserir_nota(nome, disciplina, nota):
            messagebox.showinfo("Sucesso", "Nota adicionada com sucesso!")
            self.limpar_campos()
            self.exibir_notas_gui()

    def exibir_notas_gui(self):
        """Limpa a Treeview e a preenche com os dados do DB."""
        # Limpar Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Inserir novos dados
        notas = buscar_notas()
        for nota in notas:
            self.tree.insert("", "end", values=nota)

    def atualizar_nota_gui(self):
        """Atualiza a nota do registro selecionado na Treeview."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Nenhum Item Selecionado", "Selecione uma nota para atualizar.")
            return

        item_values = self.tree.item(selected_item)["values"]
        id_registro = item_values[0] # ID é a primeira coluna

        nova_nota_str = self.nota_entry.get()

        # Validar apenas a nova nota
        try:
            nova_nota = float(nova_nota_str)
            if not (0 <= nova_nota <= 10):
                messagebox.showwarning("Nota Inválida", "A nova nota deve ser um número entre 0 e 10.")
                return
        except ValueError:
            messagebox.showwarning("Nota Inválida", "A nova nota deve ser um número válido.")
            return

        if atualizar_nota(id_registro, nova_nota):
            messagebox.showinfo("Sucesso", "Nota atualizada com sucesso!")
            self.limpar_campos()
            self.exibir_notas_gui()

    def deletar_nota_gui(self):
        """Deleta o registro selecionado na Treeview."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Nenhum Item Selecionado", "Selecione uma nota para deletar.")
            return

        item_values = self.tree.item(selected_item)["values"]
        id_registro = item_values[0] # ID é a primeira coluna

        if messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja deletar a nota de {item_values[1]} ({item_values[2]})?"):
            if deletar_nota(id_registro):
                messagebox.showinfo("Sucesso", "Nota deletada com sucesso!")
                self.limpar_campos()
                self.exibir_notas_gui()

    def selecionar_item(self, event):
        """Preenche os campos de entrada com os dados do item selecionado na Treeview."""
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)["values"]
            self.nome_entry.delete(0, tk.END)
            self.nome_entry.insert(0, item_values[1]) # Nome
            self.disciplina_entry.delete(0, tk.END)
            self.disciplina_entry.insert(0, item_values[2]) # Disciplina
            self.nota_entry.delete(0, tk.END)
            self.nota_entry.insert(0, item_values[3]) # Nota
        else:
            self.limpar_campos()

    def limpar_campos(self):
        """Limpa todos os campos de entrada."""
        self.nome_entry.delete(0, tk.END)
        self.disciplina_entry.delete(0, tk.END)
        self.nota_entry.delete(0, tk.END)


# --- 4. Execução Principal ---
if __name__ == "__main__":
    # Cria a janela principal e inicia a aplicação
    root = tk.Tk()
    app = NotasApp(root)
    root.mainloop()