import json
import time

import requests

headers = {'Authorization': 'mfa.6ukOessHxHSsR7D_Ot7EBP4pLix5E8VwwISw0Ryk2RgxCNfh76Y7FRcNvC6DYjdcVexnbXUVeQHdg_rG1N79'}

url_template = 'https://discord.com/api/v9/guilds/418433020719136768/messages/search?channel_id=489819668455096330&has=file&has=image&max_id=835651318579200000&offset='


def url_page(n: int):
    r = requests.get(url_template + str(n), headers=headers)

    data = json.loads(r.text)

    # print(data)

    images = []

    if 'messages' not in data.keys():
        return images

    for message in data['messages']:
        if len(message) == 0:
            continue
        else:
            attach = message[0]['attachments']

            for att in attach:
                images.append(att['url'])

    return images


all_images = []

# Hardcoded range
for i in range(int(274 / 25) + 1):
    time.sleep(0.5)  # Prevent Discord timeout
    # print('i=', i, sep='')
    print(f'Requesting offset={25 * i}...')
    all_images += url_page(25 * i)
    print(f'\tRequest done.')

print('Images:', *all_images, sep='\n')
print('length=', len(all_images))

with open('images.json', 'w') as file:
    file.write(json.dumps(all_images))

with open('images.txt', 'w') as file:
    print(*all_images, sep='\n', file=file)
