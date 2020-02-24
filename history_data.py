import csv
import urllib.request
import json 
import time
import math


def get_last(direc):
    with open("static/data/"+direc+".csv", 'r') as f:
        reader = csv.reader(f)
        rows=list(reader)
    if rows:
        return int(rows[-1][0])
    else:
        return 0
        
def cache(data,direc):
    last = get_last(direc)
    with open("static/data/"+direc+".csv", 'a+') as f:
        writer = csv.writer(f) 
        for x in data:
            if int(x[0]) > last:
                writer.writerow(x)  
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
    data = get_json("https://www.xmrchain.net/api/networkinfo")['data']['hash_rate']
    return int(data['data']['height'])
        
def get_blocks():
    last = get_last("blocks")
    new = []
    current = 10000 #get_current_block()
    while current > last:
        data = get_json("https://www.xmrchain.net/api/block/"+str(last))['data']
        new = [[data['block_height'],data['timestamp'],data['size'],len(data['txs']),data['txs'][0]['xmr_outputs']]]
        last +=1
        cache(new,"blocks")
    
def get_hashrate():
    return get_json("https://www.xmrchain.net/api/networkinfo")['data']['hash_rate']

'''
def get_supply():

def get_marketcap():

def get_inflation_rate():
        
def get_block_reward():

def get_block_size_24h():

def get_blockchain_size():

def get_transactions_24h():


#def get_pending_transactions():

#def get_confirmation_time():

#def get_largest_pool():

#def get_reddit_posts_7d():

#def get_github_commits_7d():    
'''

get_blocks()

