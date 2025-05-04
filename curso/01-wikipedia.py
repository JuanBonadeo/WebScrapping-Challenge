import requests
from lxml import html

url = "https://www.wikipedia.org/"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)

parser = html.fromstring(response.text)
print(response.status_code)