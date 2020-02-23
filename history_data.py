import csv
import urllib.request
import json 
import time
import math


def cache(data,direc):
    with open(direc, 'w+') as f:
        writer = csv.writer(f) 
        for x in data:
            writer.writerow(x)  
            
def get_json(url):   
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as urltemp:
        data = json.loads(urltemp.read().decode())
    return data
    
def get_price():
    data = get_json("https://api.cryptowat.ch/markets/binance/xmrusdt/ohlc?periods=14400")
    prices = [[float(x[0]),float(x[4])] for x in list(data['result']['14400'])]
    cache(prices,"price.csv")
        
def get_current_height():
    data = get_json("https://www.xmrchain.net/api/block/200000")
    return int(data['data']['current_height'])
        
def get_blocks():
    last_block_height = 2037872-2*60
    new_blocks = []
    current_height = get_current_height()-5
    while current_height != last_block_height:
        time.sleep(5)
        data = get_json("https://www.xmrchain.net/api/block/"+str(last_block_height+1))['data']
        new_blocks = new_blocks + [[data['timestamp'],data['block_height'],data['size'],len(data['txs']),data['txs'][0]['xmr_outputs']]]
        last_block_height+=1
    return new_blocks
    
def get_hashrate():
    return get_json("https://www.xmrchain.net/api/networkinfo")['data']['hash_rate']
    

def get_supply():

def get_marketcap():

def get_inflation_rate():
        
def get_block_reward():

def get_block_size_24h():

def get_blockchain_size():

def get_transactions_24h():

'''
#def get_pending_transactions():

#def get_confirmation_time():

#def get_largest_pool():

#def get_reddit_posts_7d():

#def get_github_commits_7d():    
'''

get_blocks()
