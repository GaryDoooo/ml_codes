import requests

def get_ticker(company_name):
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"q": company_name, "quotes_count": 1, "region": "US"}
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    if data["quotes"]:
        return data["quotes"][0]["symbol"]
    return None

ticker = get_ticker("SPDR Gold Shares")
print(ticker)

