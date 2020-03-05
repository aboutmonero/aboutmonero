import math
import matplotlib
import matplotlib.pyplot as plt
import convert_time as ct
import matplotlib.dates as mdate

def get_chart(data,title,xlabel,ylabel,dur, scale = "linear"):
    if dur != 'raw':
        data = ct.convert(data,dur)
        
    # Convert to the correct format for matplotlib.
    # mdate.epoch2num converts epoch timestamps to the right format for matplotlib
    secs = mdate.epoch2num([x[0] for x in data])

    fig, ax = plt.subplots()
    # plt.scatter(secs, [x[1] for x in data],s=.01)
    # Plot the date using plot_date rather than plot
    ax.plot(secs, [x[1] for x in data],linewidth=1)

    if scale:
        ax.set(xlabel = xlabel, ylabel = ylabel, title = title +"_" + dur, yscale = scale)
    else:
        ax.set(xlabel = xlabel, ylabel = ylabel, title = title +"_" + dur)
    ax.grid()
    
    # Choose your xtick format string
    date_fmt = '%m/%d/%y'
    
    # Use a DateFormatter to set the data to the correct format.
    date_formatter = mdate.DateFormatter(date_fmt)
    ax.xaxis.set_major_formatter(date_formatter)
    
    # Sets the tick labels diagonal so they fit easier.
    fig.autofmt_xdate()
    
    fig.set_size_inches(16,5)
    fig.savefig("static/data/"+ title +"_" + dur + ".png",dpi=200)
    plt.close(fig)
    return True





















