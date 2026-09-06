produtos = []
cliente = []
pedido = {
    'cliente': {},
    'itens': []
}

# -------- CADASTRO PRODUTO -------- #
nome = input("Digite o nome do produto: ")
preco = float(input('Digite o valor do produto: '))
def cadastrar_produto(produtos, nome, preco):
    produtos.append({'nome': nome, 'preco': preco})

cadastrar_produto(produtos, nome, preco)
# print(produtos)


#--------- BUSCA PRODUTO ----------#
def buscar_produto(produtos, nome):
    for produto in produtos:
        if produto['nome']  == nome:
            return produto
produto_encontrado = buscar_produto(produtos, nome)
print(produto_encontrado)


# --------CADASTRO CLIENTE-------- #
nome_cliente = input('Digite o nome do cliente: ' )
def cadastrar_cliente(cliente, nome_cliente):
    cliente.append({'nome': nome_cliente})
cadastrar_cliente(cliente, nome_cliente)


#------- BUSCAR CLIENTE--------
def buscar_cliente(clientes, nome_cliente):
    for cliente in clientes:
        if cliente['nome'] == nome_cliente:
            return cliente
cliente_encontrado = buscar_cliente(cliente, nome_cliente)
print(cliente_encontrado)
pedido['cliente'] = cliente_encontrado


#--------- ADICIONAR ITEM----------#
quantidade = int(input('Digite a quantidade do item: '))
def adicionar_item(pedido, produto, quantidade):
    pedido['itens'].append({'produto': produto, 'quantidade': quantidade})
    # pedido['cliente'] = cliente_encontrado

adicionar_item(pedido, produto_encontrado, quantidade)
print(cliente)
print(pedido)