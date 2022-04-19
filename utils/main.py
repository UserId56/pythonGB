import datetime
import requests
from neodict2xml import dict2xml
from decimal import Decimal
def get_date(dateStr):
    array_date = dateStr.split('.')
    # print(array_date)
    result = datetime.date(int(array_date[2]), int(array_date[1]), int(array_date[0]))
    return result


def currency_rates(current_valute):
    r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    date_requst = dict2xml.from_xml(r.text)['ValCurs'][0]['Date']
    valute_list = dict2xml.from_xml(r.text)['ValCurs'][1]['Valute']
    result = {}
    result['date'] = get_date(date_requst)
    for i in range(0, len(valute_list)):
        if valute_list[i][1]['CharCode'] == current_valute.upper():
            result['value'] = Decimal(valute_list[i][1]['Value'].replace(',', '.'))
    return result

if __name__ == "__main__":
    print(currency_rates('ten'))
    print(currency_rates('usd'))
    print(currency_rates('Eur'))
