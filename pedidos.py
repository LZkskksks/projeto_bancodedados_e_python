from banco import conectar


def registrar_pedido(id_cliente, itens):

    conexao = conectar()
    cursor = conexao.cursor()


    total_pedido = 0.0
    for item in itens:
        total_pedido += item["qtd"] * item["preco"]


    cursor.execute(
        "INSERT INTO pedidos (id_cliente, status, valor) VALUES (?, ?, ?)",
        (id_cliente, 'Finalizado', total_pedido)
    )


    id_pedido = cursor.lastrowid


    for item in itens:
        subtotal = item["qtd"] * item["preco"]
        cursor.execute("""
        INSERT INTO itens_pedido (id_produto, id_pedido, quantidade, total)
        VALUES (?, ?, ?, ?)
        """, (item["id_produto"], id_pedido, item["qtd"], subtotal))

    conexao.commit()
    conexao.close()
    print(f"\nPedido #{id_pedido} registrado com sucesso! Total: R$ {total_pedido:.2f}")


def listar_pedidos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id_pedido, id_cliente, data, status, valor FROM pedidos")
    pedidos = cursor.fetchall()
    conexao.close()
    return pedidos