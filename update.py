from block_data import last_block, get_blocks
from chart import build_chart
from cache import update_latest, cache_blocks, cache_price
import gc

cache_blocks()
cache_price()

data = get_block_data()
timestamp = data.pop(0)
timestamp.pop(0)
update_latest(last_block)

while data:
    gc.collect()
    yaxis = data.pop()
    title = yaxis.pop(0)
    build_chart(timestamp,yaxis,title,'all')
    build_chart(timestamp[-int(365*24*60/2):],yaxis[-int(365*24*60/2):],title,'1Y')
    build_chart(timestamp[-int(30*24*60/2):],yaxis[-int(30*24*60/2):],title,'1M')


