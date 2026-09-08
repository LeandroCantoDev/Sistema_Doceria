import json


try:
    with open('products.json', 'r') as arquivo:
        products = json.load(arquivo)
except FileNotFoundError:
    products = []
client = []
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
def search_client(clients, client_name):
    for client in clients:
        if client['name'] == client_name:
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
    name = input("Digite o produto: ")
    price = float(input("Digite o preço: "))
    register_product(products, name, price)

    other_product = input("Gostaria de adicionar mais um produto? ").upper()
    if not other_product.startswith('S'):
        break


client_name = input('Digite o nome do cliente: ')
register_client(client, client_name)
client_found = search_client(client, client_name)
order['client'] = client_found


while True:
    more_something = input('Gostaria de adicionar um produto? ').upper()
    if more_something.startswith('N'):
        break
    else:
        product = input('Digite o nome do produto: ')
    product_found = search_product(products, product)
    if product_found is None:
        print("Produto não existe")
        continue
    quantity = int(input("Digite a quantidade: "))
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

print(order)

with open('products.json', 'w') as arquivo:
    json.dump(products, arquivo)
