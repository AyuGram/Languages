import json
import os.path
import re

import requests

if not os.path.exists('./values'):
    os.chdir('../')

with open('./values/langs/en/Shared.json', encoding='utf-8') as f:
    strings = json.load(f)


def parse_latest_tag():
    r = requests.get('https://github.com/telegramdesktop/tdesktop/tags')
    regex = re.compile(r'<a href="/telegramdesktop/tdesktop/releases/tag/(.*?)"')

    try:
        return regex.search(r.text).group(1)
    except:
        return None


req = requests.get(
    f'https://raw.githubusercontent.com/telegramdesktop/tdesktop/{parse_latest_tag()}/Telegram/Resources/langs/lang.strings'
)

data = req.text
data += '''

// AyuGram keys generated

'''

for k, v in strings.items():
    if k.endswith('_Android'):
        continue

    if k.endswith('_PC'):
        k = k.replace('_PC', '')

    escaped = v.replace('"', '\\"').replace('\n', '\\n')
    data += f'"ayu_{k}" = "{escaped}";\n'

if not os.path.exists('./out'):
    os.mkdir('./out')

with open(os.path.realpath('./out/lang.strings'), 'w', encoding='utf-8') as f:
    f.write(data)

print('Done.')
