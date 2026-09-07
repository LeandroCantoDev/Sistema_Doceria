products = []
client = []
order = {
    'client': {},
    'items': [],
    'boleto': {}
}

# -------- REGISTER PRODUCT -------- #
name = input("Digite o nome do produto: ")    #'Type the product name'
price = float(input('Digite o valor do produto: '))    # 'Type the product value'
def register_product(products, name, price):
    products.append({'name': name, 'price': price})

register_product(products, name, price)
# print(produtos)


#--------- SEARCH PRODUCT ----------#
def search_product(products, name):
    for product in products:
        if product['name']  == name:
            return product
product_found = search_product(products, name)
print(product_found)


# -------- REGISTER CLIENT -------- #
client_name = input('Digite o nome do cliente: ' )   #'Type the client name'
def register_client(client, client_name):
    client.append({'name': client_name})
register_client(client, client_name)


#------- SEARCH CLIENT --------
def search_client(clients, client_name):
    for client in clients:
        if client['name'] == client_name:
            return client
client_found = search_client(client, client_name)
print(client_found)
order['client'] = client_found


#--------- ADD ITEM----------#
quantity = int(input('Digite a quantidade do item: '))         #'Type the item quantity'
def add_item(order, product, quantity):
    order['items'].append({'product': product, 'quantity': quantity})


add_item(order, product_found, quantity)
# print(client)
print(order)


# ------- GENERATE SUMMARY -------- #
def generate_summary(order):
    print(order['client']['name'])
    total = 0
    for item in order['items']:
        subtotal = item['product']['price'] * item['quantity']
        print(item['product']['name'], 'x', item['quantity'], '=', subtotal )
        total += subtotal
    print('O total do pedido é: ', total)     # The total order is  

generate_summary(order)


boleto = input('Fazer boleto? Sim ou Não: ').upper()
if boleto.startswith('S'):
    print('Fazer boleto')
    answer = True
else:
    print('Não fazer boleto')
    answer = False
order['boleto'] = answer
print(answer)
print(order)