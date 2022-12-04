import requests
from bs4 import BeautifulSoup


def get_addresses():
    url = 'https://www.energy.mk.ua/grafik-obmezhennya-spozhyvachiv/?type=gao&fil=15'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    r = requests.get(url, headers)
    bs = BeautifulSoup(r.content, 'html5lib')
    table_rows = bs.find('tbody', attrs={'id': 'output'}).find_all('tr')
    json_array = []
    for table_row in table_rows:
        columns = table_row.find_all('td')
        addresses = columns[1]
        dict_json = {
            'number': columns[0].text, 'time_start': columns[4].text, 'time_end': columns[5].text}
        all_addr_dict = {}
        street = None
        for elem in addresses:
            if (elem.name == 'b' and elem.text):
                street = elem.text
            elif addresses and 'Будинки:' in elem.text:
                all_addr_dict[street] = [line.strip()
                                         for line in elem.text[9:].strip().split(',')]
                #street = None
        dict_json['addresses'] = all_addr_dict
        json_array.append(dict_json)
    return json_array
