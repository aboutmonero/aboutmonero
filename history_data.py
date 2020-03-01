import csv
import urllib.request
import json 
import time
import math
from monero.daemon import Daemon
from monero.backends.jsonrpc import JSONRPCDaemon
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt


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
    
def avg(data, length, log = False):
    if log:
        data = [math.log(x) for x in data]
    s = sum(data[:length])
    avg = [s/length]
    for i in range(len(data)-length):
        s += data[i+length] 
        s -= data[i]
        avg.append(s/length)
    if log:
        avg = [math.exp(x) for x in avg]
    return avg 
        
def get_price():
    data = get_json("https://api.cryptowat.ch/markets/binance/xmrusdt/ohlc?periods=14400")
    prices = [[float(x[0]),float(x[4])] for x in list(data['result']['14400'])]
    cache(prices,"price")
        
def get_blocks():
    daemon = Daemon(JSONRPCDaemon(port=18081))
    last = 1500000
    new = []
    current = 2045023
    while current > last:
        data = daemon.block(height=last)
        new.append([datetime.fromisoformat(str(data.timestamp)).timestamp(),data.height,data.difficulty,float(data.reward),len(data.transactions)])
        last +=1
        if(last%10000==0):
            cache(new,"blocks")
            new = []
            print(last)

    return True

def get_block_reward():
    blocks = get_csv("blocks")
    data = [[x[0],x[3]] for x in blocks]
    return data

def get_block_time():
    blocks = get_csv("blocks")
    data = [[blocks[0][0],120]]
    for x in blocks[1:]:
        data.append([x[0],(x[0]-data[-1][0])+1])
    info = [x[1] for x in data]
    info = avg(info, 300)    
    data = [[data[i][0],info[i-300]] for i in range(300,len(data))]
    data = data[:300]+data
    return data 

def get_difficulty():
    blocks = get_csv("blocks")
    data = []
    for x in blocks:
        data.append([x[0],x[2]])
    return data 
    
def get_supply():
    reward = get_block_reward()
    supply = [[reward[0][0],0.0]]
    for x in reward[1:]:
        supply.append([x[0],x[1] + supply[-1][1]])
    return supply

def get_hashrate():
    block_time = get_block_time()
    difficulty = get_difficulty()
    data = [[difficulty[0][0],difficulty[0][1]/(block_time[0][0])]]
    for i in range(len(difficulty[1:])):
        data.append([difficulty[i][0],difficulty[i][1]/(block_time[i][1])])
    return data 
    
def get_transactions():
    blocks = get_csv("blocks")
    data = [[x[0],x[4]] for x in blocks]
    info = [x[1] for x in data]
    info = avg(info, 300,log=True)    
    data = [[data[i][0],info[i-300]] for i in range(300,len(data))]
    data = data[:300]+data
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
    
    data = data + last_month
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
    
    data = data + last_year
    
    return data
        
'''      
get_blocks()
print(convert_to_month("transactions"))
'''
#1000000 block is when time changes
def get_chart(data,title,xlabel,ylabel):
    fig, ax = plt.subplots()
    ax.plot([x[0] for x in data], [x[1] for x in data])
    ax.set(xlabel = xlabel, ylabel = ylabel, title = title)
    ax.grid()
    fig.savefig("static/data/"+ title + ".png")
    return True

get_chart(convert_to_month(get_block_reward()),"block_reward_1M","UNIX timestamp","Reward per block")
