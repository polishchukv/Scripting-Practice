import requests
from bs4 import BeautifulSoup

url = 'https://acloudguru.com/pricing'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
