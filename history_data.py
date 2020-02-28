import csv
import urllib.request
import json 
import time
import math
from monero.daemon import Daemon
from monero.backends.jsonrpc import JSONRPCDaemon

def get_last(direc):
    with open("static/data/"+direc+".csv", 'r') as f:
        reader = csv.reader(f)
        rows=list(reader)
    if rows:
        return int(rows[-1][0])
    else:
        return 0
        
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
    
def get_price():
    data = get_json("https://api.cryptowat.ch/markets/binance/xmrusdt/ohlc?periods=14400")
    prices = [[float(x[0]),float(x[4])] for x in list(data['result']['14400'])]
    cache(prices,"price")
        
def get_current_block():
    data = get_json("https://www.xmrchain.net/api/networkinfo")
    return int(data['data']['height'])
        
def get_blocks():
    daemon = Daemon(JSONRPCDaemon(port=18081))
    last = get_last("blocks")
    new = []
    current = daemon.height()
    while current > last:
        data = daemon.block(height=last)
        new = new + [[data.height,data.timestamp,data.difficulty,data.reward,len(data.transactions)]]
        last +=1
    cache(new,"blocks")
    

def get_block_reward():
    with open("static/data/blocks.csv", 'r') as f:
        reader = csv.reader(f)
        rows=list(reader)
    data = [[x[1],x[3]] for x in rows]
    cache(data,"reward")
    
def get_supply():
    with open("static/data/reward.csv", 'r') as f:
        reader = csv.reader(f)
        rows=list(reader)
    supply = [[0.0,0.0]]
    for x in rows:
        supply.append([x[0],float(x[1]) + supply[-1][1]])
    cache(supply,"supply")

def get_hashrate():
    with open("static/data/blocks.csv", 'r') as f:
        reader = csv.reader(f)
        rows=list(reader)
    data = [[x[1],float(x[2])/120] for x in rows]
    cache(data,"hashrate")
    
def get_transactions():
    with open("static/data/blocks.csv", 'r') as f:
        reader = csv.reader(f)
        rows=list(reader)
    data = [[x[1],float(x[4])] for x in rows]
    cache(data,"transactions")
    
def month(direc):
    with open("static/data/"+direc+".csv", 'r') as f:
        reader = csv.reader(f)
        rows=list(reader)
    rows = rows[::-1]
    data = rows[:720]
        
        
        
        
def year():

def all():











