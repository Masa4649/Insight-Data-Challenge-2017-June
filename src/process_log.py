#!/usr/bin/env python
# coding: UTF-8
# developed on Python 3.5.2, on Scientific Linux 7.2
#
# Insight Data Coding Challenge
#        
# __author__ = "Masahiro Notani"
# __date__ = "Wed July  5 08:10:37 2017"
#

#def xxxx():
# import time
# return
#
def log_parser2_old(name):
    import re
    from operator import itemgetter, attrgetter

    # Event Loop: Begin
    with open(name,'r') as fr:
        line = fr.readline()
        nline=0
        while line:
            print(nline,line)
            line = fr.readline()
            nline+=1

    #
    #line = fr.readline()
    #nline+=1 
    # Event Loop: End

    return name

def log_parser_test1_string(name):
    import json

    json_str = '''
    {
        "test":"json",
        "test2":"json2"
    }
    '''
    json_dict = json.loads(json_str)
    print('json_dict:{}'.format(type(json_dict)))

    return name

def log_parser_test2_file(name):
    import json

    with open('../sample_dataset/test.json','r') as fr:
    ##with open(name,'r') as fr:
        json_dict = json.load(fr)
        print('json_dict:{}'.format(type(json_dict)))
        print('book1 info:{}'.format(json_dict['book1']))
        print('book3 info:{}'.format(json_dict['book3']['page']))
        for x in json_dict:
            book_page = json_dict[x]['page']

            if(book_page >= 500):
                print('{0}:{1}'.format(x, json_dict[x]))
                
    return name

def log_parser_test3_sample(name):
    import json

    with open('../sample_dataset/stream_log.json','r') as fr:
    ##with open(name,'r') as fr:
        json_str = fr.readline()
        json_dict = json.loads(json_str)
        print('json_dict:{}'.format(type(json_dict)))
        print('Info 1:{}'.format(json_dict['event_type']))
        print('Info 2:{}'.format(json_dict['timestamp']))
        print('Info 3:{}'.format(json_dict['id']))
        print('Info 4:{}'.format(json_dict['amount']))
        amount = json_dict['amount']
        print(' amount = ',amount)
   
    return name

def log_parser(name):
    import json #https://docs.python.jp/3/library/json.html

    #D: the number of degrees that defines a user's social network.
    
    #T: the number of consecutive purchases made by a user's social network (not including the user's own purchases)

    with open('../sample_dataset/stream_log.json','r') as fr:
    ##with open(name,'r') as fr:
        json_str = fr.readline()
        json_dict = json.loads(json_str)
        print('json_dict:{}'.format(type(json_dict)))
        print('Info 1:{}'.format(json_dict['event_type']))
        print('Info 2:{}'.format(json_dict['timestamp']))
        print('Info 3:{}'.format(json_dict['id']))
        print('Info 4:{}'.format(json_dict['amount']))
        amount = json_dict['amount']
        print(' amount = ',amount)
                
    return name


# Main Routine: Begin
import sys

args = sys.argv
argc = len(args)
print(' argc = ',argc,' args = ',args)

if argc<4:
    # for Windows with 
    #fr1='../log_input/batch_log.json'
    #fr2='../log_input/stream_log.json'
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
