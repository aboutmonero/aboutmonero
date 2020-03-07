import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

labels = {
    'inflation': {
        'title' : 'inflation',
        'x-axis' : 'date',
        'y-axis' : '1y emission % of total supply',
        'scale' : 'linear',
        'options' : None
    } ,
    'marketcap': {
        'title' : 'marketcap',
        'x-axis' : 'date',
        'y-axis' : '$',
        'scale' : 'log',
        'options' : None
    } , 
    'block_time': {
        'title' : 'block_time',
        'x-axis' : 'date',
        'y-axis' : 's',
        'scale' : 'linear',
        'options' : None
    } , 
    'hashrate': {
        'title' : 'hashrate',
        'x-axis' : 'date',
        'y-axis' : 'Hashes/s',
        'scale' : 'log',
        'options' : None
    } , 
    'supply': {
        'title' : 'supply',
        'x-axis' : 'date',
        'y-axis' : 'monero',
        'scale' : 'linear',
        'options' : None
    } , 
    'price': {
        'title' : 'price',
        'x-axis' : 'date',
        'y-axis' : '$',
        'scale' : 'log',
        'options' : None
    } , 
    'block_reward': {
        'title' : 'block_reward',
        'x-axis' : 'date',
        'y-axis' : 'monero',
        'scale' : 'log',
        'options' : None
    } , 
    'block_count': {
        'title' : 'block_count',
        'x-axis' : 'date',
        'y-axis' : '#',
        'scale' : 'log',
        'options' : None
    } , 
    'block_height': {
        'title' : 'block_height',
        'x-axis' : 'date',
        'y-axis' : '#',
        'scale' : 'linear',
        'options' : None
    } , 
    'transaction': {
        'title' : 'transaction',
        'x-axis' : 'date',
        'y-axis' : '#',
        'scale' : 'log',
        'options' : None
    } , 
    'fee': {
        'title' : 'fee',
        'x-axis' : 'date',
        'y-axis' : 'monero',
        'scale' : 'log',
        'options' : 'avg'
    } , 
    'version': {
        'title' : 'version',
        'x-axis' : 'date',
        'y-axis' : '#',
        'scale' : None,
        'options' : None
    } , 
    'block_size': {
        'title' : 'block_size',
        'x-axis' : 'date',
        'y-axis' : 'b',
        'scale' : 'log',
        'options' : 'avg'
    } , 
    'blockchain_size': {
        'title' : 'blockchain_size',
        'x-axis' : 'date',
        'y-axis' : 'b',
        'scale' : 'linear',
        'options' : None
    } , 
    'nonce': {
        'title' : 'nonce',
        'x-axis' : 'date',
        'y-axis' : 'Uniformity',
        'scale' : 'linear',
        'options' : 'var'
    }
}
    
def build_chart(x_data, y_data, label, dur, scatter = False ):   

    matplotlib.rcParams.update({'font.size': 5})
    matplotlib.rcParams.update({'font.family': 'monospace'})
    matplotlib.rcParams.update({'font.weight': 'bold'})
    label = labels[label]
    
    dates = mdate.epoch2num(x_data)
    fig, ax = plt.subplots()
    if scatter:
        plt.scatter(dates, y_data,s=.01)
    else:
        ax.plot(dates, y_data,linewidth=.5)

    if label['scale']:
        ax.set(xlabel = label['x-axis'], ylabel = label['y-axis'], title = label['title'] +"_" + dur, yscale = label['scale'])
    else:
        ax.set(xlabel = label['x-axis'], ylabel = label['y-axis'], title = label['title'] +"_" + dur)
        
    ax.grid()

    date_fmt = '%m/%d/%y'
    date_formatter = mdate.DateFormatter(date_fmt)
    ax.xaxis.set_major_formatter(date_formatter)
    
    fig.set_size_inches(8,5)
    fig.savefig("static/data/"+ label['title'] +"_" + dur + ".png",dpi=150,bbox_inches='tight')
    plt.cla() 
    plt.clf() 
    plt.close('all')
    return True

















