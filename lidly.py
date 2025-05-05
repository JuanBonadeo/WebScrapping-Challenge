
#################################
########### CONDICIONES PARA EL CHALLENGE || Fecha de entrega tentativa lunes 05/05 & Catch up point Miércoles 30/04 14hs
#################################
# CREAR 3 - 5 SCRAPERS
# De 3 - 5 cadenas líderes de Estados Unidos (Florida)
# BUSQUEN
#     1. STORES
#         mandatorios:    
#             1.1. Dirección si no es online
#             1.2. Geoloc (lat y lon)
#         deseables:
#             1.1. Ciudad
#             1.2. Región
#             1.3. datos adicionales de la tienda (telefono / codigo postal / horario)
        
#     2. ITEMS
#     mandatorios:    
#         1.1. EAN o GTIN 13 || UPC o GTIN - 12 (identificarlo en el titulo si es GTIN-12)
#         1.2. Item name
#     deseables:
#         1.1. UOMs (Unit of measure - unidades de medida || height, width, length & weight/volume)
#     3. PRICES (PREFERIBLEMENTE PRECIO POR Punto de venta (tienda))
#         mandatorios:    
#             1.1. Price
#         deseables:
#             1.1. List price
#             1.2. Price per PoS (point of sale)
#             1.3. Promotions
#             1.4. Stock (CUIDADO!)

# Pointers:
#     - Cuidado con Walmart!
#     - En primera instancia buscar e investigar las cadenas existentes
#     - Exportar el resultado a CSV
#     - Exportar, en caso de que haya precios por PDV, con exportar 3 tiendas, está bien. 
#         for index, row in df_stores[:3].iterrows():
    
    
    
    
    
    
    
    
# tengo un total de:
    # -6502 productos
    # -185 stores
    # -336 categorias


import requests
import pandas as pd
import json



#--------------------------------------------STORES--------------------------------------------------------

def fetch_stores():
    url = 'https://mobileapi.lidl.com/v1/stores'
    
    
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://www.lidl.com/stores',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
    }
    
    response = requests.get(url, headers=headers)
    
    
    stores_json_response = response.json()
    
    stores_dict_list = []
    states_dict_list = {
        "AL": "Alabama",
        "AK": "Alaska",
        "AZ": "Arizona",
        "AR": "Arkansas",
        "CA": "California",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DE": "Delaware",
        "FL": "Florida",
        "GA": "Georgia",
        "HI": "Hawaii",
        "ID": "Idaho",
        "IL": "Illinois",
        "IN": "Indiana",
        "IA": "Iowa",
        "KS": "Kansas",
        "KY": "Kentucky",
        "LA": "Louisiana",
        "ME": "Maine",
        "MD": "Maryland",
        "MA": "Massachusetts",
        "MI": "Michigan",
        "MN": "Minnesota",
        "MS": "Mississippi",
        "MO": "Missouri",
        "MT": "Montana",
        "NE": "Nebraska",
        "NV": "Nevada",
        "NH": "New Hampshire",
        "NJ": "New Jersey",
        "NM": "New Mexico",
        "NY": "New York",
        "NC": "North Carolina",
        "ND": "North Dakota",
        "OH": "Ohio",
        "OK": "Oklahoma",
        "OR": "Oregon",
        "PA": "Pennsylvania",
        "RI": "Rhode Island",
        "SC": "South Carolina",
        "SD": "South Dakota",
        "TN": "Tennessee",
        "TX": "Texas",
        "UT": "Utah",
        "VT": "Vermont",
        "VA": "Virginia",
        "WA": "Washington",
        "WV": "West Virginia",
        "WI": "Wisconsin",
        "WY": "Wyoming",
        # Territorios (opcional)
        "PR": "Puerto Rico",
        "DC": "District of Columbia"
    }
    
    
    try:
        stores_data = stores_json_response['results']
        for store in stores_data:
            store_dict = {
            'address' : store['address']['street'],
            'city' : store['address']['city'],
            'region': states_dict_list[ store['address']['state'] ],
            'latitud' : store.get('coordinates', None).get('lat', None),
            'longitud' : store.get('coordinates', None).get('lon', None),
            'store_id' : store['id'],
            'store_name' : store['name'],
            }
            stores_dict_list.append(store_dict) 
            stores_df = pd.DataFrame(stores_dict_list)
            stores_df.drop_duplicates(subset='store_name', inplace=True)
    except Exception as e:
        print(f'El error es: {e}')
    return stores_df


df_stores = fetch_stores()


#--------------------------------------------CATEGORIES--------------------------------------------------------


def fetch_categories():
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://www.lidl.com/products?category=all&sort=productAtoZ',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
    }
    
    params = {
        'sort': 'productAtoZ',
    }
    
    response = requests.get('https://mobileapi.lidl.com/v1/categories', params=params, headers=headers)
    
    
    categories_data = response.json()
    
    
    categories_dict_list = []
    
    
    try:
        for category in categories_data:
            if category.get('parents') is None:
                category_dict = {
                    'code': category.get('code'),
                    'name': category.get('name', {}).get('en', ''),
                }
                categories_dict_list.append(category_dict)
       
                categories_df = pd.DataFrame(categories_dict_list)
                categories_df.drop_duplicates(subset='name', inplace=True)
            
    except Exception as e:
        print(f'El error es: {e}')
    return categories_df


df_categories = fetch_categories()


























