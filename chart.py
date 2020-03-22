import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib.ticker import LogLocator
import matplotlib.dates as mdates

labels = {
    'inflation': {
        'title' : 'Inflation Rate',
        'file-name' : 'inflation',
        'x-axis' : 'Date',
        'y-axis' : '% of Circulating Supply',
        'scale' : 'log',
    } ,
    'marketcap': {
        'title' : 'Value of Circulating Supply',
        'file-name' : 'marketcap',
        'x-axis' : 'Date',
        'y-axis' : '$',
        'scale' : 'log',
    } , 
    'marketcap_infl': {
        'title' : 'Inflation Adjusted Value of Circulating Supply (2014 Dollars)',
        'file-name' : 'marketcap_infl',
        'x-axis' : 'Date',
        'y-axis' : '2014 $',
        'scale' : 'log',
    } , 
    'block_time': {
        'title' : 'Block Time',
        'file-name' : 'block_time',
        'x-axis' : 'Date',
        'y-axis' : 'Seconds',
        'scale' : 'linear',
    } , 
    'hashrate': {
        'title' : 'Network Hashrate',
        'file-name' : 'hashrate',
        'x-axis' : 'Date',
        'y-axis' : 'Hashes/Second',
        'scale' : 'log',
    } , 
    'supply': {
        'title' : 'Circulating Supply',
        'file-name' : 'supply',
        'x-axis' : 'Date',
        'y-axis' : 'ℳ',
        'scale' : 'linear',
    } , 
    'price': {
        'title' : 'Price',
        'file-name' : 'price',
        'x-axis' : 'Date',
        'y-axis' : '$',
        'scale' : 'log',
    } , 
    'block_reward': {
        'title' : "Miner's Block Reward",
        'file-name' : 'block_reward',
        'x-axis' : 'Date',
        'y-axis' : 'ℳ',
        'scale' : 'log',
    } , 
    'block_count': {
        'title' : 'Block Count (24h)',
        'file-name' : 'block_count',
        'x-axis' : 'date',
        'y-axis' : '# of Blocks',
        'scale' : 'log',
    } , 
    'block_height': {
        'title' : 'Block Height',
        'file-name' : 'block_height',
        'x-axis' : 'Date',
        'y-axis' : '# of Blocks',
        'scale' : 'linear',
    } , 
    'transaction': {
        'title' : 'Transactions (24h)',
        'file-name' : 'transaction',
        'x-axis' : 'Date',
        'y-axis' : '# of Transactions',
        'scale' : 'log',
    } , 
    'fee': {
        'title' : 'Fee per Block (Geometric Mean Of 720 Blocks)',
        'file-name' : 'fee',
        'x-axis' : 'Date',
        'y-axis' : 'ℳ',
        'scale' : 'log',
        'options' : 'avg'
    } , 
    'version': {
        'title' : 'Version',
        'file-name' : 'version',
        'x-axis' : 'Date',
        'y-axis' : '#',
        'scale' : None,
    } , 
    'block_size': {
        'title' : 'Block Size (Geometric Mean Of 720 Blocks)',
        'file-name' : 'block_size',
        'x-axis' : 'Date',
        'y-axis' : 'b',
        'scale' : 'log',
    } , 
    'blockchain_size': {
        'title' : 'Blockchain Size',
        'file-name' : 'blockchain_size',
        'x-axis' : 'Date',
        'y-axis' : 'b',
        'scale' : 'linear',
    } , 
    'nonce': {
        'title' : 'Nonce Uniformity',
        'file-name' : 'nonce',
        'x-axis' : 'Date',
        'y-axis' : 'Uniformity',
        'scale' : 'linear',
    } , 
    '1yo': {
        'title' : "1Y Miner's Reward",
        'file-name' : '1yo',
        'x-axis' : 'Date',
        'y-axis' : '$',
        'scale' : 'log',
    } , 
    'wiki_view': {
        'title' : 'Views of Monero (cryptocurrency) Page on en.wikipedia.org',
        'file-name' : 'wiki_view',
        'x-axis' : 'Date',
        'y-axis' : 'User View #',
        'scale' : 'log',
    }
}
    
def build_chart(x_data, y_data, label_req, dur, scatter = False ):   
    matplotlib.rcParams.update({'font.family': 'monospace'})
    label = labels[label_req]
    
    dates = mdate.epoch2num(x_data)
    fig, ax = plt.subplots()
    if scatter:
        plt.scatter(dates, y_data,s=.01)
    else:
        ax.plot(dates, y_data,linewidth=.5,color = 'black')

    if label['scale']:
        if 'ℳ' in list(label['y-axis']) :
            plt.ylabel('ℳ', fontdict = {'family': 'sans'})
        ax.set(xlabel = label['x-axis'], ylabel = label['y-axis'], title = label['title'], yscale = label['scale'])
    else:
        ax.set(xlabel = label['x-axis'], ylabel = label['y-axis'], title = label['title'])

    
    if label['scale']=='log':
        ax.yaxis.set_major_locator(LogLocator(base=10))
        ax.yaxis.set_minor_locator(LogLocator(base=10,subs=(0.1,)))
    
    
    date_fmt = '%m/%d/%y'
    date_formatter = mdate.DateFormatter(date_fmt)
    
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=3))
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_minor_formatter(date_formatter)
    ax.xaxis.set_major_formatter(date_formatter)
    
    ax.grid(which='major',linestyle = '--')
    ax.grid(which='minor',linestyle = ':')
    ax.grid(True)
    
    fig.set_size_inches(8,5)
    fig.savefig("static/data/"+ label['file-name'] +"_" + dur + ".png",dpi=150)
    plt.cla() 
    plt.clf() 
    plt.close('all')
    return True















