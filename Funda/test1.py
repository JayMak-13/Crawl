import json
import re
import requests
from lxml import html

base_url = 'https://www.funda.nl'
url = 'https://www.funda.nl/en/koop/haarlem/huis-42551247-zijlstraat-5/'
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    }

req = requests.get(url, headers=headers)
doc = html.fromstring(req.content)
# print(req.text)
item = {}
try:
    on_funda_date = ''
    if 'published-date="' in req.text:
        on_funda_date = req.text.split('published-date="')[1].split('"')[0]
        item['on_funda'] = on_funda_date
    else:
        item['on_funda'] = ''
except:
    item['on_funda'] = ''
print(item['on_funda'])
# json_data_id = doc.xpath('//h1[@class="fd-m-top-none fd-m-bottom-xs fd-m-bottom-s--bp-m"]/@data-global-id')[0].strip()
# print(json_data_id)
#
#
#
# headers3 = {
#     'authority': 'www.funda.nl',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
#     'sec-ch-ua-platform': '"Windows"',
#     'accept': '*/*',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://www.funda.nl/en/koop/haarlem/huis-42551247-zijlstraat-5/',
#     'accept-language': 'en-US,en;q=0.9,pt;q=0.8,gu;q=0.7',
# }
# json_url = f'https://www.funda.nl/objectinsights/getdata/{json_data_id}/'
# session = requests.Session()
# session.get('https://www.funda.nl/en/')
# json_req = session.get(json_url, headers=headers3)
# data = json.loads(json_req.text)
# print(data)
# views = data['NumberOfViews']
# saved = data['NumberOfSaves']
# print(views)
# print(saved)
#





# cadastral data
#     fees
#
#
# exterior space
#     balcony/garden
#
# activity
#     on funda date


T