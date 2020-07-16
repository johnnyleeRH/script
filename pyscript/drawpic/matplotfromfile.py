import numpy as np 
from matplotlib import pyplot as plt

namemap = {}
names = []
values = []
if __name__ == '__main__':
    fd = open("/home/lrh/cmpshare/videostructure/ai/build/resultset", "rb")
    while True:
        line = fd.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            break
        tmp = line.split(str.encode(' '))
        namemap[tmp[0]] = tmp[1:]
    for key in namemap.keys():
        names.append(key)
        value = []
        for id in range(0, len(namemap[key])):
            value.append(float(namemap[key][id]))
        values.append(value)
    x = np.arange(0, len(values[0]))
    plt.xlabel("total cnt")
    plt.ylabel("timecost (us)")
    for id in range(0, len(names)):
        if id == 0:
            plt.plot(x, values[id], 'ob', label = names[id].decode(encoding='utf-8'))
        elif id == 1:
            plt.plot(x, values[id], 'or', label = names[id].decode(encoding='utf-8'))
        else:
            plt.plot(x, values[id], 'oy', label = names[id].decode(encoding='utf-8'))
    plt.legend()
    plt.show()