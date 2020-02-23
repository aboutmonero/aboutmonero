import csv
import urllib.request
import json 
import time
import math

def write(data,dirc):
    with open(dirc, 'w+') as f:
                writer = csv.writer(f)
                writer.writerow([time.time()])
                for x in data:
                    writer.writerow([x]) 
                    
def get_marketcap(coin):
    if coin == 'total':
        urltemp = "https://www.coingecko.com/market_cap/total_charts_data?locale=en&vs_currency=usd" 
        req = urllib.request.Request(urltemp, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as url:
            data = [x[1] for x in list(json.loads(url.read().decode())['stats'])]
            data = data[::-1]
    elif coin == 'alt':
        urltemp = "https://web-api.coinmarketcap.com/v1.1/global-metrics/quotes/historical?format=chart_altcoin&interval=1d&time_end=1580623200&time_start=2013-04-28"
        req = urllib.request.Request(urltemp, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as url:
            data = [float(x[0]) for x in json.loads(url.read().decode())['data'].values()]
            data = data[::-1]
    else:
        with urllib.request.urlopen("https://api.coingecko.com/api/v3/coins/"+coin+"/market_chart?vs_currency=usd&days=3001") as url:
            data = list(json.loads(url.read().decode())['market_caps'])
            data = [float(x[1]) if x[1] else 0 for x in data ]
            data = data[::-1]
            data = data[1:]
            for i in range(1,len(data)):
                if data[i]==0:
                    data[i] = data[i-1]
    write(data,'static/market_caps/'+coin+'.csv')
    return [float(x) for x in data]
    
def get_hashrate():

def get_transactions_rate():

def get_price():

def get_data():
    get_marketcap('total')
    get_marketcap('alt')
    get_marketcap('bitcoin')
    get_marketcap('monero')
    
    return None
    
