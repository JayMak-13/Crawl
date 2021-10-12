import requests
session = requests.Session()
session.get('https://www.funda.nl/en/')
headers = {
    'authority': 'www.funda.nl',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.funda.nl/en/koop/haarlem/huis-42551247-zijlstraat-5/',
    'accept-language': 'en-US,en;q=0.9,pt;q=0.8,gu;q=0.7',
}

response = session.get('https://www.funda.nl/objectinsights/getdata/6106884/', headers=headers)

print(response.text)


req = requests.get()