import requests
import pandas as pd
import json
import time
import random
import concurrent

def fetch_stores():
    cookies = {
        'csm-sid': '918-1782596-5487095',
        'cwr_u': '64f3bde1-cb48-4a14-87f2-9a4fdcd59116',
        'session-id': '135-5565599-9128112',
        'session-id-time': '2082787201l',
        '_gcl_au': '1.1.940198342.1745948856',
        'ubid-main': '135-4690566-1873008',
        'wfm_store_d8': 'eyJpZCI6IjEwNDc4IiwibmFtZSI6IlRhbGxhaGFzc2VlIiwidGxjIjoiVExIIiwicGF0aCI6InRhbGxhaGFzc2VlIiwic3RhdGUiOiJGTCIsInN0b3JlX25pZCI6IiIsInN0YXJ0X2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJ1cGRhdGVkX2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJnZW9tZXRyeSI6eyJjb29yZGluYXRlcyI6Wy04NC4yNjk5MTgsMzAuNDYyOTgxXSwidHlwZSI6IlBvaW50In19',
        'session-token': 'GafFaL1GLJrpRZ5wOS3JexyG4QPsebirp14Fb1gT/qqdITuAIpCtZ/f4ZaQ32fxQnZE8QqIgcRxeaw7uzJRKzp042LVftpf4EGtJUO3bLs6Jeup0SMFiUrACOMVEH58/DYr9NTEHBp9x6kDFGn88j1fv2zxhjVun6mSfKxNBiX7rFkdDKOsEioxtzgrbURKele4hGy0P/FbonWCNF0IDH444EZ7sRTheq6GblKdADQpyCtpMsAVmIvZWkX30UYNKYlnXDL1Uh9O5bVUN8PeJrdrpWZpPMXTCeHvkTtartEaA7lcrkTXKnTMCxrehrmzlJNiIGQsHn83TDKaqCtjnXA==',
        'cwr_s': 'eyJzZXNzaW9uSWQiOiI4ZmE1NjQ5MC0yOTQwLTQzMzItOGNiYS0xMDY0MDNhZjk0NTAiLCJyZWNvcmQiOmZhbHNlLCJldmVudENvdW50IjoxMzQxLCJwYWdlIjp7InBhZ2VJZCI6Ii9wcm9kdWN0LzM2NS1ieS13aG9sZS1mb29kcy1tYXJrZXQtZnJvemVuLXdpbGRjYXVnaHQtc2VhZm9vZC12YWx1ZS1wYWNrLXNvY2tleWUtc2FsbW9uLWZpbGxldHMtYjA3bnJjcnpmZiIsInBhcmVudFBhZ2VJZCI6Ii9wcm9kdWN0cy9zZWFmb29kIiwiaW50ZXJhY3Rpb24iOjE2LCJyZWZlcnJlciI6IiIsInJlZmVycmVyRG9tYWluIjoiIiwic3RhcnQiOjE3NDU5NTQ0Nzg0OTd9fQ==',
    }
    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=utf-8',
        'DNT': '1',
        'Origin': 'https://www.wholefoodsmarket.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.wholefoodsmarket.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'anti-csrftoken-a2z': 'gwvPkdVTZCot5RmVuZnSmXs8B+T3DK0Cf+T1FX2vZ5tuAAAAAQAAAABoES4JcmF3AAAAACr/Igfie4qiUf9rqj+gAw==',
        'device-memory': '8',
        'downlink': '4.15',
        'dpr': '1.25',
        'ect': '4g',
        'rtt': '200',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1.25',
        'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-ch-viewport-width': '712',
        'viewport-width': '712',
        # 'Cookie': 'csm-sid=918-1782596-5487095; cwr_u=64f3bde1-cb48-4a14-87f2-9a4fdcd59116; session-id=135-5565599-9128112; session-id-time=2082787201l; _gcl_au=1.1.940198342.1745948856; ubid-main=135-4690566-1873008; wfm_store_d8=eyJpZCI6IjEwNDc4IiwibmFtZSI6IlRhbGxhaGFzc2VlIiwidGxjIjoiVExIIiwicGF0aCI6InRhbGxhaGFzc2VlIiwic3RhdGUiOiJGTCIsInN0b3JlX25pZCI6IiIsInN0YXJ0X2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJ1cGRhdGVkX2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJnZW9tZXRyeSI6eyJjb29yZGluYXRlcyI6Wy04NC4yNjk5MTgsMzAuNDYyOTgxXSwidHlwZSI6IlBvaW50In19; session-token=GafFaL1GLJrpRZ5wOS3JexyG4QPsebirp14Fb1gT/qqdITuAIpCtZ/f4ZaQ32fxQnZE8QqIgcRxeaw7uzJRKzp042LVftpf4EGtJUO3bLs6Jeup0SMFiUrACOMVEH58/DYr9NTEHBp9x6kDFGn88j1fv2zxhjVun6mSfKxNBiX7rFkdDKOsEioxtzgrbURKele4hGy0P/FbonWCNF0IDH444EZ7sRTheq6GblKdADQpyCtpMsAVmIvZWkX30UYNKYlnXDL1Uh9O5bVUN8PeJrdrpWZpPMXTCeHvkTtartEaA7lcrkTXKnTMCxrehrmzlJNiIGQsHn83TDKaqCtjnXA==; cwr_s=eyJzZXNzaW9uSWQiOiI4ZmE1NjQ5MC0yOTQwLTQzMzItOGNiYS0xMDY0MDNhZjk0NTAiLCJyZWNvcmQiOmZhbHNlLCJldmVudENvdW50IjoxMzQxLCJwYWdlIjp7InBhZ2VJZCI6Ii9wcm9kdWN0LzM2NS1ieS13aG9sZS1mb29kcy1tYXJrZXQtZnJvemVuLXdpbGRjYXVnaHQtc2VhZm9vZC12YWx1ZS1wYWNrLXNvY2tleWUtc2FsbW9uLWZpbGxldHMtYjA3bnJjcnpmZiIsInBhcmVudFBhZ2VJZCI6Ii9wcm9kdWN0cy9zZWFmb29kIiwiaW50ZXJhY3Rpb24iOjE2LCJyZWZlcnJlciI6IiIsInJlZmVycmVyRG9tYWluIjoiIiwic3RhcnQiOjE3NDU5NTQ0Nzg0OTd9fQ==',
    }
    
    json_data = {
        'query': [
            'AYAAFLLv1MlW0bLHEPQJVSCZNjsALgACABFvcmlnaW5hbEZpZWxkTmFtZQAFcXVlcnkADWZyYWdtZW50SW5kZXgAATAAAQAGc2k6bWQ1ACBjNjEyNzMwZmM4NzA0NjYyMThkZjRiMjc1YWFlYTJiNQEAX+Z4M/HX954kofziREcEgpP9j2P70h0NkccygNGayJ+bghMAeLhsHSNstIRni3iPzOp9tXrP1E0oY3TOHDnXRsf1gzbSbQAZZQr4wTbs8f0kplwoGAfU62TUWlJkoySti8FLoZHtEA9aS35M8PaGtTDB2Vth7/3vfWv+z/3IEGNK3SVUsBWnp/953GQ9Ae2HWMA2ImwBiw7bbepZoTMz96bkJuq7sLcmLb+Q/XY2W4gbzLPILk/qF7fypgwG6Sx26Cqd0Sl3MWVF0u7Up4+6DxxuG4FaQQK9HnJlPrFI8DVsh9IDWiUqNJGPElnNYuoXQGOW1P6tz6La2vLYiHjsIAIAAAAADAAAACYAAAAAAAAAAAAAAACf2qxeEzQRCB7BT4h+utFF/////wAAAAEAAAAAAAAAAAAAAAEAAAAlrZLFkvcYlvrGJ3EmkYha2YlsDL776rLD+Skz4k6dGfjFUiqm7bRDSTpQLWgl4WBcOWz6tDc=',
        ],
    }
    
    response = requests.post('https://www.wholefoodsmarket.com/stores/search', cookies=cookies, headers=headers, json=json_data)
    
    
    stores_json_response = response.json()
    
    stores_dict_list = []
    
    stores_data = stores_json_response
    for store in stores_data:
        store_dict = {
        'address' : store['location']['address']['line1'],
        'state' : store['location']['address']['state'],
        'city' : store['location']['address']['city'],
        'latitude' : store['location']['geometry']['coordinates'][0],
        'longitude' : store['location']['geometry']['coordinates'][1],
        'store_id' : store['storeId'],
        }
        stores_dict_list.append(store_dict) 
    stores_df = pd.DataFrame(stores_dict_list)
    stores_df.drop_duplicates(subset='store_id', inplace=True)
    print("Finished fetching stores.")
    return stores_df

