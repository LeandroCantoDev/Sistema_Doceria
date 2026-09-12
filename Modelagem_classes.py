import json


try:
    with open('products.json', 'r') as arquivo:
        products = json.load(arquivo)
except FileNotFoundError:
    products = []


try: 
    with open('client.json', 'r') as arquivo:
        client = json.load(arquivo)
except FileNotFoundError:
    client = []

try:
    with open('orders.json', 'r') as arquivo:
        orders = json.load(arquivo)
except FileNotFoundError:
    orders = []

order = {
    'client': {},
    'items': [],
    'boleto': {},
}


# -------- REGISTER PRODUCT -------- #
def register_product(products, name, price):
    products.append({'name': name, 'price': price})


#--------- SEARCH PRODUCT ----------#
def search_product(products, name):
    for product in products:
        if product['name']  == name:
            return product


# -------- REGISTER CLIENT -------- #
def register_client(client, client_name):
    client.append({'name': client_name})


#------- SEARCH CLIENT --------
def search_client(clients, name):
    for client in clients:
        if client['name'] == name:
            return client


#--------- ADD ITEM----------#
def add_item(order, product, quantity):
    order['items'].append({'product': product, 'quantity': quantity})


# ------- GENERATE SUMMARY -------- #
def generate_summary(order):
    print(order['client']['name'])
    total = 0
    for item in order['items']:
        subtotal = item['product']['price'] * item['quantity']
        print(item['product']['name'], 'x', item['quantity'], '=', subtotal )
        total += subtotal
    print('O total do pedido é: ', total)     # 'The total order is: '


while True:
    print()
    print('Escolha uma ação que queira realizar')
    print('1 Cadastrar produto')
    print('2 Cadastrar cliente')
    print('3 Realizar pedido')
    print('4 Ver últimos pedidos')
    print('5 Sair')
    print()
    select = input()

    if select == '1':

        while True:
            name = input("Digite o produto: ")
            if name == '':
                print("Digite o produto corretamente")  
                continue      
            product_found = search_product(products, name)
            if product_found is None:
                while True:
                    try:
                        price = float(input("Digite o preço: "))
                        break
                    except ValueError:
                        print('Digite o preço com números.')
                        continue
                register_product(products, name, price)
            else:
                print('Produto já existe ')
            
            other_product = input("Gostaria de adicionar mais um produto? ").upper()
            if not other_product.startswith('S'):
                break
        with open('products.json', 'w') as arquivo:
            json.dump(products, arquivo)

    elif select == '2':    
        while True:  
            client_name = input('Digite o nome do cliente: ')
            if client_name == '':
                print("Digite o nome corretamente")  
                continue 
            register_client(client, client_name)
            with open('client.json', 'w') as arquivo:
                json.dump(client, arquivo)
            break

    elif select == '3':
        client_name = input('Digite o nome do cliente: ')
        client_found = search_client(client, client_name)
        order['client'] = client_found
        if client_found is None:
            print("Cliente não existe, por favor adicione em registrar clientes.")
            continue
        print()
        for product in products:
            print(product['name'], product['price'])
        print()
        while True:
            more_something = input('Gostaria de selecionar um produto? ').upper()
            if more_something.startswith('N'):
                break
            else:
                product = input('Digite o nome do produto: ')
            product_found = search_product(products, product)
            if product_found is None:
                print("Produto não existe")
                continue
            while True:
                try:
                    quantity = int(input("Digite a quantidade: "))
                    break
                except ValueError:
                    print('Digite a quantidade em números.')
                    continue
            add_item(order, product_found, quantity)
        print()
        print('Resumo da compra:')
        generate_summary(order)
        print()
        print('Fazer boleto?')
        print("Sim / Não")
        boleto = input("Fazer boleto? ").upper()
        if boleto.startswith("S"):
            answer = True
        else:
            answer = False
        order['boleto'] = answer
        print()
        orders.append(order)

        with open('orders.json', 'w') as arquivo:
            json.dump(orders, arquivo)

    elif select == '4':
        for x in orders[-10:]:
            generate_summary(x)
            print()
    elif select == '5':
        print('Sair')
        break
    else:
        print('Digite uma opção válida')
