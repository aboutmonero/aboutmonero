import csv
import urllib.request
import json 
import time
import math
from monero.daemon import Daemon
from monero.backends.jsonrpc import JSONRPCDaemon
from datetime import datetime


def get_csv(direc):
    with open("static/data/"+direc+".csv", 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    rows = [[float(y) for y in x] for x in rows]
    return rows
        
def cache(data,direc):
    with open("static/data/"+direc+".csv", 'a+') as f:
        writer = csv.writer(f) 
        writer.writerows(data)
    return True
            
def get_json(url):   
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as urltemp:
        data = json.loads(urltemp.read().decode())
    return data
    
def cache_price():
    last = str(int(get_csv("price")[-1][0]))
    prices = []
    data = get_json("https://api.cryptowat.ch/markets/binance/xmrusdt/ohlc?periods=21600&after="+last)
    data = list(data['result']['21600'])[1:]
    for i in range(len(data)):
        prices.append([data[i][0],float(data[i][4])])
    if prices:
        return cache(prices,"price")
    else:
        return False
    
def test():
    daemon = Daemon(JSONRPCDaemon(port=18081))
    current = daemon.height()-1
    data = daemon.block(height=100000)
    print([data.timestamp,data.height,data.difficulty,float(data.reward),data.num_txes,data.fee,data.size,data.nonce,data.version[0],data.version[1]])
    

def update_latest(target, data):
    with open("static/data/latest.csv", 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for x in rows:
        if x[0] == target:
            x[1] = data
    with open("static/data/latest.csv", 'w') as f:
        writer = csv.writer(f) 
        writer.writerows(rows)
    return True

def get_latest():
    with open("static/data/latest.csv", 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    return ["{0:,.2f}".format(float(x[1])) for x in rows]





