import math
import matplotlib
import matplotlib.pyplot as plt
import convert_time as ct
import matplotlib.dates as mdate
from math_in_place import *

def build_chart(x_data,y_data,title,xlabel,ylabel, dur, scale, scatter = False ):   
    
    # Convert to the correct format for matplotlib.
    # mdate.epoch2num converts epoch timestamps to the right format for matplotlib
    secs = mdate.epoch2num(x_data)
    
    fig, ax = plt.subplots()
    if scatter:
        plt.scatter(secs, y_data,s=.01)
    else:
        # Plot the date using plot_date rather than plot
        ax.plot(secs, y_data,linewidth=1)

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
    
    fig.set_size_inches(16,10)
    fig.savefig("static/data/"+ title +"_" + dur + ".png",dpi=200,bbox_inches='tight')
    # Clear the current axes.
    plt.cla() 
    # Clear the current figure.
    plt.clf() 
    # Closes all the figure windows.
    plt.close('all')
    import gc; gc.collect()
    return True

















