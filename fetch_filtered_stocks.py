import requests
import json

res_l = requests.get('https://openapi.twse.com.tw/v1/opendata/t187ap03_L').json()
res_o = requests.get('https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap03_O').json()

# keep only specific industry codes
keep_codes = {'17', '24', '25', '26', '27', '28', '29', '30', '31', '34', '36'}

stocks = {}
for item in res_l + res_o:
    ind = item.get('產業別', '')
    if ind in keep_codes:
        code = item.get('公司代號', '')
        name = item.get('公司簡稱', '')
        if code and name:
            stocks[code] = name

with open('filtered_stocks.json', 'w', encoding='utf-8') as f:
    json.dump(stocks, f, ensure_ascii=False)

print(f'Total kept stocks: {len(stocks)}')
