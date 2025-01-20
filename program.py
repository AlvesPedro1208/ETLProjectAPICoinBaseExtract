import requests
import json

URL = 'https://api.exchange.coinbase.com/currencies'

response = requests.get(URL)

if response.status_code == 200:
    products = response.json()

    #Filtragem de campos necessários
    filtered_products = []
    for product in products:
        filtered_products.append({
            'id': product.get('ID'),
            'name': product.get('name'),
            'min_size': product.get('min_size'),
            'type': product.get('details').get('type'),
            'default_network': product.get('default_network'),
            'display_name': product.get('display_name')
        })

    #Exibição dos dados filtrados
    print(json.dumps(filtered_products, indent=4))
else:
    print(f'Erro ao obter dados: {response.status_code}')


