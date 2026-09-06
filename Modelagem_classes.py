products = []
client = []
order = {
    'client': {},
    'items': []
}

# -------- REGISTER PRODUCT -------- #
name = input("Digite o nome do produto: ")    #'Digit the product name'
price = float(input('Digite o valor do produto: '))    # 'Digit the product value'
def register_product(products, name, price):
    products.append({'name': name, 'price': price})

register_product(products, name, price)
# print(produtos)


#--------- SEARCH PRODUCT ----------#
def search_products(products, name):
    for product in products:
        if product['name']  == name:
            return product
product_found = search_products(products, name)
print(product_found)


# -------- REGISTER CUSTOMER -------- #
client_name = input('Digite o nome do cliente: ' )   #'Digit the client name'
def register_customer(client, client_name):
    client.append({'name': client_name})
register_customer(client, client_name)


#------- SEARCH CLIENT --------
def search_client(clients, client_name):
    for client in clients:
        if client['name'] == client_name:
            return client
client_found = search_client(client, client_name)
print(client_found)
order['client'] = client_found


#--------- ADD ITEM----------#
quantity = int(input('Digite a quantidade do item: '))         #'Digit the quantity item'
def add_item(order, product, quantity):
    order['items'].append({'product': product, 'quantity': quantity})


add_item(order, product_found, quantity)
print(client)
print(order)