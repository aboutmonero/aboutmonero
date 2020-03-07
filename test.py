from history import *
from chart import *
from cache import *

label = {
    'title' : 'block_size',
    'x-axis' : 'date',
    'y-axis' : '1y emission % of total supply',
    'scale' : 'log'
}

chart_data = [[x['timestamp'],x[label['title']]] for x in get_blocks()]
chart_data = avg(chart_data,720,log=True)
build_chart(chart_data,label['title'],label['x-axis'],label['y-axis'],'all',label['scale'])



