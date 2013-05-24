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
graphLines = {}

def drawKey(key):
    pairs = sorted(graphVals[key], key = itemgetter(0))
    xVals = [pair[0] for pair in pairs]
    yVals = [pair[1] for pair in pairs]
    if key in graphLines:
        graphLines[key].set_xdata(xVals)
        graphLines[key].set_ydata(yVals)
    else:
        line, = plt.plot(xVals,yVals, label=key)
        graphLines[key] = line
    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()
    plt.legend(loc=0)
    plt.draw()

def parseData(label, data):
    if label in graphVals:
        graphVals[label].append(map(int,data))
    else:
        graphVals[label] = [map(int,data)]
    drawKey(label)

def parse(line):
    line = [val.strip() for val in line.split(",")]
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

plt.ion()
plt.plot([],[])

process = Popen(["tests/simpleTest/simpleTest.py"], stdout=PIPE)
for line in iter(process.stdout.readline, ""):
    line = line.rstrip("\n")
    parse(line)
    print line

plt.show()

print "Press q to exit"
userInput = ""

while userInput != 'q':
    userInput = raw_input(": ")
