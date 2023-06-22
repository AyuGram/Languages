from lxml import etree as et

import json
import os.path

if not os.path.exists('./values'):
    os.chdir('../')

with open('./values/Shared.json') as f:
    strings = json.load(f)

root = et.Element('resources')

for k, v in strings.items():
    string = et.SubElement(root, 'string', {'name': k.replace('ayu_', '')})
    string.text = v

tree = et.ElementTree(root)

if not os.path.exists('./out'):
    os.mkdir('./out')

tree.write('./out/ayu.xml', pretty_print=True, xml_declaration=True, encoding="utf-8")

print('Done.')
