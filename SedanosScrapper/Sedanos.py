

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
    



# traer 100 prductos de 1 categoria

# import requests
# import pandas as pd
# import json


# def fetch_100P():
#     headers = {
#         'accept': 'application/json, text/javascript, */*; q=0.01',
#         'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#         'dnt': '1',
#         'origin': 'https://www.sedanos.com',
#         'priority': 'u=1, i',
#         'referer': 'https://www.sedanos.com/shop/meat/d/22394618',
#         'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'cross-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
#     }
    
#     params = {
#         'app_key': 'sedanos',
#         'department_id': '22394618',
#         'department_id_cascade': 'true',
#         'fields': 'id,identifier,upc,name,store_id,department_id,size,popularity,quantity_step,quantity_minimum,quantity_initial,quantity_label,quantity_label_singular,varieties,quantity_size_ratio_description,status,status_id,sale_configuration_type_id,fulfillment_type_id,fulfillment_type_ids,other_attributes,clippable_offer,slot_message,call_out,has_featured_offer,tax_class_label,promotion_text,sale_offer,store_card_required,average_rating,review_count,like_code,shelf_tag_ids,offers,is_place_holder_cover_image,video_config,enforce_product_inventory,disallow_adding_to_cart,substitution_type_ids,unit_price,offer_sale_price,canonical_url,offered_together,sequence',
#         'include_offered_together': 'true',
#         'limit': '100',
#         'popularity_sort': 'asc',
#         'render_id': '1745763999375',
#         'sort': 'popularity',
#         'store_id': '5761',
#         'token': 'cb1b0701f3e646bbe5c9e0518addcfc4',
#     }
    
#     response = requests.get('https://api.freshop.com/1/products', params=params, headers=headers)
    
#     products_json_response = response.json()
    
#     products_dict_list = []
    
#     products_data = products_json_response['items']
    
#     for product in products_data:
#         product_dict = {
#         'product_id': product['id'],
#         'upc': product['upc'],
#         'product_name': product['name'],
#         'unit_price' : product['']
#         'popularirty': product
#         }
#         products_dict_list.append(product_dict)
        
#     product_df = pd.DataFrame(products_dict_list)
#     product_df.drop_duplicates(subset='product_id', inplace=True)
#     return product_df
# product_df = fetch_100P()












import requests
import pandas as pd
import json
import time
import random
import concurrent.futures



def fetch_stores():
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://www.sedanos.com/store-locator',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
    }
    
    params = {
        'app_key': 'sedanos',
        'has_address': 'true',
        'limit': '-1',
        'token': 'cb1b0701f3e646bbe5c9e0518addcfc4',
    }
    
    response = requests.get('https://api.freshop.com/1/stores', params=params, headers=headers)
    
    stores_json_response = response.json()
    
    stores_dict_list = []
    
    stores_data = stores_json_response['items']
    for store in stores_data:
        store_dict = {
        'address' : store['address_1'],
        'city' : store['city'],
        'latitude' : store['longitude'],
        'longitude' : store['latitude'],
        'store_id' : store['id'],
        'store_number' : store['store_number'],
        }
        stores_dict_list.append(store_dict) 
    stores_df = pd.DataFrame(stores_dict_list)
    stores_df.drop_duplicates(subset='store_number', inplace=True)
    print("Finished fetching stores.")
    return stores_df

df_stores = fetch_stores()
    


def fetch_categories():
    print("Fetching categories...")
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'dnt': '1',
        'origin': 'https://www.sedanos.com',
        'priority': 'u=1, i',
        'referer': 'https://www.sedanos.com/shop/catering/d/22571166',
        'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    }
    
    params = {
        'app_key': 'sedanos',
        'custom_filter_id_cascade': 'false',
        'department_id_cascade': 'false',
        'include_custom_filters': 'false',
        'include_departments': 'true',
        'include_offered_together': 'true',
        'include_shelf_tags': 'false',
        'include_tags': 'false',
        'limit': '0',
        'render_id': '1745762834459',
        'token': 'cb1b0701f3e646bbe5c9e0518addcfc4',
    }
    
    response = requests.get('https://api.freshop.com/1/products', params=params, headers=headers)
    
    categories_json_response = response.json()
    
    categories_dict_list = []
    
    categories_data = categories_json_response['departments']
    
    for category in categories_data:
        if (category.get('parent_id', None) == '22394611' and category.get('id') != '22394619'):
            category_dict = {
            'category_id': category['id'],
            'category_name': category['name'],
            'total_products': int(category['count'])
            }
            categories_dict_list.append(category_dict)
        
    categories_df = pd.DataFrame(categories_dict_list)
    categories_df.drop_duplicates(subset='category_id', inplace=True)
    print("Finished fetching categories.")
    return categories_df


df_categories = fetch_categories()

LIMIT = 100  

