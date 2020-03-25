from cache import get_csv
from collections import deque
from math import exp, log

last_block = {
    'timestamp' : 0,
    'price' : 0,
    'block_size' : 0,
    'blockchain_size' : 0,
    'block_count' : 0,
    'block_height' : 0,
    'block_reward' : 0,
    'nonce' : 1,
    'version' : 0,
    'fee' : 0,
    'block_time' : 10,
    'supply' : 0,
    'hashrate' : 0.1,
    'transaction' : 0,
    'transaction_block_max' : 0,
    'marketcap' : 0,
    'marketcap_infl' : 0,
    'inflation' : 0,
    '1yo': 0.0,
    'wiki_view': 0.0
}

def get_block_data():
    #setup output list with keys as first element
    output = [[i] for i in list(last_block.keys())]
    
    #import data from csv
    blocks = get_csv("blocks")[::-1]
    price = get_csv("price")[::-1]
    cpi = get_csv("CPIAUCSL")[::-1]
    wiki = get_csv("wiki")[::-1]
    
    #initiate price
    p = price.pop()    
    last_block['price'] = p[1]
    
    #initiate wiki
    w = wiki.pop()    
    last_block['wiki_views'] = w[2]
    
    #initiate cpi
    cpi_last = cpi.pop()
    reference_cpi = cpi_last[1]
    
    #stacks for fast processing
    day = deque([])
    year = deque([])
    nonces = deque([])
    fees = deque([])
    block_sizes = deque([])
    
    #nonce uniformity constants
    #there are 2160 nonces and 2160 bins
    bin_size = int((2**32)/(720*3))
    #we count how many nonces are in each bin
    bin_count = [0 for i in range((2**32)//(bin_size)+1)]
    #the number of bins with only 1 nonce should be about 1/e
    unique_bins = 0
    
    #block reward over 1y
    reward_1y = 0
    
    while blocks:
        #block data
        x = blocks.pop()
        
        #no calculation data
        last_block['timestamp'] = x[0]
        last_block['block_height'] = int(x[1])
        last_block['version'] = str(int(x[8]))+"."+str(int(x[9]))
        last_block['block_reward'] = x[3]
        last_block['supply'] += x[3]
        last_block['blockchain_size'] += x[6]
        
        #24h stats
        day.append([x[0],x[4]])
        last_block['transaction'] += x[4]
        last_block['block_count'] += 1
        last_block['transaction_block_max'] = max(last_block['transaction_block_max'],x[4])
        if maxmax[1] < last_block['transaction_block_max']:
            maxmax = [x[1],last_block['transaction_block_max']]
        print(maxmax)
        #remove old data
        while day[0][0] < x[0] - 24*60*60:
            head = day.popleft()[1]
            last_block['transaction'] -= head
            last_block['block_count'] -= 1
            last_block['block_time']=((24*60*60)/last_block['block_count'])
            last_block['hashrate'] = x[2] / (last_block['block_time'])
            if head == last_block['transaction_block_max']:
                last_block['transaction_block_max'] = max([x[1] for x in day])
        
        #price
        while p[0] < x[0] and price:
            p = price.pop()
            last_block['price'] = p[1]
            
        #inflation 1y %
        reward_1y += x[3]
        last_block['1yo'] += last_block['price']*x[3]
        year.append([x[0],[last_block['price'],x[3]]])
        while year[0][0] < x[0] - 365*24*60*60:
            amt = year.popleft()[1]
            reward_1y -= amt[1]
            last_block['1yo'] -= amt[0]*amt[1]
        last_block['inflation']  = 100 * reward_1y / last_block['supply']

        #CPI
        while cpi_last[0] < x[0] and cpi:
            cpi_last = cpi.pop()
            
        #wiki
        while w[0] < x[0] and wiki:
            w = wiki.pop()
            last_block['wiki_view'] = w[2]
            
        last_block['marketcap']=last_block['supply']*last_block['price']
        last_block['marketcap_infl']=last_block['supply']*last_block['price']/(cpi_last[1]/reference_cpi)
        
        #fee geometric mean
        if x[5]:
            fees.append(x[5])
            if len(fees) > 720:
                last_block['fee'] = exp(log(last_block['fee']) + log(x[5]/fees.popleft())/720)
            else:
                last_block['fee'] = x[5]
        
        #block_size geometric mean    
        block_sizes.append(x[6])
        if len(block_sizes) > 720:
            last_block['block_size'] = exp(log(last_block['block_size']) + log(x[6]/block_sizes.popleft())/720)
        else:
            last_block['block_size'] = x[6]
        
        #nonce uniformity
        #calculate which bin the nonce belongs in like a histogram
        nonce = int(x[7])//bin_size
        #add to memory
        nonces.append(nonce)
        #put nonce into bin
        bin_count[nonce] += 1
        #recalculate bins with exactly one
        if bin_count[nonce] == 1:
            unique_bins += 1 
        elif bin_count[nonce] == 2:
            unique_bins -= 1 
        if len(nonces)> 720*3:    
            #remove nonce and recalculate
            nonce = nonces.popleft()    
            bin_count[nonce] -= 1
            if bin_count[nonce] == 1:
                unique_bins += 1 
            elif bin_count[nonce] == 0:
                unique_bins -= 1
        #assuming the nonces are uniformly random, unique_bins : 2160 == 1 : e
        #thus e * unique_bins / 2160 == 1
        last_block['nonce'] = (exp(1)*unique_bins/(720*3))*100
        
        for i in range(len(output)):
            output[i].append(list(last_block.values())[i])
        
    return output
