from lxml import etree as et

import json
import os.path

if not os.path.exists('./values'):
    os.chdir('../')

langs = [
    'en',
    'ru',
    'be',
    'pt',
    'es',
    'uk'
]

if not os.path.exists('./out'):
    os.mkdir('./out')

if not os.path.exists('./out/android'):
    os.mkdir('./out/android')

for lang in langs:
    with open(f'./values/langs/{lang}/Shared.json', encoding='utf-8') as f:
        strings = json.load(f)

    root = et.Element('resources')

    for k, v in strings.items():
        string = et.SubElement(root, 'string', {'name': k})
        string.text = v

    tree = et.ElementTree(root)

    suffix = f'-{lang}' if lang != 'en' else ''

    if not os.path.exists(f'./out/android/values{suffix}'):
        os.mkdir(f'./out/android/values{suffix}')

    tree.write(f'./out/android/values{suffix}/ayu.xml', pretty_print=True, xml_declaration=True, encoding="utf-8")

    print(f'Processed "{lang}"')

print('Done.')
