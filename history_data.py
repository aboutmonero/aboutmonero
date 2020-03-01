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
        rows=list(reader)
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
    
def get_price():
    data = get_json("https://api.cryptowat.ch/markets/binance/xmrusdt/ohlc?periods=14400")
    prices = [[float(x[0]),float(x[4])] for x in list(data['result']['14400'])]
    cache(prices,"price")
        
def get_current_block():
    data = get_json("https://www.xmrchain.net/api/networkinfo")
    return int(data['data']['height'])
        
def get_blocks():
    
    def get_block_reward():
        blocks = get_csv("blocks")
        data = [[x[0],x[3]] for x in blocks]
        last = len(get_csv("reward"))
        data = data[last-1369999:]
        cache(data,"reward")
        
    def get_supply():
        reward = get_csv("reward")
        supply = [[0.0,0.0]]
        last = len(get_csv("supply"))
        reward = reward[last:]
        for x in reward:
            supply.append([x[0],float(x[1]) + supply[-1][1]])
        cache(data,"reward")

    def get_hashrate():
        blocks = get_csv("blocks")
        data = [[x[1],float(x[2])/120] for x in blocks]
        cache(data,"hashrate")
        
    def get_transactions():
        blocks = get_csv("blocks")
        data = [[x[1],float(x[4])] for x in blocks]
        cache(data,"transactions")
        
    daemon = Daemon(JSONRPCDaemon(port=18081))
    last = 2000000
    new = []
    current = 2030000
    while current > last:
        data = daemon.block(height=last)
        new.append([datetime.fromisoformat(str(data.timestamp)).timestamp(),data.height,data.difficulty,float(data.reward),len(data.transactions)])
        last +=1
        if(last%1000==0):
            print(last)
    cache(new,"blocks")
    return True

def convert_to_month(direc):
    data = get_csv(direc)
    start = time.time() - 30*24*60*60

    # find earliest block
    i = len(data)
    while float(data[i][0]) > start:
        i -= 1
        
    # cut off earlier blocks
    data = data[i:]
    
    # want 360 data points
    l = int(len(data)/360)
    data = [data[i] for i in range(len(data)) if i % l == 0]
    
    cache(month_data,direc+"_1m")
    return month_data    
        
        
'''      
get_blocks()
print(convert_to_month("transactions"))
'''
#1000000 block is when time changes
get_blocks()



