#!/usr/bin/env python

import time


def getTime():
    while True:
        curr_time = time.ctime()
        time.sleep(1)
        #for length in range(secs):
        #print("Start : %s" % curr_time)
        #time.sleep(1)
        #print("End : %s" % curr_time)

        return curr_time
