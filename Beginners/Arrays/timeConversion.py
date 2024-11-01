#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    data = s.split(":")
    if data[-1][-2:] == "AM" and data[0] == "12":
            return "00:{}:{}".format(data[1],data[2][:-2])
    elif data[-1][-2:] == "PM" and data[0] != "12":
            return "{}:{}:{}".format(int(data[0]) + 12, data[1], data[2][:-2])
    return "{}:{}:{}".format(data[0],data[1],data[2][:-2])

def assert_equals(x,y):  
    if x == y:
          print("pass")
    else:
          print("failed")

if __name__ == '__main__':

    s = "07:05:45PM"
    actual = timeConversion(s)
    expected = "19:05:45"
    assert_equals(actual,expected)

    s = "12:01:00PM"
    actual = timeConversion(s)
    expected = "12:01:00"
    assert_equals(actual,expected)

    s = "12:01:00AM"
    actual = timeConversion(s)
    expected = "00:01:00"
    assert_equals(actual,expected)