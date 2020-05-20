import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.benzinga.com/').text
soup = BeautifulSoup(r, 'html.parser')
print(soup.findAll('div', {'class': 'views-field-title'}))