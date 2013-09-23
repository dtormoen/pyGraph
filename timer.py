#! /usr/bin/python
import matplotlib
import numpy as np
import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import os
import time
import sys
from operator import itemgetter
from subprocess import Popen, PIPE

graphVals = {}
graphLines = {}

lastUpdate = time.time() - 1

def redrawGraph():
    global lastUpdate
    newUpdate = time.time()
    if (newUpdate - lastUpdate) > 1.0:
        lastUpdate = newUpdate
        return True
    return False

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
    if redrawGraph():
        ax = plt.gca()
        ax.relim()
        ax.autoscale_view()
        plt.legend(loc=0)
        plt.draw()

def parseData(label, data):
    if label in graphVals:
        graphVals[label].append(map(float,data))
    else:
        graphVals[label] = [map(float,data)]
    drawKey(label)

def parse(line):
    line = [val.strip() for val in line.split(",")]
    if len(line[0]) < 3:
        return
    if line[0][0:2] == '#>' or len(line[0] <3):
        label = line[0][2:].strip()
        if label == 'xAxis':
            plt.xlabel(line[1])
        elif label == 'yAxis':
            plt.ylabel(line[1])
        elif label == 'Title' or label =='title':
            plt.suptitle(line[1])
        data = []
        for x in line[1:]: 
            try:
                data.append(float(x))
            except ValueError:
                return
        parseData(label,data)

def main(argv):
    plt.ion()
    plt.plot([],[])

    if len(argv) < 2:
        print "Please select a program to analyze"
        return

    # process = Popen(["tests/closestPair/leastDistance.py"], stdout=PIPE)
    process = Popen([argv[1]], stdout=PIPE)
    for line in iter(process.stdout.readline, ""):
        line = line.rstrip("\n")
        parse(line)
        print line

    plt.show()

    print "Press q to exit"
    userInput = ""

    while userInput != 'q':
        userInput = raw_input(": ")

main(sys.argv)
