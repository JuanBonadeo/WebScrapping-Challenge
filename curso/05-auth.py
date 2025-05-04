import requests 
from lxml import html

import json

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

url = 'https://github.com/login'

session = requests.Session()

response = session.get(url, headers = headers)
print(response.text, )