import json
import os.path

import requests

if not os.path.exists('./values'):
    os.chdir('../')

with open('./values/Shared.json') as f:
    strings = json.load(f)

req = requests.get(
    'https://raw.githubusercontent.com/telegramdesktop/tdesktop/dev/Telegram/Resources/langs/lang.strings'
)

data = req.text
data += '''

// AyuGram keys generated

'''

for k, v in strings.items():
    escaped = v.replace('"', '\\"')
    data += f'"ayu_{k}" = "{escaped}";\n'

if not os.path.exists('./out'):
    os.mkdir('./out')

with open(os.path.realpath('./out/lang.strings'), 'w', encoding='utf-8') as f:
    f.write(data)

print('Done.')
