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
# #>>xaxis,name
# #>>yaxis,name

controlFunctions = {
    "label" : addLabel
}

graphVals = {}
graphLabels = {}

def addLabel(line):
    if len(line) == 3 and line[1].isdigit():
        graphLabels[int(line[1])] = line[2]


def parseData(line):
    if len(line) < 3:
        return
    for x in line:
        if not x.lstrip('-').isdigit():
            return
    line = [int(x) for x in line]
    if line[0] in graphVals:
        graphVals[line[0]].append(line[1:3])
    else:
        graphVals[line[0]] = [line[1:3]]

def parse(line):
    if row[0][0:2] == '#>':
        parseFunc = controlFunctions.get(line[0][2:],parseData)
        parseFunc(line)

process = Popen(["./test2"], stdout=PIPE)
output = process.communicate()[0]
output = [[x.strip() for x in row.split(",")] for row in output.split("\n") if len(row) > 0]
map(parse,output)

for key in graphVals:
    pairs = sorted(graphVals[key], key = itemgetter(0))
    xVals = [pair[0] for pair in pairs]
    yVals = [pair[1] for pair in pairs]
    if key in graphLabels:
        plt.plot(xVals,yVals, label=graphLabels[key])
    else:
        plt.plot(xVals,yVals)
plt.legend(loc=0)

plt.show()
