from banco import conectar


def cadastrar_cliente(cliente):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO clientes (nome, email, telefone, cidade, estado, endereco, cep, data_de_nascimento)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """

    valores = (
        cliente["nome"],
        cliente["email"],
        cliente["telefone"],
        cliente["cidade"],
        cliente["estado"],
        cliente["endereco"],
        cliente["cep"],
        cliente["data_de_nascimento"]
    )

    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()
    print("Cliente cadastrado com sucesso!")


def listar_clientes():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id_cliente, nome, telefone, cidade FROM clientes")
    registros = cursor.fetchall()
    conexao.close()

    lista_clientes = []
    for linha in registros:
        dados = {
            "id": linha[0],
            "nome": linha[1],
            "telefone": linha[2],
            "cidade": linha[3]
        }
        lista_clientes.append(dados)

    return lista_clientes