df_stores = fetch_stores()


def fetch_categories():
    cookies = {
        'csm-sid': '918-1782596-5487095',
        'cwr_u': '64f3bde1-cb48-4a14-87f2-9a4fdcd59116',
        'session-id': '135-5565599-9128112',
        'session-id-time': '2082787201l',
        '_gcl_au': '1.1.940198342.1745948856',
        'ubid-main': '135-4690566-1873008',
        'wfm_store_d8': 'eyJpZCI6IjEwNDc4IiwibmFtZSI6IlRhbGxhaGFzc2VlIiwidGxjIjoiVExIIiwicGF0aCI6InRhbGxhaGFzc2VlIiwic3RhdGUiOiJGTCIsInN0b3JlX25pZCI6IiIsInN0YXJ0X2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJ1cGRhdGVkX2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJnZW9tZXRyeSI6eyJjb29yZGluYXRlcyI6Wy04NC4yNjk5MTgsMzAuNDYyOTgxXSwidHlwZSI6IlBvaW50In19',
        'session-token': 'a9avGVfxvDEPMSqrzV5hfSTpKpuoH3hKpuNf+NW2blHpANqtwtCr58CVVmMX4tA767IfxGftwwH16lIoMwWw63dYTTO2zetL/cqJCTreB7dq+5cG6M1ip4nOmfzmoAmOx/6ua23+wI3bwRZ2tSvPT7z6jZZe9vaLdSctqj0GvTAKr98Cjwu4r8btrX67Ndz8kwnqtGE5XH4iuFsJmFq93w/VPnVDWtEoMLLznSrnrsTvZsufEQTEHneJEJ/9Br9qS/mbc7KghDs0aaT9Uh3YMU6+GjOvMDW/SQmvLsLLcgmq50Au+oirb+hQRcoSgLrZwrFkwGdbIgWzWXni68MzTg==',
        'cwr_s': 'eyJzZXNzaW9uSWQiOiI4ZmE1NjQ5MC0yOTQwLTQzMzItOGNiYS0xMDY0MDNhZjk0NTAiLCJyZWNvcmQiOmZhbHNlLCJldmVudENvdW50IjoxMDM1LCJwYWdlIjp7InBhZ2VJZCI6Ii9wcm9kdWN0cyIsInBhcmVudFBhZ2VJZCI6Ii9zYWxlcy1mbHllciIsImludGVyYWN0aW9uIjoxMSwicmVmZXJyZXIiOiJodHRwczovL3d3dy53aG9sZWZvb2RzbWFya2V0LmNvbS9zYWxlcy1mbHllcj9zdG9yZS1pZD0xMDQ3OCIsInJlZmVycmVyRG9tYWluIjoid3d3Lndob2xlZm9vZHNtYXJrZXQuY29tIiwic3RhcnQiOjE3NDU5NDk3MTUwMDl9fQ==',
    }
    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Pragma': 'no-cache',
        'Referer': 'https://www.wholefoodsmarket.com/products',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'device-memory': '8',
        'downlink': '10',
        'dpr': '1',
        'ect': '4g',
        'rtt': '150',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1',
        'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-ch-viewport-width': '1865',
        'viewport-width': '1865',
        'x-nextjs-data': '1',
        # 'Cookie': 'csm-sid=918-1782596-5487095; cwr_u=64f3bde1-cb48-4a14-87f2-9a4fdcd59116; session-id=135-5565599-9128112; session-id-time=2082787201l; _gcl_au=1.1.940198342.1745948856; ubid-main=135-4690566-1873008; wfm_store_d8=eyJpZCI6IjEwNDc4IiwibmFtZSI6IlRhbGxhaGFzc2VlIiwidGxjIjoiVExIIiwicGF0aCI6InRhbGxhaGFzc2VlIiwic3RhdGUiOiJGTCIsInN0b3JlX25pZCI6IiIsInN0YXJ0X2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJ1cGRhdGVkX2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJnZW9tZXRyeSI6eyJjb29yZGluYXRlcyI6Wy04NC4yNjk5MTgsMzAuNDYyOTgxXSwidHlwZSI6IlBvaW50In19; session-token=a9avGVfxvDEPMSqrzV5hfSTpKpuoH3hKpuNf+NW2blHpANqtwtCr58CVVmMX4tA767IfxGftwwH16lIoMwWw63dYTTO2zetL/cqJCTreB7dq+5cG6M1ip4nOmfzmoAmOx/6ua23+wI3bwRZ2tSvPT7z6jZZe9vaLdSctqj0GvTAKr98Cjwu4r8btrX67Ndz8kwnqtGE5XH4iuFsJmFq93w/VPnVDWtEoMLLznSrnrsTvZsufEQTEHneJEJ/9Br9qS/mbc7KghDs0aaT9Uh3YMU6+GjOvMDW/SQmvLsLLcgmq50Au+oirb+hQRcoSgLrZwrFkwGdbIgWzWXni68MzTg==; cwr_s=eyJzZXNzaW9uSWQiOiI4ZmE1NjQ5MC0yOTQwLTQzMzItOGNiYS0xMDY0MDNhZjk0NTAiLCJyZWNvcmQiOmZhbHNlLCJldmVudENvdW50IjoxMDM1LCJwYWdlIjp7InBhZ2VJZCI6Ii9wcm9kdWN0cyIsInBhcmVudFBhZ2VJZCI6Ii9zYWxlcy1mbHllciIsImludGVyYWN0aW9uIjoxMSwicmVmZXJyZXIiOiJodHRwczovL3d3dy53aG9sZWZvb2RzbWFya2V0LmNvbS9zYWxlcy1mbHllcj9zdG9yZS1pZD0xMDQ3OCIsInJlZmVycmVyRG9tYWluIjoid3d3Lndob2xlZm9vZHNtYXJrZXQuY29tIiwic3RhcnQiOjE3NDU5NDk3MTUwMDl9fQ==',
    }
    
    params = {
        'store': '10478',
    }
    
    response = requests.get(
        'https://www.wholefoodsmarket.com/_next/data/Ncw9ULavm0ZnyLSw84ld-/products.json',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    
    response_json = response.json()
    
    categories_data = response_json['pageProps']['data']['facets'][0]['refinements']
    
    categories_dict_list = []
    
    
    for category in categories_data:
        if category['slug'] != 'all-products':
            category_dict = {
            'category_id': category['slug'],
            'category_name': category['label'],
            'total_products': int(category['count'])
            }
            categories_dict_list.append(category_dict)
        
    categories_df = pd.DataFrame(categories_dict_list)
    categories_df.drop_duplicates(subset='category_id', inplace=True)
    print("Finished fetching categories.")
    return categories_df

df_categories = fetch_categories()

def fetch_products_in_category(row, store_id):
    cat_id = row['category_id']
    total_products = row['total_products']
    cat_name = row['category_name']

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Referer': f'https://www.wholefoodsmarket.com/products/{cat_id}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'credentials': 'include',
        'device-memory': '8',
        'downlink': '9.95',
        'dpr': '1',
        'ect': '4g',
        'rtt': '150',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1',
        'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-ch-viewport-width': '1865',
        'viewport-width': '1865',
        # 'Cookie': 'csm-sid=918-1782596-5487095; cwr_u=64f3bde1-cb48-4a14-87f2-9a4fdcd59116; session-id=135-5565599-9128112; session-id-time=2082787201l; _gcl_au=1.1.940198342.1745948856; ubid-main=135-4690566-1873008; session-token=ykCGCBsaBlNeiSSlrFtiG95fniD2M5c8GmpjaeYpjlupZj0Tqnqn7ubnjiCpRpeJNvg5RzzvoVPGAsIGjeKpQ09aDnl8IiAYahXaPlr6UshoYQ6U7+5ExYELb6i55ajyX+fIC9njnivuXO/lczyFtvunAFxTQs0iw8g4Z3AoaWwAIp0mFia4hOSuLAULOZte29OcRNk0yWMWTG9uw0C3knW0IyHsLTMwQh9Zg9UnPpeAGpNvk4GfsKJEdcCqbNvS+enFZigwVjVysfkgth9T7hZ6CzqbYNRYN/EwVvI610wqso6tHjTDDrFYcuZDBrOWM8x69J11hBqpjB+wYzYkWA==; wfm_store_d8=eyJpZCI6IjEwNDc4IiwibmFtZSI6IlRhbGxhaGFzc2VlIiwidGxjIjoiVExIIiwicGF0aCI6InRhbGxhaGFzc2VlIiwic3RhdGUiOiJGTCIsInN0b3JlX25pZCI6IiIsInN0YXJ0X2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJ1cGRhdGVkX2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJnZW9tZXRyeSI6eyJjb29yZGluYXRlcyI6Wy04NC4yNjk5MTgsMzAuNDYyOTgxXSwidHlwZSI6IlBvaW50In19; cwr_s=eyJzZXNzaW9uSWQiOiI4ZmE1NjQ5MC0yOTQwLTQzMzItOGNiYS0xMDY0MDNhZjk0NTAiLCJyZWNvcmQiOmZhbHNlLCJldmVudENvdW50IjoyNjUsInBhZ2UiOnsicGFnZUlkIjoiL3Byb2R1Y3RzL2FsbC1wcm9kdWN0cyIsInBhcmVudFBhZ2VJZCI6Ii9wcm9kdWN0cyIsImludGVyYWN0aW9uIjoyLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3Lndob2xlZm9vZHNtYXJrZXQuY29tL3Byb2R1Y3RzIiwicmVmZXJyZXJEb21haW4iOiJ3d3cud2hvbGVmb29kc21hcmtldC5jb20iLCJzdGFydCI6MTc0NTk0ODk2MjE4Nn19',
    }
    
    cookies = {
        'csm-sid': '918-1782596-5487095',
        'cwr_u': '64f3bde1-cb48-4a14-87f2-9a4fdcd59116',
        'session-id': '135-5565599-9128112',
        'session-id-time': '2082787201l',
        '_gcl_au': '1.1.940198342.1745948856',
        'ubid-main': '135-4690566-1873008',
        'session-token': 'ykCGCBsaBlNeiSSlrFtiG95fniD2M5c8GmpjaeYpjlupZj0Tqnqn7ubnjiCpRpeJNvg5RzzvoVPGAsIGjeKpQ09aDnl8IiAYahXaPlr6UshoYQ6U7+5ExYELb6i55ajyX+fIC9njnivuXO/lczyFtvunAFxTQs0iw8g4Z3AoaWwAIp0mFia4hOSuLAULOZte29OcRNk0yWMWTG9uw0C3knW0IyHsLTMwQh9Zg9UnPpeAGpNvk4GfsKJEdcCqbNvS+enFZigwVjVysfkgth9T7hZ6CzqbYNRYN/EwVvI610wqso6tHjTDDrFYcuZDBrOWM8x69J11hBqpjB+wYzYkWA==',
        'wfm_store_d8': 'eyJpZCI6IjEwNDc4IiwibmFtZSI6IlRhbGxhaGFzc2VlIiwidGxjIjoiVExIIiwicGF0aCI6InRhbGxhaGFzc2VlIiwic3RhdGUiOiJGTCIsInN0b3JlX25pZCI6IiIsInN0YXJ0X2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJ1cGRhdGVkX2RhdGUiOiIyMDI1LTA0LTI5VDE3OjQ4OjI1LjU1MjU5ODA1OFoiLCJnZW9tZXRyeSI6eyJjb29yZGluYXRlcyI6Wy04NC4yNjk5MTgsMzAuNDYyOTgxXSwidHlwZSI6IlBvaW50In19',
        'cwr_s': 'eyJzZXNzaW9uSWQiOiI4ZmE1NjQ5MC0yOTQwLTQzMzItOGNiYS0xMDY0MDNhZjk0NTAiLCJyZWNvcmQiOmZhbHNlLCJldmVudENvdW50IjoyNjUsInBhZ2UiOnsicGFnZUlkIjoiL3Byb2R1Y3RzL2FsbC1wcm9kdWN0cyIsInBhcmVudFBhZ2VJZCI6Ii9wcm9kdWN0cyIsImludGVyYWN0aW9uIjoyLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3Lndob2xlZm9vZHNtYXJrZXQuY29tL3Byb2R1Y3RzIiwicmVmZXJyZXJEb21haW4iOiJ3d3cud2hvbGVmb29kc21hcmtldC5jb20iLCJzdGFydCI6MTc0NTk0ODk2MjE4Nn19',
    }
    all_products = []
    skip = 0
    LIMIT = 60
    
    
    while True:
        params = {
            'leafCategory': cat_id,
            'store': store_id,
            'limit': str(LIMIT),
            'offset': str(skip),
        }
        try:
            response = requests.get(f'https://www.wholefoodsmarket.com/api/products/category/{cat_id}',params=params,cookies=cookies,headers=headers,)
            response.raise_for_status()
            data = response.json()
            products = data.get('results', [])
            all_products.extend(products)
            print(f'✅ Obtenidos {len(products)} productos de la categoría {cat_name} con skip {skip}')
        except Exception as e:
            print(f'❌ Error al obtener productos de la categoría {cat_name} con skip {skip}: {e}')
            break

        # Si recibimos menos productos que el límite, ya no hay más productos
        if len(products) < LIMIT:
            print(f'🛑 Ya no hay más productos para la categoría {cat_name}')
            break

        skip += LIMIT

        # Pausa aleatoria para no abusar del servidor
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
        futures = [executor.submit(fetch_products_in_category, row, '10478') for _, row in df_categories.iterrows()]
        
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



