import json
import requests

def get_response(stock_symbol)
    url = f"https://my-api.com/stocks?symbol={stock_symbol}"
    response = requests.get(url) # issues an HTTP request
    return json.loads(response.text)
