import csv
import requests
import json 
import os
import datetime
import time
from dotenv import load_dotenv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


load_dotenv()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
#INFO INPUTS
#
import plotly

plotly.tools.set_credentials_file(username='kms923', api_key='28X77R0cm1ATCaYZGbbY')

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
#print(api_key)

request_url = f"https://www.alphavantage.co/query?function=SECTOR&apikey={api_key}"
response = requests.get(request_url)
parsed_response = json.loads(response.text)  # parse json into a dictionary
last_refreshed = parsed_response["Meta Data"]["Last Refreshed"]

##retrieving sector data for sector input by user

input_sector = input("Please input sector: ")

titlecase_input_sector = input_sector.title() #convert user input to title case https://www.geeksforgeeks.org/title-in-python/

one_day_performance = parsed_response["Rank B: 1 Day Performance"][titlecase_input_sector]
one_month_performance = parsed_response["Rank D: 1 Month Performance"][titlecase_input_sector]
three_month_performance = parsed_response["Rank E: 3 Month Performance"][titlecase_input_sector]
YTD_performance = parsed_response["Rank F: Year-to-Date (YTD) Performance"][titlecase_input_sector]

##Retrieving sector data

one_day = parsed_response["Rank B: 1 Day Performance"]
one_month = parsed_response["Rank D: 1 Month Performance"]
three_month = parsed_response["Rank E: 3 Month Performance"]
YTD = parsed_response["Rank F: Year-to-Date (YTD) Performance"]

a = list(one_day[titlecase_input_sector])
a.remove('%')
one_day_converted = float("".join(a))

b = list(one_month[titlecase_input_sector])
b.remove('%')
one_month_converted = float("".join(b))

c = list(three_month[titlecase_input_sector])
c.remove('%')
three_month_converted = float("".join(c))

d = list(YTD[titlecase_input_sector])
d.remove('%')
YTD_converted = float("".join(d))

#https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python

#Creating the sector performance chart

x = ['1Day Perf. (%)', '1M Perf. (%)', '3M Perf. (%)', 'YTD Perf. (%)']
y = [one_day_converted, one_month_converted, three_month_converted, YTD_converted]

data = [go.Bar(
            x=x,
            y=y,
            text=y,
            textposition = 'auto',
            marker=dict(
                color='rgb(106,90,205)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )]

py.iplot(data, filename='bar-direct-labels')

print('Sector Performance chart has been successfully created.')