item_info_list = fetch_all_item_info( df_categories)



def parse_item_data(responses_list):
    print('Starting item-parsing...')
    item_dict_list = []

    for product in responses_list:
        # Extracción de campos base
        brand = product.get('brand', None)
        image_thumbnail = product.get('imageThumbnail', None)
        is_local = product.get('isLocal', None)
        name = product.get('name', None)
        slug = product.get('slug', None)
        uom = product.get('uom', None)
        
        # Extraer ASIN del slug (última parte después del último '-')
        asin = slug.split('-')[-1] if slug else None

        item_dict = {
            'brand': brand,
            'image_thumbnail': image_thumbnail,
            'is_local': is_local,
            'name': name,
            'slug': slug,
            'uom': uom,
            'asin': asin  # Nuevo campo añadido
        }

        item_dict_list.append(item_dict)

    print(f'Parsed {len(item_dict_list)} items.')
    return item_dict_list



def parse_prices_data(responses_list):
    print('Starting prices-parsing...')
    prices_dict_list = []
    for product in responses_list:
        name = product.get('name', None)
        regular_price = product.get('regularPrice', None)
        slug = product.get('slug', None)
        store = product.get('store', None)
        item_dict = {
            'name': name,
            'regular_price': regular_price,
            'slug': slug,
            'store': store,
        }
        
        prices_dict_list.append(item_dict)
        

    print(f'Parsed {len(item_dict_list)} items.')
    return prices_dict_list




item_dict_list = parse_item_data(item_info_list)
df_items = pd.DataFrame(item_dict_list)
df_items.to_csv('productos.csv', index=False)


stores_ids = ['10478','10704','10621']
prices_info_list = fetch_prices_for_stores(df_categories, stores_ids, 5)
prices_dict_list = parse_prices_data(prices_info_list)
df_prices = pd.DataFrame(prices_dict_list)
df_prices.to_csv('precios.csv', index=False)















