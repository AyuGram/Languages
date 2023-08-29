import re

from lxml import etree as et

import json
import os.path

if not os.path.exists('./values'):
    os.chdir('../')

langs = [
    'ar',
    'be',
    'de',
    'en',
    'es',
    'fa',
    'pt',
    'ru',
    'tr',
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
        if k + '_Android' in strings:
            continue

        if k.endswith('_Desktop'):
            continue

        if k.endswith('_Android'):
            k = k.replace('_Android', '')

        string = et.SubElement(root, 'string', {'name': k})
        string.text = v.replace('\'', '\\\'')

    tree = et.ElementTree(root)

    suffix = f'-{lang}' if lang != 'en' else ''

    if not os.path.exists(f'./out/android/values{suffix}'):
        os.mkdir(f'./out/android/values{suffix}')

    tree.write(f'./out/android/values{suffix}/ayu.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')

    # fix CDATA
    with open(f'./out/android/values{suffix}/ayu.xml', encoding='utf-8') as f:
        data = f.read()
        data = re.sub(r'&lt;!\[CDATA\[&lt;a href="(.+?)"&gt;(.+?)&lt;/a&gt;\]\]&gt;', r'<![CDATA[<a href="\1">\2</a>]]>', data)

    with open(f'./out/android/values{suffix}/ayu.xml', 'w', encoding='utf-8') as f:
        f.write(data)

    print(f'Processed "{lang}"')

print('Done.')
