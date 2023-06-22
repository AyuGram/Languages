import json

import bs4
import requests

with open('ayu.xml') as f:
    text = f.read()

tree = bs4.BeautifulSoup(text, 'xml')

strings = {}
for string in tree.find_all('string'):
    t = string.attrs['name']
    strings[f'ayu_{t}'] = string.text

with open('./values/Shared.json', 'w') as f:
    json.dump(strings, f, indent=2)

print('Done.')
