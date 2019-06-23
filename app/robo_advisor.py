import csv
import json
import os
import datetime
import statistics 
from dotenv import load_dotenv
import requests

load_dotenv() #> loads contents of the .env file into the script's environment

# source: https://github.com/prof-rossetti/nyu-info-2335-201905/edit/master/notes/python/datatypes/numbers.md
def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

#
# INFO INPUTS
#

api_key = os.environ.get("ALPHAVANTAGE_API_KEY") #"demo"
#print(api_key)

#INPUT VALID SYMBOL--must be less than 6 characters
symbol = input("Please input a stock ticker:") #"AMZN"

if (len(symbol) > 5):
    print("Symbol must be less than 6 characters")
    exit()
else:
#IF VALID SYMBOL, MAKING REQUEST FOR DATA
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

    response = requests.get(request_url)

    parsed_response = json.loads(response.text)

    last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

#breakpoint()

tsd = parsed_response["Time Series (Daily)"] #TODO: sort to ensure latest day is first

dates = list(tsd.keys())

latest_day = dates[0] # "2019-02-20"

latest_close = tsd[latest_day]["4. close"] #> 1,000.00


# maximum of all high prices, & min of all low prices

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(high_price)
    low_prices.append(low_price)

recent_high = max(high_prices)
recent_low = min(low_prices)

# average of all closing prices

closing_prices = []

for date in dates:
    closing_price = tsd[date]["4. close"]
    closing_prices.append(closing_price)

closing_prices_float = map(float, closing_prices)

average_closing_price = statistics.mean(closing_prices_float)

#
# INFO OUTPUTS
#

# csv-mgmt/write_teams.py

#csv_file_path = "prices.csv" # a relative filepath

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
        })
#making "Request AT" dynamic:
now = datetime.datetime.now()

#Print results
print("-------------------------")
print("SELECTED SYMBOL: " + symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + now.strftime("%Y-%m-%d %I:%M %p"))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"AVERAGE CLOSING PRICE IN LAST 100 DAYS: {to_usd(float(average_closing_price))}")
print("-------------------------")
#Determining recommendation
if average_closing_price:
    if average_closing_price < float(latest_close):
        print("RECOMMENDATION: SELL!")
        print("RECOMMENDATION REASON: The stock is overvalued. The most recent closing price is higher than its average closing price in the last 100 days.")
        print(f"WRITING DATA TO {csv_file_path}...")
        print("-------------------------")
        print("HAPPY INVESTING!")
        print("-------------------------")
    elif average_closing_price > float(latest_close):
        print("RECOMMENDATION: BUY!")
        print("RECOMMENDATION REASON: The stock is undervalued. The most recent closing price is lower than its average closing price in the last 100 days.")
        print("-------------------------")
        print(f"WRITING DATA TO {csv_file_path}...")
        print("-------------------------")
        print("HAPPY INVESTING!")
        print("-------------------------")
else:
        print("RECOMMENDATION: HOLD!")
        print("RECOMMENDATION REASON: The stock trades at fair value. The most recent closing price is equal to its average closing price in the last 100 days.")
        print("-------------------------")
        print(f"WRITING DATA TO {csv_file_path}...")
        print("-------------------------")
        print("HAPPY INVESTING!")
        print("-------------------------")