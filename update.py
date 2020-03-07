from history import *
from chart import *
from cache import update_latest
import time
import gc

cache_blocks()
cache_price()

blocks = get_blocks()
times = blocks.pop(0)
times.pop(0)
while blocks:
    gc.collect()
    data = blocks.pop()
    title = data.pop(0)
    build_chart(times,data,title,'all')
    build_chart(times[-int(365*24*60/2):],data[-int(365*24*60/2):],title,'1Y')
    build_chart(times[-int(30*24*60/2):],data[-int(30*24*60/2):],title,'1M')

update_latest(block)
