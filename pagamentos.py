from banco import conectar


def registrar_pagamento(id_pedido, forma_pagamento, valor):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO pagamentos (id_pedido, forma_pagamento, valor, status)
    VALUES (?, ?, ?, 'Aprovado')
    """
    cursor.execute(sql, (id_pedido, forma_pagamento, valor))

    conexao.commit()
    conexao.close()
    print("Pagamento registrado com sucesso!")


def listar_pagamentos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id_pagamento, id_pedido, forma_pagamento, valor, status, data FROM pagamentos")
    dados = cursor.fetchall()
    conexao.close()
    return dados