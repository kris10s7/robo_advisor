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

##input sector
input_sector = input("Please input sector: ")

one_day_performance = parsed_response["Rank B: 1 Day Performance"][input_sector]
one_month_performance = parsed_response["Rank D: 1 Month Performance"][input_sector]
three_month_performance = parsed_response["Rank E: 3 Month Performance"][input_sector]
YTD_performance = parsed_response["Rank F: Year-to-Date (YTD) Performance"][input_sector]

trace = go.Table(
    header=dict(values=[' ', '1Day Performance', '1M Performance', '3 Month Performance', 'YTD performance'],
                line = dict(color='#ffffff'),
                fill = dict(color='#ddd3ee'),
                align = ['left'] * 5),
    cells=dict(values=[[input_sector], [one_day_performance],[one_month_performance], [three_month_performance], [YTD_performance]],
               line = dict(color='#ddd3ee'),
               fill = dict(color='#ffffff'),
               align = ['left'] * 5))

layout = dict(width=500, height=300)
data = [trace]
fig = dict(data=data, layout=layout)
py.iplot(fig, filename = 'styled_table')

