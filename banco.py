import sqlite3

def conectar():
    return sqlite3.connect("padaria.db")

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    # Tabela Categoria
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categoria (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT NOT NULL
    )
    """)

    # Tabela Clientes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT,
        telefone TEXT,
        cidade TEXT,
        estado TEXT,
        endereco TEXT,
        cep TEXT,
        data_de_nascimento DATE
    )
    """)

    # Tabela Produtos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_produto TEXT NOT NULL,
        descricao TEXT,
        id_categoria INTEGER,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL,
        FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria)
    )
    """)

    # Tabela Pedidos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER,
        data DATETIME DEFAULT CURRENT_TIMESTAMP,
        status TEXT,
        valor REAL,
        FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
    )
    """)

    # Tabela Itens Pedido
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS itens_pedido (
        id_item INTEGER PRIMARY KEY AUTOINCREMENT,
        id_produto INTEGER,
        id_pedido INTEGER,
        quantidade INTEGER,
        total REAL,
        FOREIGN KEY (id_produto) REFERENCES produtos (id_produto),
        FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido)
    )
    """)

    # Tabela Pagamentos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pagamentos (
        id_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pedido INTEGER,
        forma_pagamento TEXT,
        valor REAL,
        status TEXT,
        data DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido)
    )
    """)

    # Tabela Entregas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entregas (
        id_entrega INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pedido INTEGER,
        saida DATETIME,
        entrega DATETIME,
        status TEXT,
        taxa REAL,
        FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido)
    )
    """)

    conexao.commit()
    conexao.close()
    print("Banco de dados e tabelas verificados com sucesso!")


criar_tabelas()