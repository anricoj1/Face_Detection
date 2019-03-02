import numpy as np
import pandas as pd
import math

def main(print_data):
    colnames = ['x', 'y']
    filename = 'files.txt'
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line !='':
                data = pd.read_csv(line, names=colnames, sep=' ')
                print_data(data, line)

def print_data(data, line):
    print(line)
    print(' ')
    print(data)
    print(' ')
    print('------------------------------------------')
    print(' ')
    print('Eye Length: ', eye_length(data))
    print('Eye Distance: ', eye_distance(data))
    print('Nose ratio: ', nose_ratio(data))
    print('Lip Size: ', lip_size(data))
    print('Lip Length ', lip_length(data))
    print('Eye-brow length: ', brow_length(data))
    print('Aggressive Ratio: ', aggress(data))

def n_features(data):
    eye_length()
    eye_distance()
    nose_ratio()
    lip_size()
    lip_length()
    brow_length()
    aggress()

def eye_length(data):
    x1 = data.x[7]
    y1 = data.y[7]
    x2 = data.x[12]
    y2 = data.y[12]
    v1 = math.pow(x2-x1, 2)
    v2 = math.pow(y2-y1, 2)
    value = math.sqrt(v1 + v2)
    return ('{0:.3g}'.format(value))

def eye_distance(data):
    x1 = data.x[7]
    y1 = data.y[7]
    x2 = data.x[12]
    y2 = data.y[12]
    dist = (x1-y1) / (x2-y2)
    return ('{0:.3g}'.format(dist))

def nose_ratio(data):
    p1 = data.x[15] - data.x[14]
    p2 = data.y[15] - data.y[14]
    p3 = data.x[20] - data.x[19]
    p4 = data.y[20] - data.y[19]
    v1 = math.pow(p1, 2) + math.pow(p2, 2)
    v2 = math.pow(p3, 2) + math.pow(p4, 2)
    n = math.sqrt(v1) / math.sqrt(v2)
    return ('{0:.3g}'.format(n))

def lip_size(data):
    p1 = data.x[2] - data.x[1]
    p2 = data.y[2] - data.y[1]
    p3 = data.x[17] - data.x[16]
    p4 = data.y[17] - data.y[16]
    lip = math.sqrt(math.pow(p1, 2) + math.pow(p2, 2)) / math.sqrt(math.pow(p3, 2) + math.pow(p4, 2))
    return ('{0:.3g}'.format(lip))

def lip_length(data):
    p1 = data.x[2] - data.x[1]
    p2 = data.y[2] - data.y[1]
    p3 = data.x[20] - data.x[19]
    p4 = data.y[20] - data.y[19]
    lip_l = math.sqrt(math.pow(p1, 2) + math.pow(p2, 2)) / math.sqrt(math.pow(p3, 2) + math.pow(p4, 2))
    return ('{0:.3g}'.format(lip_l))

def brow_length(data):
    p1 = data.x[4] - data.x[3]
    p2 = data.y[4] - data.y[3]
    p3 = data.x[12] - data.x[7]
    p4 = data.y[12] - data.y[7]
    brow = math.sqrt(math.pow(p1, 2) + math.pow(p2, 2)) / math.sqrt(math.pow(p3, 2) + math.pow(p4, 2))
    return ('{0:.3g}'.format(brow))

def aggress(data):
    p1 = data.x[18] - data.x[9]
    p2 = data.y[18] - data.y[9]
    p3 = data.x[20] - data.x[19]
    p4 = data.y[20] - data.y[19]
    a = math.sqrt(math.pow(p1, 2) + math.pow(p2, 2)) / math.sqrt(math.pow(p3, 2) + math.pow(p4, 2))
    return ('{0:.3g}'.format(a))


# end main program passing print_data
main(print_data)
