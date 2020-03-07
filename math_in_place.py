
import math

def avg(source, length, log = False):
    if log:
        source = [x for x in source if x[1]]
        data = [math.log(x[1]) for x in source]
    else:
        data = [x[1] for x in source]
    s = sum(data[:length])
    avg = data[:length]
    for i in range(len(data)-length):
        s += data[i+length] 
        s -= data[i]
        avg.append(s/length)
    if log:
        avg = [math.exp(x) for x in avg]
    out = [[source[i][0],avg[i]] for i in range(len(avg))]
    return out

def var(source, length, log = False):
    data = [x[1] for x in source]
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
    out = [[source[i][0],var[i]] for i in range(len(var))]
    return out
