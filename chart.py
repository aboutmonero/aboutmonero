import math
import matplotlib
import matplotlib.pyplot as plt
import convert_time

def get_chart(data,title,xlabel,ylabel,dur, scale = "linear",):
    data = convert_time.convert(data,dur)
    fig, ax = plt.subplots()
    ax.plot([x[0] for x in data], [x[1] for x in data])
    ax.set(xlabel = xlabel, ylabel = ylabel, title = title +"_" + dur, yscale = scale)
    ax.grid()
    fig.set_size_inches(16,5)
    fig.savefig("static/data/"+ title +"_" + dur + ".png",dpi=100)
    plt.close(fig)
    return True





















