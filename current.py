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
    rows = rows[-100:]
    rows = [[float(y) for y in x] for x in rows]
    return rows
            
def get_json(url):   
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as urltemp:
        data = json.loads(urltemp.read().decode())
    return data
    
def get_price():
    data = get_json("https://api.cryptowat.ch/markets/binance/xmrusdt/ohlc?periods=14400")
    prices = [[float(x[0]),float(x[4])] for x in list(data['result']['14400'])]
    cache(prices,"price")

def get_block_reward():
    blocks = get_csv("blocks")
    data = [[x[0],x[3]] for x in blocks]
    return data[-1]

def get_block_time():
    blocks = get_csv("blocks")
    data = [[blocks[0][0],120]]
    for x in blocks[1:]:
        data.append([x[0],(x[0]-data[-1][0])+1])
    data = [[data[i][0],sum([data[i-j][1] for j in range(60)])/60] for i in range(60,len(data))]
    data = data[:60]+data
    return data[-1]

def get_difficulty():
    blocks = get_csv("blocks")
    data = []
    for x in blocks:
        data.append([x[0],x[2]])
    return data[-1]
    
def get_supply():
    reward = get_block_reward()
    supply = [[reward[0][0],0.0]]
    for x in reward[1:]:
        supply.append([x[0],x[1] + supply[-1][1]])
    return supply[-1]

def get_hashrate():
    block_time = get_block_time()
    difficulty = get_difficulty()
    data = [[difficulty[0][0],difficulty[0][1]/(block_time[0][0])]]
    for i in range(len(difficulty[1:])):
        data.append([difficulty[i][0],difficulty[i][1]/(block_time[i][1])])
    return data[-1]
    
def get_transactions():
    blocks = get_csv("blocks")
    data = [[x[0],x[4]] for x in blocks]
    return data
    
def convert_to_month(data):
    start = time.time() - 30*24*60*60

    # find earliest block
    i = len(data) - 1
    while float(data[i][0]) > start:
        i -= 1
        
    # cut off earlier blocks
    data = data[i:]
    
    # want 360 data points
    l = int(len(data)/360)
    data = [data[i] for i in range(len(data)) if i % l == 0]
    
    return data    
        

def convert_to_year(data):
    last_month = convert_to_month(data)
    
    start = time.time() - 360*24*60*60

    # find earliest block
    i = len(data) - 1
    while float(data[i][0]) > start:
        i -= 1
        
    # cut off earlier blocks
    data = data[i:]
    
    #find last block
    finish = time.time() - 30*24*60*60
    i = len(data) - 1
    while float(data[i][0]) > finish:
        i -= 1
    data = data[:i]
    
    # want 360 data points
    l = int(len(data)/360)
    data = [data[i] for i in range(len(data)) if i % l == 0]
    
    data.append(last_month)
    return data    
        

def convert_to_all(data):
    last_year = convert_to_year(data)

    #find last block
    finish = time.time() - 360*24*60*60
    i = len(data) - 1
    while float(data[i][0]) > finish:
        i -= 1
    data = data[:i]
    
    # want 360 data points
    l = int(len(data)/360)
    data = [data[i] for i in range(len(data)) if i % l == 0]
    
    data.append(last_year)
    
    return data
        
'''      
get_blocks()
print(convert_to_month("transactions"))
'''
#1000000 block is when time changes
get_blocks()



