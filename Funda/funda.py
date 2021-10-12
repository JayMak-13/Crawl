import json
import re

import pandas
import requests
from lxml import html

base_url = 'https://www.funda.nl'
url = 'https://www.funda.nl/en/koop/heel-nederland/'

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    }

req = requests.get(url, headers=headers)
doc = html.fromstring(req.content)


all_data = []

last_page = ''.join(doc.xpath('//div[@class="pagination-pages"]//p[contains(text(),"from")]/following::a[1]/text()')).strip().replace(',', '')
lp = int(last_page)
for pages in range(1, 5):
    page_url = f'https://www.funda.nl/en/koop/heel-nederland/p{pages}/'
    print(page_url)

    req1 = requests.get(page_url, headers=headers)
    doc1 = html.fromstring(req1.content)
    homes = doc1.xpath('//div[@class="search-result-content"]')
    for home in homes:
        item = {}
        home_url = base_url + home.xpath('.//a[1][contains(@data-object-url-tracking,"resultlist")]/@href')[0].strip()
        print(home_url)
        req2 = requests.get(home_url, headers=headers)
        doc2 = html.fromstring(req2.content)
        try:
            item['title'] = doc2.xpath('//span[@class="object-header__title"]//text()')[0].strip()
        except:
            item['title'] = ''
        print(item['title'])

        try:
            item['price'] = doc2.xpath('//strong[@class="object-header__price"]//text()')[0].strip()
        except:
            item['price'] = ''
        print(item['price'])

        try:
            item['description'] = "".join(doc2.xpath('//div[@class="object-description-body"]//text()')).strip()
        except:
            item['description'] = ''
        print(item['description'])

        try:
            item['address'] = "".join(doc2.xpath('//span[@class="object-header__subtitle fd-color-dark-3"]/text()')).strip()
        except:
            item['address'] = ''
        print(item['address'])

        try:
            size = doc2.xpath('//li/span[contains(text(),"living area")]/preceding-sibling::span[1]//text()')[0].strip()
        except:
            size = ''
        try:
            bathrooms = doc2.xpath('//li/span[contains(text(),"plot size")]/preceding-sibling::span[1]//text()')[0].strip()
        except:
            bathrooms = ''
        try:
            bedrooms = doc2.xpath('//li/span[contains(text(),"bedrooms")]/preceding-sibling::span[1]//text()')[0].strip()
        except:
            bedrooms = ''

        item['size_bathrooms_bedrooms'] = size + " + " + bathrooms + " + " +  bedrooms
        print(item['size_bathrooms_bedrooms'])


        # Features | Transfer of Ownership
        try:
            item['asking_price'] = doc2.xpath('//dt[contains(text(),"Asking price")]/following::span[1][@class="fd-m-right-xs"]//text()')[0].strip()
        except:
            item['asking_price'] = ''
        print(item['asking_price'])

        try:
            item['asking_price_per_m'] = doc2.xpath('//dt[contains(text(),"Asking price per m²")]/following::dd[1]/text()')[0].strip()
        except:
            item['asking_price_per_m'] = ''
        print(item['asking_price_per_m'])

        try:
            item['listed_since'] = doc2.xpath('//dt[contains(text(),"Listed since")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['listed_since'] = ''
        print(item['listed_since'])

        try:
            item['status'] = doc2.xpath('//dt[contains(text(),"Status")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['status'] = ''
        print(item['status'])

        try:
            item['acceptance'] = doc2.xpath('//dt[contains(text(),"Acceptance")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['acceptance'] = ''
        print(item['acceptance'])


        # Features | Construction
        try:
            item['kind_of_house'] = doc2.xpath('//dt[contains(text(),"Kind of house")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['kind_of_house'] = ''
        print(item['kind_of_house'])

        try:
            item['building_type'] = doc2.xpath('//dt[contains(text(),"Building type")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['building_type'] = ''
        print(item['building_type'])

        try:
            item['year_of_construction'] = doc2.xpath('//dt[contains(text(),"Year of construction")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['year_of_construction'] = ''
        print(item['year_of_construction'])

        try:
            item['type_of_proof'] = doc2.xpath('//dt[contains(text(),"Type of roof")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['type_of_proof'] = ''
        print(item['type_of_proof'])


        # Features | Surface areas and volume
        try:
            item['living_area'] = doc2.xpath('//dt[contains(text(),"Living area")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['living_area'] = ''
        print(item['living_area'])

        try:
            item['exterior_space_attached_to_building'] = doc2.xpath('//dt[contains(text(),"Exterior space attached to the building")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['exterior_space_attached_to_building'] = ''
        print(item['exterior_space_attached_to_building'])

        try:
            item['external_storage_space'] = doc2.xpath('//dt[contains(text(),"External storage space")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['external_storage_space'] = ''
        print(item['external_storage_space'])

        try:
            item['plot_size'] = doc2.xpath('//dt[contains(text(),"Plot size")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['plot_size'] = ''
        print(item['plot_size'])

        try:
            item['volume_in_cubic_meters'] = doc2.xpath('//dt[contains(text(),"Volume in cubic meters")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['volume_in_cubic_meters'] = ''
        print(item['volume_in_cubic_meters'])


        # Features | Layout
        try:
            item['number_of_rooms'] = doc2.xpath('//h3[contains(text(),"Layout")]/following::dt[contains(text(),"Number of rooms")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['number_of_rooms'] = ''
        print(item['number_of_rooms'])

        try:
            item['number_of_bathrooms'] = doc2.xpath('//h3[contains(text(),"Layout")]/following::dt[contains(text(),"Number of bath rooms")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['number_of_bathrooms'] = ''
        print(item['number_of_bathrooms'])

        try:
            item['bathroom_facilities'] = doc2.xpath('//h3[contains(text(),"Layout")]/following::dt[contains(text(),"Bathroom facilities")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['bathroom_facilities'] = ''
        print(item['bathroom_facilities'])

        try:
            item['number_of_stories'] = doc2.xpath('//h3[contains(text(),"Layout")]/following::dt[contains(text(),"Number of stories")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['number_of_stories'] = ''
        print(item['number_of_stories'])

        try:
            item['layout_facilities'] = doc2.xpath('//h3[contains(text(),"Layout")]/following::dt[contains(text(),"Facilities")][1]/following::dd[1]/span//text()')[0].strip()
        except:
            item['layout_facilities'] = ''
        print(item['layout_facilities'])


        # Features | Energy
        try:
            item['enery_label'] = doc2.xpath('//h3[contains(text(),"Energy")]/following::dt[contains(text(),"Energy label")]/following::dd[1]/span/text()')[0].strip()
        except:
            item['enery_label'] = ''
        print(item['enery_label'])

        try:
            item['insulation'] = doc2.xpath('//h3[contains(text(),"Energy")]/following::dt[contains(text(),"Insulation")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['insulation'] = ''
        print(item['insulation'])

        try:
            item['heating'] = doc2.xpath('//h3[contains(text(),"Energy")]/following::dt[contains(text(),"Heating")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['heating'] = ''
        print(item['heating'])

        try:
            item['hot_water'] = doc2.xpath('//h3[contains(text(),"Energy")]/following::dt[contains(text(),"Hot water")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['hot_water'] = ''
        print(item['hot_water'])


        # Features | Cadastral data
        try:
            item['cadastral_map'] = home_url + doc2.xpath('//h3[contains(text(),"Cadastral data")]/following::a[contains(text(),"Cadastral map")]/@href')[0].strip()
        except:
            item['cadastral_map'] = ''
        print(item['cadastral_map'])

        try:
            item['area'] = doc2.xpath('//h3[contains(text(),"Cadastral data")]/following::dt[contains(text(),"Area")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['area'] = ''
        print(item['area'])

        try:
            item['ownership_situation'] = doc2.xpath('//h3[contains(text(),"Cadastral data")]/following::dt[contains(text(),"Ownership situation")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['ownership_situation'] = ''
        print(item['ownership_situation'])

        try:
            item['fees'] = doc2.xpath('//h3[contains(text(),"Cadastral data")]/following::dt[contains(text(),"Fees")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['fees'] = ''
        print(item['fees'])


        # Features | Exterior space
        try:
            item['garden'] = doc2.xpath('//h3[contains(text(),"Exterior space")]/following::dt[contains(text(),"Garden")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['garden'] = ''
        print(item['garden'])

        try:
            item['back_garden'] = doc2.xpath('//h3[contains(text(),"Exterior space")]/following::dt[contains(text(),"Back garden")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['back_garden'] = ''
        print(item['back_garden'])

        try:
            item['garden_location'] = doc2.xpath('//h3[contains(text(),"Exterior space")]/following::dt[contains(text(),"Garden location")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['garden_location'] = ''
        print(item['garden_location'])

        try:
            item['balcony/roof_garden'] = doc2.xpath('//h3[contains(text(),"Exterior space")]/following::dt[contains(text(),"Balcony/roof garden")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['balcony/roof_garden'] = ''
        print(item['balcony/roof_garden'])


        # Features | Storage space
        try:
            item['shed/storage'] = doc2.xpath('//h3[contains(text(),"Storage space")]/following::dt[contains(text(),"Shed / storage")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['shed/storage'] = ''
        print(item['shed/storage'])

        try:
            item['storage_facilities'] = doc2.xpath('//h3[contains(text(),"Storage space")]/following::dt[contains(text(),"Facilities")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['storage_facilities'] = ''
        print(item['storage_facilities'])


        # Features | Parking
        try:
            item['type_of_parking_facilities'] = doc2.xpath('//h3[contains(text(),"Parking")]/following::dt[contains(text(),"Type of parking facilities")][1]/following::dd[1]/span/text()')[0].strip()
        except:
            item['type_of_parking_facilities'] = ''
        print(item['type_of_parking_facilities'])


        # Features | Activity
        try:
            json_data_id = doc.xpath('//h1[@class="fd-m-top-none fd-m-bottom-xs fd-m-bottom-s--bp-m"]/@data-global-id')[0].strip()

            headers3 = {
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
            json_url = f'https://www.funda.nl/objectinsights/getdata/{json_data_id}/'
            session = requests.Session()
            session.get('https://www.funda.nl/en/')
            json_req = session.get(json_url, headers=headers3)
            data = json.loads(json_req.text)
            item['viewed'] = data['NumberOfViews']
            item['saved'] = data['NumberOfSaves']
        except:
            item['viewed'] = ''
            item['saved'] = ''
        print(item['viewed'])
        print(item['saved'])

        try:
            on_funda_date = ''
            if 'published-date="' in req.text:
                on_funda_date = req2.text.split('published-date="')[1].split('"')[0]
                item['on_funda'] = on_funda_date
            else:
                item['on_funda'] = ''
        except:
            item['on_funda'] = ''
        print(item['on_funda'])


        # # Neighbourhood
        try:
            neighbour_url = re.findall('/informatie(.*)', doc2.xpath('//h2[contains(text(),"Neighborhood")]/following::a[1]/@href')[0].strip())[0].strip()
            neighbour_json_url = base_url + "/informatie/preview" + neighbour_url
            headers2 = {
                    'accept': "application/json, text/plain, */*",
                    'accept-encoding': "gzip, deflate, br",
                    'accept-language': "en-US,en;q=0.9,pt;q=0.8,gu;q=0.7",
                    'cache-control': "no-cache",
                    'cookie': ".ASPXANONYMOUS=MhatTBMrEjDgF3kDLv_JXcjJ3DtjoaRxPE1L7czUBziJF__wAihterIpv1CD_CQdlUzuXeuEdv_whefuKJ3Jw6Hi_txBRYl8JZhfJxiSnwF8IY3MtMq2-f8Ud-GMYTLZywu1kQZFRlMiV6PqzNvoMkoQvoQ1; OptanonAlertBoxClosed=2021-10-01T09:36:38.563Z; eupubconsent-v2=CPNZGJTPNZGJTAcABBENBmCgAPLAAAAAAChQIJtF7S5dRGPCWG58ZtskOQQPoNSMJgQjABaJImgJwAKAMIQCkmASPATgBAACCAYAKAIBAANkGAAAAQAAQAAAAAGEQAAABAIIICIAgBIBCAAIAAQAAIAQQAAAgEACAEAAkwAAAIIAQEAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH9gAAAPCQHQAEAALAAqABkADgAHgAQAAyABoADwAIgATAAngBVACwAG8ARwAlwBhwDUANUAfoBHACUgGKAReAmIBcgC8wGSBABAADwAPgAtAD-AM0AgYCPQErBgAoACwA3gEtAOoAvoNAFAC4ANSAtAC0gIvAXIIABgALADeAS0RADAGoAi8BcgoBoAA0AB8AGAAZABEACwAGMAPgA_ACYAFyALwAvwBhAGIANoAeIA_gEEAIUARwAkwBQACoAFaALIAZQAzYBqAGrAOIA5AB5gEcAJNAS0BLoCeAJ6AUgAr8BaAFpALuAYEAxUBnAGdANAAacA4UB-gH7AQIAj0BIICYgE7gKIAU2AswBcgC84F8gX0MAVgAPgAwADIAIgAWAAxAB-AEwAL0AYQBiADbAH8AggBHACTAFAAKgAVoAsgBjgDKgGoAasA4gDkAHmARwAlsBPAE9AKQAV8Au4BioDOAM6AaCA0wDTgHCAP2AgQBHoCQQExAJ3AUQApsBZgC8xwBYABAADwALgAfABaADkAH4AaAA_gDNAIGAQgAiIBLYDAAMCAZkA14CPQErAJiAVMAvodApAAWABUADIAHAAQQAxADIAGgAPAAfABEACYAE8AKoAWAAuABfADEAG8AR0AlwCYAFiAMMAZQA0QBqADfAH6ARYAjgBKYC0ALSAXUAxQB1AEXgJBAVYAtkBcgC8wGSEAH4AAQAEAALAAaAA8ADIAIgAWAAxAB_AEwATQAqgBcgC8AL8AYQBiADQAG0AN8AfwCBAEWAI4ASYAoABUACtgFiAWQAygBmwDUANUAb4A4gByADzAI4ASkAnABPACkAFZAK_AWgBaQC7gGAAMUAZmAzgDOgGggNMA04BwgDqQH6AfsBAACBAEegJBATEAncBRACmwFmALZAXJAvkC-iUBcABAACwAMgAcABiADwAIgATAAqgBcAC-AGIANoAjgBlADVAI5AWgBaQC6gGKAOoAi8BeZIAUABcAHIAbwBfADUAJaAa8BKwC9gF9FIDYACwAKgAZAA4ACCAGIAZAA0AB4AEQAJgATwAqgBYAC-AGIAWIAygBogDVAH6ARYAjgBKQEXgLkAXmAyQoATAAuAB8AFoAOQAfgBtADeAI4AagA1wCWgF1AMAAYoA14CPQExAKmAX0AA.flgAAAAAAAAA; objectnotfound=objectnotfound=false; optimizelyEndUserId=oeu1633080999955r0.09357772646460538; ajs_anonymous_id=%227aad5e21-96ed-48cb-b919-888eb5adab13%22; fd-user-checked=true; lzo=koop=%2fkoop%2fheel-nederland%2f; SNLBCORS=8b8d8c7a06085568b54a0868f92db453; SNLB=8b8d8c7a06085568b54a0868f92db453; sr=0%7cfalse; html-classes=js; _gid=GA1.2.1598379494.1633323851; sessionstarted=true; __RequestVerificationToken=qBQfLTyqcdp_wwK2WoHOT7VGuB7__FZesXelT1Y0oDFr79sc8VUZ-y-_e4pV--6Re0FLDpHk9oAY5t70EHBzOL_yYm81; bm_mi=D6C63020E876C0B96EA54AC5DB6448F9~1rpOPB3R1VaCYzWMEgcTUgbTPtuSp1WCwZlTkbOv2M6Wnn1+gEcoSMlue3iRDEoO9jA0ledebyI2AZ6rhVrLkdpTRCVQZChMPkGARbUYl51z9rByALJGLhEjHV30WMYQ/6KHDm7abmLTvij0HmNNwqMdsmk65cI3VqIz7R+bu8OLDS6A2Mk4qizZlUrxbFQhiwVZ6k277Z3e7CSLXbP8zJMQCH/VsyjlyEgmu11m/uj5LI6OKeIDQ00TJOv+299sVDyin0euKLL9+WlJUfT5V9c2/Xa0lLS85RdhqN6yZzKtXFXn/7diNYOJTASqR5kXfIjaYx5Lm5rJWemyXOV+KQ==; ak_bmsc=7D2E29DED39B011222C4FB84B450B194~000000000000000000000000000000~YAAQDv7UF4XqSq56AQAAEu61Sg2q/RJahLzrEePAOMAbquC6mhTeipfjfjUgLnD9QlHD5tPpcl9FT+x9PUJ9nMP4C9DPW/bf8CbAA0sxLqU8ts/dvqbHp0LuNyILLZbvxMlADlxNBouSqNwrjyFOic+1DjoXaXqGCwvO+l3kSROk/1z0vkkj4PakEEfkceO4y76AkGGyUxAsXu0ARlgoJKuPk0FSN9q++oj0R/HE/2wXBww70XFtqK1+GSR8CZKUqXJLqwu1o2JpgeITVYoDE+VmEXW9e2MQgUj9kVwsFe2E9XvVPqGps0QKvdAlqR3856p2AezwJdQ+OAwyAkAtgNS3TJmxc4/meG54i0AusQ3vt7AxSAgGBet3mL3fwLaCB9dnZndcDhCqBVIfC7jdCqa+pM2AnNzZ2g98Bc3chD1O5gLc9CtOSmH2JEDzTx/fFYLeA/pI/8ykTenup7+XUysHItYHK2XkA3RncTK9k1uTz/xdeslDIeHWI5CHntxQYKzvpHjfrde28zMSUkobySlf1BRbu+28qblRbhQS+5EUjyObCx7S8UYMXiH3D8FaQw==; _gat_UA-3168440-16=1; _dd_s=logs=1&id=e42de008-535c-4444-8f0f-54a025430b3a&created=1633338275583&expire=1633342639212; OptanonConsent=isIABGlobal=false&datestamp=Mon+Oct+04+2021+15%3A32%3A20+GMT%2B0530+(India+Standard+Time)&version=6.22.0&consentId=3dd2a37b-4fb8-4d22-9cdd-3150aa764b90&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CF01%3A1%2CF02%3A1%2CF03%3A1%2CBG30%3A1%2CF04%3A1%2CC0004%3A1%2CF05%3A1%2CBG29%3A1%2CSTACK39%3A1&hosts=H41%3A1%2CH42%3A1%2CH44%3A1%2CH45%3A1%2CH5%3A1%2CH18%3A1%2CH21%3A1%2CH1%3A1%2CH37%3A1%2CH6%3A1%2CH38%3A1%2CH7%3A1%2CH35%3A1%2CH10%3A1%2CH34%3A1%2CH39%3A1%2CH43%3A1%2CH9%3A1%2CH11%3A1%2CH2%3A1%2CH12%3A1%2CH15%3A1%2CH40%3A1%2CH16%3A1%2CH17%3A1&geolocation=IN%3BGJ&AwaitingReconsent=false; _ga_WLRNSHBY8J=GS1.1.1633336981.5.1.1633341739.0; _ga=GA1.1.2122294305.1633080992; bm_sv=6A35B9C6B4CE083E3AC9B71724387E96~YK/Z9BZZHOhCllYHvSxkvq12JtCFCbx/c1of3h3fUgv10DmzKYUwYdi+pmI7shX53EdEnLbCPMmz0VU4a6iCFFTsZseifjdgZuBJugEJwelJ1Bm2YGXwwSlnEEwQcvBCCdS5/MWC4/HV71n4E3MplqN/22AW+wrxJWl7D3JClpw=",
                    'pragma': "no-cache",
                    'referer': "https://www.funda.nl/en/koop/bladel/huis-42552974-felix-timmermanslaan-12/",
                    'sec-ch-ua': "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"",
                    'sec-ch-ua-mobile': "?0",
                    'sec-ch-ua-platform': "\"Windows\"",
                    'sec-fetch-dest': "empty",
                    'sec-fetch-mode': "cors",
                    'sec-fetch-site': "same-origin",
                    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
                    'postman-token': "79f25d03-5ef4-1b56-f32c-baec73723784"
                }

            js_req = requests.get(neighbour_json_url,headers=headers2)
            json_data1 = json.loads(js_req.text)
            for details in json_data1:
                try:
                    if details['key'] == 'Inhabitants':
                        item['resident'] = int(details['value'])
                    elif details['key'] == 'FamiliesWithChildren':
                        item['family_with_children'] = int(details['value'])
                    elif details['key'] == 'AvgAskingPricePerM²':
                        item['avg_asking_price/m²'] = int(details['value'])
                except:
                    item['resident'] = ''
                    item['family_with_children'] = ''
                    item['avg_asking_price/m²'] = ''
        except:
            item['resident'] = ''
            item['family_with_children'] = ''
            item['avg_asking_price/m²'] = ''

        print(item['resident'])
        print(item['family_with_children'])
        print(item['avg_asking_price/m²'])

        try:
            item['in_the_neighbourhood'] = ', '.join(doc2.xpath('//h2[contains(text(),"Neighborhood")]/following::ul[@class="object-buurt__list"]//span[@class="object-buurt__term"]//text()')).strip()
        except:
            item['in_the_neighbourhood'] = ''
        print(item['in_the_neighbourhood'])

        all_data.append(item)





result = pandas.DataFrame(all_data)
result.to_csv('funda.csv')
