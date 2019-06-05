import numpy as np
import pandas as pd
import math

import scipy
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics

# loop through files.txt
def main(print_data, K_Neighbors):
    colnames = ['x', 'y']
    filename = 'files.txt'
    files = 'test.txt'
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line !='':
                data = pd.read_csv(line, names=colnames, sep=' ')
                print_data(data, line)
                K_Neighbors(data)

# compare data to find K-Nearst Term
def K_Neighbors(data):
    x = pd.DataFrame.from_dict([ [eye_length(data), eye_distance(data), nose_ratio(data), lip_size(data), lip_length(data), brow_length(data), aggress(data)] ],
                                orient='index', columns = ['eye_len', 'eye_dist', 'nose', 'lip_size', 'lip_len', 'brow_length', 'agressive']    )


    print(x.columns)
    X_prime = x[0,1,2,3,4,5,6]
    y = x[1]
    X = preprocessing.scale(X_prime)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .50, random_state = 17)

    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train, y_train)
    print(clf)

    y_expect = n_features
    y_pred = clf.predict(test)

    print(metrics.classifaction_report(y_expect, y_pred))

# print data
def print_data(data, line):
    print(' ')
    print(' ')
    print('------------------------------------------')
    print(' ')
    print('--------Training Set [Feature Extraction]---------')
    print(' ')
    print('Eye Length: ', eye_length(data))
    print('Eye Distance: ', eye_distance(data))
    print('Nose ratio: ', nose_ratio(data))
    print('Lip Size: ', lip_size(data))
    print('Lip Length ', lip_length(data))
    print('Eye-brow length: ', brow_length(data))
    print('Aggressive Ratio: ', aggress(data))
    print(' ')
    print('---------Testing Set [Feature Extraction]-----------')
    print(' ')


# define functions for ratios
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

main(print_data, K_Neighbors)
