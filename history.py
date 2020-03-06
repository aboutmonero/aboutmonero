import time
from cache import *
from math_in_place import *
import collections

block = {
    'timestamp' : 0,
    'price' : 0,
    'block_reward' : 0,
    'reward_1y' : 0,
    'block_size' : 0,
    'block_height' : 0,
    'nonce' : 1,
    'version' : 0,
    'fee' : 0,
    'block_time' : 0,
    'supply' : 0,
    'block_size' : 0,
    'blockchain_size' : 0,
    'hashrate' : 0,
    'transaction' : 0,
    'block_count' : 0,
    'marketcap' : 0,
    'inflation' : 0,
}

def get_all():
    blocks = get_csv("blocks")[::-1]
    price = get_csv("price")[::-1]
    
    p = price.pop()    
    block['price'] = p[1]
    
    out = []
    day = collections.deque([])
    year = collections.deque([])
    
    nonces = collections.deque([])
    bin_size = int((2**32)/720)
    bin_count = [0 for i in range((2**32)//(bin_size)+1)]
    unique_bins = 0
    
    while blocks:
        x = blocks.pop()
        
        block['timestamp'] = x[0]
        day.append([x[0],x[4]])
        block['transaction'] += x[4]
        block['block_count'] += 1
        
        while day[0][0] < x[0] - 24*60*60:
            block['transaction'] -= day.popleft()[1]
            block['block_count'] -= 1
        
        block['block_time']=(24*60*60/block['block_count'])
        
        year.append([x[0],x[3]])
        block['block_reward'] = x[3]
        block['reward_1y'] += x[3]
        block['supply'] += x[3]
        block['blockchain_size'] += x[6]
        block['block_size'] = x[6]
        
        while year[0][0] < x[0] - 365*24*60*60:
            block['reward_1y'] -= year.popleft()[1]
        
        block['inflation']  = 100 * block['reward_1y'] / block['supply']
        
        while p[0] < x[0]:
            p = price.pop()
            block['price'] = p[1]
            
        block['marketcap']=block['supply']*block['price']
        block['hashrate'] = x[2] / (block['block_time'])
        block['fee'] = x[5]
        block['nonce'] = int(x[7])
        block['block_height'] = int(x[1])
        block['version'] = str(int(x[8]))+"."+str(int(x[9]))
        
        out.append(block.copy())
        
    return out
