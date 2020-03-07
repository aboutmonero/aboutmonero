from history import *
from chart import *
from cache import *
import time

'''
cache_blocks()
cache_price()
'''
labels = [{
    'title' : 'inflation',
    'x-axis' : 'date',
    'y-axis' : '1y emission % of total supply',
    'scale' : 'linear',
    'options' : None
    } , {
    'title' : 'marketcap',
    'x-axis' : 'date',
    'y-axis' : '$',
    'scale' : 'log',
    'options' : None
    } , {
    'title' : 'block_time',
    'x-axis' : 'date',
    'y-axis' : 's',
    'scale' : 'linear',
    'options' : None
    } , {
    'title' : 'hashrate',
    'x-axis' : 'date',
    'y-axis' : 'Hashes/s',
    'scale' : 'log',
    'options' : None
    } , {
    'title' : 'supply',
    'x-axis' : 'date',
    'y-axis' : 'monero',
    'scale' : 'linear',
    'options' : None
    } , {
    'title' : 'price',
    'x-axis' : 'date',
    'y-axis' : '$',
    'scale' : 'log',
    'options' : None
    } , {
    'title' : 'block_reward',
    'x-axis' : 'date',
    'y-axis' : 'monero',
    'scale' : 'log',
    'options' : None
    } , {
    'title' : 'block_count',
    'x-axis' : 'date',
    'y-axis' : '#',
    'scale' : 'log',
    'options' : None
    }, {
    'title' : 'block_height',
    'x-axis' : 'date',
    'y-axis' : '#',
    'scale' : 'linear',
    'options' : None
    }, {
    'title' : 'transaction',
    'x-axis' : 'date',
    'y-axis' : '#',
    'scale' : 'log',
    'options' : None
    }, {
    'title' : 'fee',
    'x-axis' : 'date',
    'y-axis' : 'monero',
    'scale' : 'log',
    'options' : 'avg'
    }, {
    'title' : 'version',
    'x-axis' : 'date',
    'y-axis' : '#',
    'scale' : None,
    'options' : None
    }, {
    'title' : 'block_size',
    'x-axis' : 'date',
    'y-axis' : 'b',
    'scale' : 'log',
    'options' : 'avg'
    }, {
    'title' : 'blockchain_size',
    'x-axis' : 'date',
    'y-axis' : 'b',
    'scale' : 'linear',
    'options' : None
    }, {
    'title' : 'nonce',
    'x-axis' : 'date',
    'y-axis' : 'Uniformity',
    'scale' : 'linear',
    'options' : 'var'
    }]

blocks = get_blocks()
times = blocks.pop(0)
times.pop(0)
while blocks:
    data = blocks.pop()
    title = data.pop(0)
    label = [x for x in labels if x['title'] == title]
    if label:
        label = label[0]
        build_chart(times,data,label['title'],label['x-axis'],label['y-axis'],'all',label['scale'])
        build_chart(times[-int(365*24*60/2):],data[-int(365*24*60/2):],label['title'],label['x-axis'],label['y-axis'],'1Y',label['scale'])
        build_chart(times[-int(30*24*60/2):],data[-int(30*24*60/2):],label['title'],label['x-axis'],label['y-axis'],'1M',label['scale'])

update_latest(block)
