import json
import re

with open('filtered_stocks.json', 'r', encoding='utf-8') as f:
    stocks = json.load(f)

# format the dictionary and list
stock_names_str = 'STOCK_NAMES = ' + repr(stocks)

stock_list_str = 'TW_STOCKS = list(set([\n    '
codes = list(stocks.keys())
for i in range(0, len(codes), 10):
    stock_list_str += ', '.join(f'\"{c}\"' for c in codes[i:i+10]) + ',\n    '
stock_list_str = stock_list_str.rstrip(' \n,') + '\n]))'

with open('tw_stock_screener.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace TW_STOCKS
content = re.sub(r'TW_STOCKS = list\(set\(\[.*?\]\)\)', stock_list_str, content, flags=re.DOTALL)

# Replace STOCK_NAMES
content = re.sub(r'STOCK_NAMES = \{.*?\}', stock_names_str, content, flags=re.DOTALL)

with open('tw_stock_screener.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated tw_stock_screener.py with new stock list.')
