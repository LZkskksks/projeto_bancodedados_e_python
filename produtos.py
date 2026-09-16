from banco import conectar


def cadastrar_produto(nome, preco, estoque, descricao="", id_categoria=1):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO produtos (nome_produto, descricao, id_categoria, preco, estoque)
    VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(sql, (nome, descricao, id_categoria, preco, estoque))

    conexao.commit()
    conexao.close()
    print(f"Produto '{nome}' cadastrado com sucesso!")


def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id_produto, nome_produto, preco, estoque FROM produtos")
    registros = cursor.fetchall()
    conexao.close()

    lista_produtos = []
    for r in registros:
        p = {
            "id": r[0],
            "nome": r[1],
            "preco": r[2],
            "estoque": r[3]
        }
        lista_produtos.append(p)

    return lista_produtos