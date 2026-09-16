from banco import conectar


def registrar_entrega(id_pedido, taxa, status="Em Trânsito"):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO entregas (id_pedido, status, taxa)
    VALUES (?, ?, ?)
    """
    cursor.execute(sql, (id_pedido, status, taxa))

    conexao.commit()
    conexao.close()
    print("Entrega agendada/registrada com sucesso!")


def listar_entregas():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id_entrega, id_pedido, status, taxa FROM entregas")
    dados = cursor.fetchall()
    conexao.close()
    return dados