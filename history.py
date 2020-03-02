import time
import math
import convert_time
import chart
import cache

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
    data = cache.get_csv("price")
    return data
            
def get_block_reward():
    blocks = cache.get_csv("blocks")
    data = [[x[0],x[3]] for x in blocks]
    return data

def get_block_time():
    blocks = cache.get_csv("blocks")
    data = [[blocks[0][0],120]]
    for x in blocks[1:]:
        data.append([x[0],(x[0]-data[-1][0])+1])
    info = [x[1] for x in data]
    info = avg(info, 300)    
    data = [[data[i][0],info[i-300]] for i in range(300,len(data))]
    data = data[:300]+data
    return data 

def get_difficulty():
    blocks = cache.get_csv("blocks")
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
    block_time = cget_block_time()
    difficulty = get_difficulty()
    data = [[difficulty[0][0],difficulty[0][1]/(block_time[0][0])]]
    for i in range(len(difficulty[1:])):
        data.append([difficulty[i][0],difficulty[i][1]/(block_time[i][1])])
    return data 
    
def get_transactions():
    blocks = cache.get_csv("blocks")
    data = [[x[0],x[4]] for x in blocks]
    info = [x[1] for x in data]
    info = avg(info, 300,log=True)    
    data = [[data[i][0],info[i-300]] for i in range(300,len(data))]
    data = data[:300]+data
    return data
    

chart.get_chart(get_price(),"price","UNIX timestamp","$/ℳ","all", scale = "log")
























