from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import urllib.parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

url = 'https://pec.ac.in'
response = requests.get(url, headers=headers)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
text = soup.get_text()

print(text)
