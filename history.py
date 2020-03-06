import time
from cache import *
from math_in_place import *
            
def get_price():
    data = get_csv("price")
    update_latest('price',data[-1][1])
    return data 
            
def get_block_reward():
    blocks = get_csv("blocks")
    data = [[x[0],x[3]] for x in blocks]
    update_latest('block_reward',data[-1][1])
    return data

def get_block_time():
    blocks = get_csv("blocks")
    data = [[blocks[0][0],120]]
    for x in blocks[1:]:
        data.append([x[0],(x[0]-data[-1][0])+1])
    info = [x[1] for x in data]
    info = avg(info, 300)    
    data = [[data[i][0],info[i]] for i in range(len(data))]
    update_latest('block_time',data[-1][1])
    return data 

def get_difficulty():
    blocks = get_csv("blocks")
    data = []
    for x in blocks:
        data.append([x[0],x[2]])
    return data 
    
def get_supply():
    reward = get_block_reward()
    supply = [[reward[0][0],reward[0][1]]]
    s = 0
    for x in reward[1:]:
        s += x[1]
        supply.append([x[0],s])
    update_latest('supply',supply[-1][1])
    return supply

def get_hashrate():
    block_time = get_block_time()
    difficulty = get_difficulty()
    data = [[difficulty[0][0],difficulty[0][1]/(block_time[0][0])]]
    for i in range(len(difficulty[1:])):
        data.append([difficulty[i][0],difficulty[i][1]/(block_time[i][1])])
    update_latest('hashrate',data[-1][1])
    return data[50000:]
    
def get_transactions():
    blocks = get_csv("blocks")
    data = [[x[0],x[4]] for x in blocks]
    i = 0
    transactions = []
    while data[i][0] - data[0][0] < 24*60*60:
        i += 1
    j = i
    s = sum([x[1] for x in data[:j]])
    while j < len(data):
        s += data[j][1]
        while data[j][0] - data[j-i][0] > 24*60*60:
            s -= data[j-i][1]
            i -= 1
        while data[j][0] - data[j-i][0] < 24*60*60 and j + 1 < len(data):
            j += 1  
            i += 1
            s += data[j][1]
        transactions.append([data[j][0],s])
        s -= data[j-i][1]
        j += 1
    update_latest('transactions',transactions[-1][1])
    return transactions

def get_block_count():
    blocks = get_csv("blocks")
    data = [[x[0]] for x in blocks]
    i = 0
    block_count = []
    while data[i][0] - data[0][0] < 24*60*60:
        i += 1
    j = i
    while j < len(data):
        while data[j][0] - data[j-i][0] > 24*60*60:
            i -= 1
        while data[j][0] - data[j-i][0] < 24*60*60 and j + 1 < len(data):
            j += 1  
            i += 1
        block_count.append([data[j][0],i])
        j += 1
    update_latest('block_count',block_count[-1][1])
    return block_count
        
def get_marketcap():
    price = get_price()
    supply = get_supply()
    i = 0
    start = price[0][0]
    while supply[i][0]< start:
        i+=1
    supply = supply[i:]
    data = []
    j = 0
    for i in range(len(supply)):
        while price[j][0] < supply[i][0]:
            j+=1
        data.append([supply[i][0],supply[i][1]*price[j][1]])
    update_latest('marketcap',data[-1][1])
    return data   
    
def get_inflation():
    reward = get_block_reward()
    supply = get_supply()
    
    i = 0
    inflation = []
    while reward[i][0] - reward[0][0] < 360*24*60*60:
        i += 1
    j = i
    s = sum([x[1] for x in reward[:j]])
    while j < len(reward):
        s += reward[j][1]
        while reward[j][0] - reward[j-i][0] > 360*24*60*60:
            s -= reward[j-i][1]
            i -= 1
        while reward[j][0] - reward[j-i][0] < 360*24*60*60 and j + 1 < len(reward):
            j += 1  
            i += 1
            s += reward[j][1]
        inflation.append([reward[j][0],100*s/supply[j][1]])
        s -= reward[j-i][1]
        j += 1
    update_latest('inflation',inflation[-1][1])
    return inflation
    
def get_block_size(raw=False):
    blocks = get_csv("blocks")
    data = [[x[0],x[6]] for x in blocks]
    if raw:
        return data
    info = [x[1] for x in data]
    info = avg(info, 720,log=True)    
    data = [[data[i][0],info[i]] for i in range(len(data))]
    update_latest('block_size',data[-1][1])
    return data 

def get_blockchain_size():
    blocks = get_csv("blocks")
    size = [[x[0],x[6]] for x in blocks]
    chainsize = [[size[0][0],0.0]]
    s = 0
    for x in size[1:]:
        s += x[1]
        chainsize.append([x[0],s])
    update_latest('blockchain_size',chainsize[-1][1])
    return chainsize

def get_fees(raw=False):
    blocks = get_csv("blocks")
    data = [[x[0],x[5]] for x in blocks if x[5]]
    if raw:
        return data
    info = [x[1] for x in data]
    info = avg(info, 720,log=True)    
    data = [[data[i][0],info[i]] for i in range(len(data))] 
    update_latest('fees',data[-1][1])
    return data
    
def get_nonces(raw=False):
    blocks = get_csv("blocks")
    data = [[x[0],int(x[7])] for x in blocks]
    if raw:
        return data
    info = [x[1] for x in data]
    info = var(info, 10000)    
    data = [[data[i][0],info[i]] for i in range(len(data))]
    update_latest('nonces',data[-1][1])
    return data
    

def get_version_major():
    blocks = get_csv("blocks")
    data = [[x[0],x[8]] for x in blocks]
    update_latest('version_major',data[-1][1])
    return data

def get_version_minor():
    blocks = get_csv("blocks")
    data = [[x[0],x[9]] for x in blocks]
    update_latest('version_minor',data[-1][1])
    return data
    
def get_version():
    maj = get_version_major()
    mino = get_version_minor()
    maj = [[maj[i][0],str(int(maj[i][1]))+"."+str(int(mino[i][1]))] for i in range(len(maj))]
    return maj
    
def get_height():
    blocks = get_csv("blocks")
    data = [[blocks[i][0],i] for i in range(len(blocks))]
    update_latest('height',data[-1][1])
    return data