def fetch_products_in_category(row, store_id, token='cb1b0701f3e646bbe5c9e0518addcfc4'):
    cat_id = row['category_id']
    total_products = row['total_products']
    cat_name = row['category_name']
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'dnt': '1',
        'origin': 'https://www.sedanos.com',
        'priority': 'u=1, i',
        'referer': f'https://www.sedanos.com/shop/{cat_name}/d/{cat_id}',
        'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    }

    all_products = []
    skip = 0

    while True:
        params = {
            'app_key': 'sedanos',
            'department_id': cat_id,
            'department_id_cascade': 'true',
            'fields': 'id, identifier, upc, name, store_id, department_id, size,popularity, canonical_url, varieties,quantity_size_ratio_description,status,status_id,other_attributes,average_rating,review_count,unit_price,offer_sale_price',  
            'include_offered_together': 'true',
            'limit': str(LIMIT),
            'popularity_sort': 'asc',
            'render_id': '1745763999375',
            'sort': 'popularity',
            'store_id': store_id,
            'token': token,
            'skip': str(skip),
        }

        try:
            response = requests.get('https://api.freshop.com/1/products', params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            products = data.get('items', [])
            all_products.extend(products)
            print(f'✅ Obtenidos {len(products)} productos de la categoría {cat_name} con skip {skip}')
        except Exception as e:
            print(f'❌ Error al obtener productos de la categoría {cat_name} con skip {skip}: {e}')
            break

        
        if len(products) < LIMIT:
            print(f'🛑 Ya no hay más productos para la categoría {cat_name}')
            break

        skip += LIMIT

        sleep_time = random.randint(15, 35)
        print(f'⏳ Esperando {sleep_time}s antes del próximo request...')
        time.sleep(sleep_time)

    return all_products




def fetch_all_item_info(df_categories, max_workers=5):
    print('Fetching items info...')
    item_info_list = []
    # Crea el grupo de hilos
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        #Crea las tareas par cada categoria
        futures = [executor.submit(fetch_products_in_category, row, '5761') for _, row in df_categories.iterrows()]
        
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            try:
                result = future.result()
                item_info_list.extend(result)
                print(f'Completed {i+1}/{len(futures)}')
            except Exception as e:
                print(f"Error in thread: {e}")

    print('Finished fetching item info.')
    return item_info_list

def fetch_prices_for_stores(df_categories, store_ids, max_workers=5):
    prices_list = []
    tasks = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for store_id in store_ids:
            print(f'Fetching prices for store {store_id}...')
            for _, row in df_categories.iterrows():
                tasks.append(executor.submit(fetch_products_in_category, row, store_id))

        for i, future in enumerate(concurrent.futures.as_completed(tasks)):
            try:
                result = future.result()
                prices_list.extend(result)
                print(f'Completed {i+1}/{len(tasks)}')
            except Exception as e:
                print(f"Error in thread: {e}")

    print('Finished fetching prices for all stores.')
    return prices_list

#'id, identifier, upc, name, store_id, department_id, size,popularity, canonical_url,quantity_size_ratio_description,status,status_id,other_attributes,average_rating,review_count,unit_price,offer_sale_price'
def parse_products_data(responses_list):
    print('Starting products-parsing...')
    item_dict_list = []
    for product in responses_list:
        name = product.get('name', None)
        id = product.get('id', None)
        upc = product.get('upc', None)
        category = product.get('category_id')
        size = product.get('size', None)
        url = product.get('canonical_url', None)
        status = product.get('status', None)

        item_dict = {
            'id': id,
            'name': name,
            'upc': upc,
            'category': category,
            'size': size,
            'url': url,
            'status': status,
        }
        
        item_dict_list.append(item_dict)
        

    print(f'Parsed {len(item_dict_list)} items.')
    return item_dict_list

def parse_prices_data(responses_list):
    print('Starting prices-parsing...')
    prices_dict_list = []
    for product in responses_list:
        product_id = product.get('id', None)
        product_upc = product.get('upc', None)
        unit_price = product.get('unit_price')
        sale_price = product.get('offer_sale_price')
        store_id = product.get('store_id', None)
        item_dict = {
            'product_id': product_id,
            'unit_price': unit_price,
            'sale_price': sale_price,
            'store_id': store_id
        }
        
        prices_dict_list.append(item_dict)
        

    print(f'Parsed {len(item_dict_list)} items.')
    return prices_dict_list






item_info_list = fetch_all_item_info( df_categories, 5)
item_dict_list = parse_products_data(item_info_list)
df_items = pd.DataFrame(item_dict_list)
df_items.to_csv('productos.csv', index=False)

stores_ids = ['5762', '5761', '5760']
prices_info_list = fetch_prices_for_stores(df_categories, stores_ids, 5)
prices_dict_list = parse_prices_data(prices_info_list)
df_prices = pd.DataFrame( prices_dict_list )
df_prices.to_csv('precios.csv', index=False)


