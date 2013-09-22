#! /usr/bin/python
import random
import math
import time
import sys

dataPoints = 10000

def makeData(num):
	return [(random.uniform(0,100), random.uniform(0,100)) for x in range(0,num)]

def distance(p1,p2):
	return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def bruteForce(data):
	minDist = -1
	points = [(0,0),(0,0)]

	for i in range(0,len(data)):
		for j in range(i+1,len(data)):
			dist = distance(data[i],data[j])
			if (dist < minDist or minDist == -1):
				minDist = dist
				points[0] = data[i]
				points[1] = data[j]
	return [points[0], points[1], minDist]

def betweenSet(data, median, dist):
	medianx = median
	middleData = [x for x in data if x[0] < medianx + dist and x[0] > medianx - dist]
	p1 = (0,0)
	p2 = (0,0)
	minDist = dist + 1
	for i in range(0, len(middleData)):
		for j in range(i+1, min(len(middleData), i+8)):
			tempDist = distance(middleData[i],middleData[j])
			if tempDist < dist:
				minDist = tempDist
				p1 = middleData[i]
				p2 = middleData[j]
	return [p1, p2, minDist]


def closestPair(data):
	if len(data) < 4:
		return bruteForce(data)
	sortedx = sorted(data, key = lambda p: p[0])
	median = sortedx[int(len(sortedx)/2)][0]
	result1 = closestPair([x for x in data if x[0] <= median])
	result2 = closestPair([x for x in data if x[0] >= median])
	if result1[2] < result2[2]:
		best = result1
	else:
		best = result2
	middleResult = betweenSet(data, median, best[2])

	if (middleResult[2] != -1 and middleResult[2] < best[2]):
		return middleResult
	return best

def algorithm(data):
	sortedy = sorted(data, key = lambda p: p[1])
	return closestPair(sortedy)
	
dataPoints = 0
for x in range(0,2500/10):
	dataPoints +=10
	data = makeData(dataPoints)

	t1 = time.time()
	result1 = bruteForce(data)
	t2 = time.time()
	print "#>BruteForce,", dataPoints, ",", t2-t1
	t3 = time.time()
	result2 = algorithm(data)
	t4 = time.time()
	print "#>ClosestPairAlgorithm,", dataPoints, ",", t4-t3
	sys.stdout.flush() #Needed to make graph update in real time