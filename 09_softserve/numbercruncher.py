# Icebroken (Tanzeem Hasan and Ivan Gontchar)
# SoftDev
# K06:: "The More You Know About Your Data..."
# 2024 - 09 - 19
# Time spent:

'''
Disco:
QCC:
HOW THIS SCRIPT WORKS
'''

import random
import pprint

def maker():
    returner = "The industry you got is "
    with open("occupations.csv", "r") as file:
        f = file.read()
    arr = f.split("\n")
    #print(arr)
    dict = {}
    total = 0
    for i in range(1, len(arr[1:len(arr)-1])):
        if arr[i][0] == '\"':
            x = arr[i].split("\",")
            #print(arr[i].split("\","))
            #total += int(x[1])
            y = [x[0][1:], float(x[1])]
            total += y[1]
            dict[total] = y
        else:
            x = arr[i].split(",")
            #print(x)
            y = [x[0], float(x[1])]
            total += y[1]
            dict[total] = y
    #pprint.pp(dict)
    x = random.random() * 99.8;
    choice = [];
    temp = list(dict.keys())
    for i in temp:
        if(i > x):
            choice = dict.get(i)
            break
    #print(x)
    #print(choice)
    returner += choice[0]
    returner += ", that takes up " + str(choice[1]) + "% of the job market.</b><br><br>"
    for i in arr:
        returner += i + "<br>"
    #print("The industry you got is " + choice[0] + ", that takes up", choice[1], "% of the job market.")
    return returner

maker()
