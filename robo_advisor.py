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

#breakpoint()

tsd = parsed_response["Time Series (Daily)"] #TODO: sort to ensure latest day is first

dates = list(tsd.keys())

latest_day = dates[0] # "2019-02-20"

latest_close = tsd[latest_day]["4. close"] #> 1,000.00


# maximum of all high prices
# high_prices = [10, 20, 30, 5]
# recent_high = max(high_prices)

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(high_price)
    low_price = tsd[date]["3. low"]
    low_prices.append(low_price)

recent_high = max(high_prices)
recent_low = min(low_prices)

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
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")