import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

labels = {
    'inflation': {
        'title' : 'Inflation Rate',
        'file-name' : 'inflation',
        'x-axis' : 'Date',
        'y-axis' : '% of Circulating Supply',
        'scale' : 'log',
        'options' : None
    } ,
    'marketcap': {
        'title' : 'Value of Circulating Supply',
        'file-name' : 'marketcap',
        'x-axis' : 'Date',
        'y-axis' : '$',
        'scale' : 'log',
        'options' : None
    } , 
    'block_time': {
        'title' : 'Block Time',
        'file-name' : 'block_time',
        'x-axis' : 'Date',
        'y-axis' : 'Seconds',
        'scale' : 'linear',
        'options' : None
    } , 
    'hashrate': {
        'title' : 'Network Hashrate',
        'file-name' : 'hashrate',
        'x-axis' : 'Date',
        'y-axis' : 'Hashes/Second',
        'scale' : 'log',
        'options' : None
    } , 
    'supply': {
        'title' : 'Circulating Supply',
        'file-name' : 'supply',
        'x-axis' : 'Date',
        'y-axis' : 'ℳ',
        'scale' : 'linear',
        'options' : None
    } , 
    'price': {
        'title' : 'Price',
        'file-name' : 'price',
        'x-axis' : 'Date',
        'y-axis' : '$',
        'scale' : 'log',
        'options' : None
    } , 
    'block_reward': {
        'title' : "Miner's Block Reward",
        'file-name' : 'block_reward',
        'x-axis' : 'Date',
        'y-axis' : 'ℳ',
        'scale' : 'log',
        'options' : None
    } , 
    'block_count': {
        'title' : 'Block Count (24h)',
        'file-name' : 'block_count',
        'x-axis' : 'date',
        'y-axis' : '# of Blocks',
        'scale' : 'log',
        'options' : None
    } , 
    'block_height': {
        'title' : 'Block Height',
        'file-name' : 'block_height',
        'x-axis' : 'Date',
        'y-axis' : '# of Blocks',
        'scale' : 'linear',
        'options' : None
    } , 
    'transaction': {
        'title' : 'Transactions (24h)',
        'file-name' : 'transaction',
        'x-axis' : 'Date',
        'y-axis' : '# of Transactions',
        'scale' : 'log',
        'options' : None
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
        'options' : None
    } , 
    'block_size': {
        'title' : 'Block Size (Geometric Mean Of 720 Blocks)',
        'file-name' : 'block_size',
        'x-axis' : 'Date',
        'y-axis' : 'b',
        'scale' : 'log',
        'options' : 'avg'
    } , 
    'blockchain_size': {
        'title' : 'Blockchain Size',
        'file-name' : 'blockchain_size',
        'x-axis' : 'Date',
        'y-axis' : 'b',
        'scale' : 'linear',
        'options' : None
    } , 
    'nonce': {
        'title' : 'Nonce Uniformity',
        'file-name' : 'nonce',
        'x-axis' : 'Date',
        'y-axis' : 'Uniformity',
        'scale' : 'linear',
        'options' : 'var'
    }
}
    
def build_chart(x_data, y_data, label_req, dur, scatter = False ):   
    matplotlib.rcParams.update({'font.size': 5, 'font.family': 'monospace'})
    label = labels[label_req]
    
    dates = mdate.epoch2num(x_data)
    fig, ax = plt.subplots()
    if scatter:
        plt.scatter(dates, y_data,s=.01)
    else:
        ax.plot(dates, y_data,linewidth=.5)

    if label['scale']:
        if 'ℳ' in list(label['y-axis']) :
            plt.ylabel('ℳ', fontdict = {'family': 'sans'})
        ax.set(xlabel = label['x-axis'], ylabel = label['y-axis'], title = label['title'], yscale = label['scale'])
    else:
        ax.set(xlabel = label['x-axis'], ylabel = label['y-axis'], title = label['title'])
    ax.grid()

    date_fmt = '%m/%d/%y'
    date_formatter = mdate.DateFormatter(date_fmt)
    ax.xaxis.set_major_formatter(date_formatter)
    fig.set_size_inches(8,5)
    fig.savefig("static/data/"+ label['file-name'] +"_" + dur + ".png",dpi=150,bbox_inches='tight')
    plt.cla() 
    plt.clf() 
    plt.close('all')
    return True

















