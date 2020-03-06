
import math

def avg(data, length, log = False):
    if log:
        data = [math.log(x) for x in data]
    s = sum(data[:length])
    avg = data[:length] + [s/length]
    for i in range(len(data)-length):
        s += data[i+length] 
        s -= data[i]
        avg.append(s/length)
    if log:
        avg = [math.exp(x) for x in avg]
    return avg

def var(data, length, log = False):
    if log:
        data = [math.log(x) for x in data]
    bin_size = int((2**32)/length)
    data = [int(x)//bin_size for x in data]
    init = data[:length]
    cnt = [0 for i in range((2**32)//bin_size+1)]
    for i in init:
        cnt[i]+=1
    unique = sum([1 for x in cnt if x == 1])
    var = [math.exp(1)*100*(unique)/length for x in data[:length]]
    for i in range(len(data)-length):
        cnt[data[i+length]] += 1
        if cnt[data[i+length]] == 1:
            unique += 1 
        if cnt[data[i+length]] == 2:
            unique -= 1 
        cnt[data[i]] -= 1
        if cnt[data[i]] == 1:
            unique += 1 
        if cnt[data[i]] == 0:
            unique -= 1 
        var.append(math.exp(1)*100*(unique)/length)
    return var  
