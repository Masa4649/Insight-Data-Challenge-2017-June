#!/usr/bin/env python
# coding: UTF-8
# developed on Python 3.5.2, on Scientific Linux 7.2 / Windows 10
#
# Insight Data Coding Challenge
#        
# __author__ = "Masahiro Notani"
# __date__ = "Wed July  5 08:10:37 2017"
#

#== Standard Library ==
#import math as mt
from math import log,pi,sin,cos,sqrt
import numpy as np
#import scipy as sc
##from scipy import linalg
##from scipy import spatial
##import scipy.spatial.distance
import pandas as pd
import matplotlib.pyplot as plt
##import pylab

def log_parser(name1,name2,name3):
    import json #https://docs.python.jp/3/library/json.html
    
    # arrays
    num_purchase = [0] * 10000 # N times purchace by Nth customer
    sum_purchase = [0] * 10000 # sum of price bought by Nth customer
    mat_purchase = np.zeros([10000, 50]) # history of purchase (N, M)
    #social_net = [0] * 10000 * 10000
    #D: the number of degrees that defines a user's social network.
    D=2
    #T: the number of consecutive purchases made by a user's social network (not including the user's own purchases)
    T=40
    fw = open(name3,'w')
    print('*** open file 1: ',name1)
    with open(name1,'r') as fr:
        json_str = fr.readline()
        json_dict = json.loads(json_str)
        #print('json_dict:{}'.format(type(json_dict)))
        print('Info 1:{}'.format(json_dict['D']))
        print('Info 2:{}'.format(json_dict['T']))
        D = int(json_dict['D'])
        T = int(json_dict['T'])
        nline=0
        json_str = fr.readline()
        while json_str:
            #json_str = fr.readline()
            json_dict = json.loads(json_str)
            if json_dict['event_type']=='unfriend':
                #print('unfriend')
                n1 = int(json_dict['id1'])
                n2 = int(json_dict['id2'])
                #pass
            elif json_dict['event_type']=='befriend':
                #print('befriend')
                n1 = int(json_dict['id1'])
                n2 = int(json_dict['id2'])
                #pass
            elif json_dict['event_type']=='purchase':
                #print('purchase')
                n = int(json_dict['id'])
                m = num_purchase[n]
                if m < T:
                    num_purchase[n] +=1
                    sum_purchase[n] += float(json_dict['amount'])
                    mat_purchase[n][m] = float(json_dict['amount'])
                    x = mat_purchase.sum(axis=1)
                    #y = mat_purchase[n,0:m].mean()
                    #z = mat_purchase.std(axis=1)
                    #print(x[n]/float(num_purchase[n]))
                    sum1=0.0
                    sum2=0.0
                    for i in range(m+1):
                        sum1 += float(mat_purchase[n][i])

                    ave = sum1 / float(num_purchase[n])
                    for i in range(m+1):
                        xi = float(mat_purchase[n][i] - ave)
                        sum2 += xi * xi
                        
                    sgm = sqrt(sum2 / float(num_purchase[n]))
                    #print(x[n]/float(num_purchase[n]),ave,sgm)
                    #if m > 7:
                    #    print(n,num_purchase[n],ave,sgm)
                    #
                    if m > 4:
                        if float(json_dict['amount']) > (ave + 3 * sgm):
                            #print("abnormal",n,num_purchase[n],ave,sgm,json_dict['amount'])
                            obj = {"event_type":"purchase", "timestamp":json_dict['timestamp'], "id":json_dict['id'], "amount": json_dict['amount'], "mean": ave, "sd": sgm }
                            json_str = json.dumps(obj)
                            #print(json_str)
                            #print(json.dumps(obj, indent=2))
                            #print(json.dumps(obj))
                            fw.write(json_str)
                            fw.write('\n')
                            #obj = {"event_type":"purchase", "timestamp":"2017-06-13 11:33:02", "id": "2", "amount": "1601.83", "mean": "29.10", "sd": "21.46"}
                else:
                    #for i in range(T):
                    #    print(mat_purchase[n][i])
                    pass
            else:
                print('*************** unknown **********************')
                exit()
            #
            json_str = fr.readline()
            nline +=1


    print('*** open file 2: ',name2)
    with open(name2,'r') as fr:
        nline=0
        json_str = fr.readline()
        while json_str:
            #json_str = fr.readline()
            json_dict = json.loads(json_str)
            if json_dict['event_type']=='unfriend':
                #print('unfriend')
                n1 = int(json_dict['id1'])
                n2 = int(json_dict['id2'])
                #pass
            elif json_dict['event_type']=='befriend':
                #print('befriend')
                n1 = int(json_dict['id1'])
                n2 = int(json_dict['id2'])
                #pass
            elif json_dict['event_type']=='purchase':
                #print('purchase')
                n = int(json_dict['id'])
                m = num_purchase[n]
                if m < T:
                    num_purchase[n] +=1
                    sum_purchase[n] += float(json_dict['amount'])
                    mat_purchase[n][m] = float(json_dict['amount'])
                    x = mat_purchase.sum(axis=1)
                    #y = mat_purchase[n,0:m].mean()
                    #z = mat_purchase.std(axis=1)
                    #print(x[n]/float(num_purchase[n]))
                    sum1=0.0
                    sum2=0.0
                    for i in range(m+1):
                        sum1 += float(mat_purchase[n][i])

                    ave = sum1 / float(num_purchase[n])
                    for i in range(m+1):
                        xi = float(mat_purchase[n][i] - ave)
                        sum2 += xi * xi
                        
                    sgm = sqrt(sum2 / float(num_purchase[n]))
                    #print(x[n]/float(num_purchase[n]),ave,sgm)
                    #if m > 7:
                    #    print(n,num_purchase[n],ave,sgm)
                    #
                    if m > 4:
                        if float(json_dict['amount']) > (ave + 3 * sgm):
                            #print("abnormal",n,num_purchase[n],ave,sgm,json_dict['amount'])
                            obj = {"event_type":"purchase", "timestamp":json_dict['timestamp'], "id":json_dict['id'], "amount": json_dict['amount'], "mean": ave, "sd": sgm }
                            json_str = json.dumps(obj)
                            #print(json_str)
                            #print(json.dumps(obj, indent=2))
                            #print(json.dumps(obj))
                            fw.write(json_str)
                            fw.write('\n')
                            #obj = {"event_type":"purchase", "timestamp":"2017-06-13 11:33:02", "id": "2", "amount": "1601.83", "mean": "29.10", "sd": "21.46"}
                else:
                    #for i in range(T):
                    #    print(mat_purchase[n][i])
                    pass
            else:
                print('*************** unknown **********************')
                exit()
            #
            json_str = fr.readline()
            nline +=1
            
    #
    fw.close()
    return name3


# Main Routine: Begin
import sys

args = sys.argv
argc = len(args)
print(' argc = ',argc,' args = ',args)

if argc<4:
    # for Windows with 
    #fr1='../log_input/batch_log.json'
    #fr2='../log_input/stream_log.json'
    #fw1='../log_output/flagged_purchases_s.json'
    #
    fr1='../sample_dataset/batch_log.json'
    fr2='../sample_dataset/stream_log.json'
    fw1='../log_output/flagged_purchases.json'
else:
    # for Linux with run.sh
    fr1=args[2] # batch_log.json
    fr2=args[3] # stream_log.json
    fw1=args[4] # flagged_purchase.json

log_parser(fr1,fr2,fw1)

input("Hit any key to End.") #=== stopper for Python on Windows ===#
# sys.exit()
# Main Routine: End
