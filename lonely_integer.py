#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    # create a dictionary
    d = {}

    # loop through the array
    for item in a:
        # if the item is not in the dictionary
        if item not in d:
            # add it to the dictionary
            d[item] = 1
        else:
            # otherwise increment the value
            d[item] += 1

    # get the key with the value of 1

    for key, value in d.items():
        if value == 1:
            return key
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
