import requests
import json

# source: https://github.com/prof-rossetti/nyu-info-2335-201905/edit/master/notes/python/datatypes/numbers.md
def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

#
# INFO INPUTS
#


request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

latest_close = parsed_response["Time Series (Daily)"]["2019-02-20"]["4. close"] #> 1,000.00

#breakpoint()

#
# INFO OUTPUTS
#


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")