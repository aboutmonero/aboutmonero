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
    
def cache_blocks():
    daemon = Daemon(JSONRPCDaemon(port=18081))
    last = int(get_csv("blocks")[-1][0])
    new = []
    current = 2045024
    while current > last:
        last +=1
        data = daemon.block(height=last)
        new.append([datetime.fromisoformat(str(data.timestamp)).timestamp(),data.height,data.difficulty,float(data.reward),len(data.transactions)])
    cache(new,"blocks")
    return True


def cache_blocks_tmp():
    daemon = Daemon(JSONRPCDaemon(port=18081))
    last = 0
    new = []
    current = 500000
    while current > last:
        last +=1
        data = daemon.block(height=last)
        new.append([datetime.fromisoformat(str(data.timestamp)).timestamp(),data.height,data.difficulty,float(data.reward),len(data.transactions)])
        if last % 10000==0:
            cache(new,"blocks_early")
            new = [] 
            print(last)
    return True

cache_blocks_tmp()









