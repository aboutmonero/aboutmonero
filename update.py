from history import *
from chart import *
from cache import *

cache_blocks()
cache_price()

infl = get_inflation()
get_chart(infl,"inflation","Date","% of Total Supply","all",scale='log')
get_chart(infl,"inflation","Date","% of Total Supply","1Y",scale='log')
get_chart(infl,"inflation","Date","% of Total Supply","1M",scale='log')

infl = get_marketcap()
get_chart(infl,"marketcap","Date","$","all",scale='log')
get_chart(infl,"marketcap","Date","$","1Y",scale='log')
get_chart(infl,"marketcap","Date","$","1M",scale='log')

infl = get_price()
get_chart(infl,"price","Date","$","all",scale='log')
get_chart(infl,"price","Date","$","1Y",scale='log')
get_chart(infl,"price","Date","$","1M",scale='log')

infl = get_block_reward()
get_chart(infl,"block_reward","Date","ℳ","all",scale='log')
get_chart(infl,"block_reward","Date","ℳ","1Y",scale='log')
get_chart(infl,"block_reward","Date","ℳ","1M",scale='log')

infl = get_supply()
get_chart(infl,"supply","Date","ℳ","all")
get_chart(infl,"supply","Date","ℳ","1Y")
get_chart(infl,"supply","Date","ℳ","1M")


infl = get_hashrate()
get_chart(infl,"hashrate","Date","H/s","all",scale='log')
get_chart(infl,"hashrate","Date","H/s","1Y",scale='log')
get_chart(infl,"hashrate","Date","H/s","1M",scale='log')

infl = get_transactions()
get_chart(infl,"transactions","Date","#","all",scale='log')
get_chart(infl,"transactions","Date","#","1Y",scale='log')
get_chart(infl,"transactions","Date","#","1M",scale='log')


infl = get_block_count()
get_chart(infl,"block_count","Date","#","all",scale='log')
get_chart(infl,"block_count","Date","#","1Y",scale='log')
get_chart(infl,"block_count","Date","#","1M",scale='log')

infl = get_block_size()
get_chart(infl,"block_size","Date","b","all",scale='log')
get_chart(infl,"block_size","Date","b","1Y",scale='log')
get_chart(infl,"block_size","Date","b","1M",scale='log')

infl = get_blockchain_size()
get_chart(infl,"blockchain_size","Date","b","all",scale='log')
get_chart(infl,"blockchain_size","Date","b","1Y",scale='log')
get_chart(infl,"blockchain_size","Date","b","1M",scale='log')

infl = get_fees()
get_chart(infl,"fees","Date","ℳ","all",scale = 'log')
get_chart(infl,"fees","Date","ℳ","1Y",scale = 'log')
get_chart(infl,"fees","Date","ℳ","1M",scale = 'log')

infl = get_nonces()
get_chart(infl,"nonces","Date","Randomness","all",scale = 'log')
get_chart(infl,"nonces","Date","Randomness","1Y",scale='log')
get_chart(infl,"nonces","Date","Randomness","1M",scale='log')






