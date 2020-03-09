from history import block, get_blocks
from chart import build_chart
from cache import update_latest, cache_blocks, cache_price
import gc

#cache_blocks()
#cache_price()

data = get_blocks()
timestamp = data.pop(0)
timestamp.pop(0)
update_latest(block)

while data:
    gc.collect()
    yaxis = data.pop()
    title = yaxis.pop(0)
    build_chart(timestamp,yaxis,title,'all')
    build_chart(timestamp[-int(365*24*60/2):],yaxis[-int(365*24*60/2):],title,'1Y')
    build_chart(timestamp[-int(30*24*60/2):],yaxis[-int(30*24*60/2):],title,'1M')


