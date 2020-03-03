import time
import math
from datetime import datetime

def convert_to_1M(data):
    start = time.time() - 30*24*60*60

    # find earliest block
    i = len(data) - 1
    while float(data[i][0]) > start:
        i -= 1
        
    # cut off earlier blocks
    data = data[i:]
    
    # want 360 data points
    l = int(len(data)/300)
    if l:
        data = [data[i] for i in range(len(data)) if i % l == 0]
    
    return data    
        

def convert_to_1Y(data):
    last_month = convert_to_1M(data)
    
    start = time.time() - 360*24*60*60

    # find earliest block
    i = len(data) - 1
    while float(data[i][0]) > start:
        i -= 1
        
    # cut off earlier blocks
    data = data[i:]
    
    #find last block
    finish = time.time() - 30*24*60*60
    i = len(data) - 1
    while float(data[i][0]) > finish:
        i -= 1
    data = data[:i]
    
    # want n data points
    l = int(len(data)/300)
    if l:
        data = [data[i] for i in range(len(data)) if i % l == 0]
    
    data = data + last_month
    return data    
        

def convert_to_all(data):
    last_year = convert_to_1Y(data)

    #find last block
    finish = time.time() - 360*24*60*60
    i = len(data) - 1
    while float(data[i][0]) > finish:
        i -= 1
    data = data[:i]
    
    # want n data points
    l = int(len(data)/600)
    data = [data[i] for i in range(len(data)) if ((i<1000000 and i % (l*2) == 0) or (i>1000000 and i%l==0))]
    
    data = data + last_year
    
    return data
        


def convert(data,dur):
    if dur == "1M":
        return convert_to_1M(data)
    elif dur == "1Y":
        return convert_to_1Y(data)
    else:
        return convert_to_all(data)









