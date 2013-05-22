#! /usr/bin/python
import matplotlib
import numpy as np
import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import os
from operator import itemgetter
from subprocess import Popen, PIPE

#language:
# #>id,x,y

graphVals = {}

def parseData(label, data):
    if label in graphVals:
        graphVals[label].append(map(int,data))
    else:
        graphVals[label] = [map(int,data)]

def parse(line):
    if len(line) < 3 and len(line[0]) < 3:
        return
    if line[0][0:2] == '#>':
        label = line[0][2:].strip()
        data = []
        for x in line[1:]: 
            try:
                data.append(float(x))
            except ValueError:
                return
        parseData(label,data)

process = Popen(["tests/simpleTest/simpleTest.py"], stdout=PIPE)
output = process.communicate()[0]
output = [[x.strip() for x in row.split(",")] for row in output.split("\n") if len(row) > 0]
print output
map(parse,output)

print graphVals

for key in graphVals:
    pairs = sorted(graphVals[key], key = itemgetter(0))
    xVals = [pair[0] for pair in pairs]
    yVals = [pair[1] for pair in pairs]
    plt.plot(xVals,yVals, label=key)
plt.legend(loc=0)

plt.show()
