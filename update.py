from history import *
from chart import *
from cache import *


cache_blocks()
cache_price()


durations = ['1M','1Y','all']
blocks = get_all()
labels = [{
    'title' : 'inflation',
    'x-axis' : 'date',
    'y-axis' : '1y emission % of total supply',
    'scale' : 'linear'
    } , {
    'title' : 'marketcap',
    'x-axis' : 'date',
    'y-axis' : '$',
    'scale' : 'log'
    } , {
    'title' : 'block_time',
    'x-axis' : 'date',
    'y-axis' : 's',
    'scale' : 'linear'
    } , {
    'title' : 'hashrate',
    'x-axis' : 'date',
    'y-axis' : 'Hashes/s',
    'scale' : 'log'
    } , {
    'title' : 'supply',
    'x-axis' : 'date',
    'y-axis' : 'monero',
    'scale' : 'linear'
    } , {
    'title' : 'price',
    'x-axis' : 'date',
    'y-axis' : '$',
    'scale' : 'log'
    } , {
    'title' : 'block_reward',
    'x-axis' : 'date',
    'y-axis' : 'monero',
    'scale' : 'log'
    } , {
    'title' : 'block_count',
    'x-axis' : 'date',
    'y-axis' : '#',
    'scale' : 'log'
    }, {
    'title' : 'block_height',
    'x-axis' : 'date',
    'y-axis' : '#',
    'scale' : 'linear'
    }, {
    'title' : 'transaction',
    'x-axis' : 'date',
    'y-axis' : '#',
    'scale' : 'log'
    }, {
    'title' : 'fee',
    'x-axis' : 'date',
    'y-axis' : 'monero',
    'scale' : 'log'
    }, {
    'title' : 'version',
    'x-axis' : 'date',
    'y-axis' : '#',
    'scale' : None
    }, {
    'title' : 'block_size',
    'x-axis' : 'date',
    'y-axis' : 'b',
    'scale' : 'log'
    }, {
    'title' : 'blockchain_size',
    'x-axis' : 'date',
    'y-axis' : 'b',
    'scale' : 'linear'
    }, {
    'title' : 'nonce',
    'x-axis' : 'date',
    'y-axis' : 'Uniformity',
    'scale' : 'linear'
    }]
for label in labels:
    if label['title'] == 'block_size':
        chart_data = [[x['timestamp'],x[label['title']]] for x in blocks]
        chart_data = avg(chart_data,720,log=True)
        blocks[-1][label['title']] = chart_data[-1][1]
    elif label['title'] == 'nonce':
        chart_data = [[x['timestamp'],x[label['title']]] for x in blocks]
        chart_data = var(chart_data,720)
        blocks[-1][label['title']] = chart_data[-1][1]
    elif label['title'] == 'fee':
        chart_data = [[x['timestamp'],x[label['title']]] for x in blocks if x[label['title']]]
        chart_data = avg(chart_data,720,log=True)
        blocks[-1][label['title']] = chart_data[-1][1]
    else:
        chart_data = [[x['timestamp'],x[label['title']]] for x in blocks]
    for duration in durations:
        build_chart(chart_data[2000:],label['title'],label['x-axis'],label['y-axis'],duration,label['scale'])

update_latest(blocks[-1])
