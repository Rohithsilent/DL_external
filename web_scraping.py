import requests

from bs4 import BeautifulSoup

url = 'https://example.com'

3
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

title = soup.title.string

print(f'Title of the webpage: {title}')

print('all paragraphs: ')

for p in soup.find_all('p'):
    print(p.get_text())

print('all links:')
for link in soup.find_all('a'):
    print('text',link.get_text(),'url',link.get('href'))