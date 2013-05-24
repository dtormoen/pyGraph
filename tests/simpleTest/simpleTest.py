#! /usr/bin/python
import time
import sys

for x in range(0,10):
    print "#>1,",x,",",x
    print "#>2,",x,",",x*2
    sys.stdout.flush()
    time.sleep(1)
