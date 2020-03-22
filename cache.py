from csv import reader, writer
import time
import urllib.request
from json import loads
from monero.daemon import Daemon
from monero.backends.jsonrpc import JSONRPCDaemon

def get_csv(direc,fl=True):
    if direc == 'blocks':
        with open(direc+"_1000000.csv", 'r') as f:
            read = reader(f)
            rows = list(read)   
        rows = [[float(y) for y in x] for x in rows]
        with open(direc+"_2000000.csv", 'r') as f:
            read = reader(f)
            newrows = list(read)   
        rows = rows + [[float(y) for y in x] for x in newrows]
        with open(direc+".csv", 'r') as f:
            read = reader(f)
            newrows = list(read)   
        rows = rows + [[float(y) for y in x] for x in newrows]
        return rows
    with open(direc+".csv", 'r') as f:
        rows = list(reader(f))
    rows = [[float(y) for y in x] for x in rows]
    return rows
        
def cache(data,direc):
    with open(direc+".csv", 'a+') as f:
        write = writer(f) 
        write.writerows(data)
    return True
            
def get_json(url):   
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as urltemp:
        data = loads(urltemp.read().decode())
    return data

def get_csv_from_url(url):   
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as urltemp:
        data = list(reader(urltemp.read().decode('latin-1').split('\n')))
    return data
        
def cache_price():
    last = str(int(get_csv("price")[-1][0]))
    prices = []
    data = get_json("https://api.cryptowat.ch/markets/binance/xmrusdt/ohlc?periods=7200&after="+last)
    data = list(data['result']['7200'])[1:]
    for i in range(len(data)):
        prices.append([data[i][0],float(data[i][4])])
    if prices:
        return cache(prices,"price")
    else:
        return False

def cache_CPI():
    last = str(float(get_csv("CPIAUCSL")[-1][1]))
    cpi = []
    data = get_csv_from_url("https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL")[:-1]
    if last == str(data[-1][1]):
        return False
    else:
        cpi.append([time.time(),float(data[-1][1])])
        return cache(cpi,"CPIAUCSL")
        
def cache_wiki():
    last = str(int(get_csv("wiki")[-1][1]))
    now = str(int(time.time()/(60*60*24*365))+1970+1)
    data = get_json("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Monero_(cryptocurrency)/daily/"+last+"/"+now+"120100")
    data = list(data['items'])[-1]
    if data['timestamp'] == last:
        return False
    else:
        return cache([[time.time(),data['timestamp'],int(data['views'])]],"wiki")
                
def cache_blocks(last = None, end = None):
    daemon = Daemon(JSONRPCDaemon(host='10.8.0.4', port=18081))
    new = []
    if not end:
        end = daemon.height() - 1
    if not last:
        last = int(get_csv("blocks")[-1][1])
    while end > last:
        last +=1
        data = daemon.block(height=last)
        new.append([data.timestamp,data.height,data.difficulty,float(data.reward), \
            data.num_txes,float(data.fee),data.size,data.nonce,data.version[0],data.version[1]])
    if new:
        cache(new,"blocks")
        return True
    else:
        return False

def update_latest(targets):
    with open("latest.csv", 'r') as f:
        read = reader(f)
        rows = list(read)
    for target in targets.keys():
        for x in rows:
            if x[0] == target:
                x[1] = targets[target]
    with open("latest.csv", 'w') as f:
        write = writer(f) 
        write.writerows(rows)
    return True

def get_latest():
    with open("latest.csv", 'r') as f:
        read = reader(f)
        rows = list(read)
    for i in range(len(rows)):
        if i in [1,2,3,4,6,9,12,13,14,15,16,17]:
            rows[i] = "{0:,}".format(int(float(rows[i][1])))
        elif i == 10:
            rows[i] = "{0:,.6f}".format(float(rows[i][1]))
        else:
            rows[i] = "{0:,.2f}".format(float(rows[i][1]))
    return rows

