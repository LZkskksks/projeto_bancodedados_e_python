CREATE TABLE IF NOT EXISTS "clientes" (
    "id_cliente" INTEGER NOT NULL,
    "nome" VARCHAR(100) NOT NULL,
    "email" VARCHAR(100) NOT NULL UNIQUE,
    "telefone" VARCHAR(20) NOT NUll,
    "cidade" VARCHAR(80) NOT NULL,
    "uf" VARCHAR(2) NOT NULL,
    "endereco" VARCHAR(200) NOT NULL,
    "cep" VARCHAR(8) NOT NULL,
    "data_de_nascimento" DATE NOT NULL,
    PRIMARY KEY("id_cliente")
);

CREATE TABLE IF NOT EXISTS "categorias" (
    "id_categoria" INTEGER NOT NULL,
    "categoria" VARCHAR(50) NOT NULL,
    PRIMARY KEY("id_categoria")
);

CREATE TABLE IF NOT EXISTS "produtos" (
    "id_produto" INTEGER NOT NULL,
    "id_categoria" INTEGER,
    "nome_produto" VARCHAR(100) NOT NULL,
    "descricao" VARCHAR(255),
    "preco" NUMERIC(10,2) NOT NULL,
    "estoque" INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY("id_produto"),

    FOREIGN KEY ("id_categoria") REFERENCES "categorias"("id_categoria")
    ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "pedidos" (
    "id_pedido" INTEGER NOT NULL,
    "id_cliente" INTEGER NOT NULL,
    "data" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "status" VARCHAR(30) NOT NULL DEFAULT 'pendente',
    "valor" NUMERIC(10,2) NOT NULL,
    PRIMARY KEY("id_pedido"),
    
    FOREIGN KEY ("id_cliente") REFERENCES "clientes"("id_cliente")
    ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "itens_pedido" (
    "id_item" INTEGER NOT NULL,
    "id_produto" INTEGER NOT NULL,
    "id_pedido" INTEGER NOT NULL,
    "quantidade" INTEGER NOT NULL,
    "total" NUMERIC(10,2) NOT NULL DEFAULT 0,
    PRIMARY KEY("id_item"),

    FOREIGN KEY ("id_produto") REFERENCES "produtos"("id_produto")
    ON UPDATE NO ACTION ON DELETE NO ACTION,

    FOREIGN KEY ("id_pedido") REFERENCES "pedidos"("id_pedido")
    ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "pagamentos" (
    "id_pagamento" INTEGER NOT NULL,
    "id_pedido" INTEGER NOT NULL,
    "forma_pagamento" VARCHAR(30) NOT NULL,
    "valor" NUMERIC(10,2) NOT NULL,
    "status" VARCHAR(30) NOT NULL DEFAULT 'pendente',
    "data" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY("id_pagamento"),

    FOREIGN KEY ("id_pedido") REFERENCES "pedidos"("id_pedido")
    ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "entregas" (
    "id_entrega" INTEGER NOT NULL,
    "id_pedido" INTEGER NOT NULL,
    "saida" DATETIME NOT NULL,
    "entrega" DATETIME NOT NULL,
    "status" VARCHAR(30) NOT NULL DEFAULT 'pendente',
    "taxa" NUMERIC(10,2) NOT NULL,
    PRIMARY KEY("id_entrega"),
    FOREIGN KEY ("id_pedido") REFERENCES "pedidos"("id_pedido")
    ON UPDATE NO ACTION ON DELETE NO ACTION
);

