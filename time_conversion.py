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
    # get the last two characters
    last_two = s[-2:]
    hour = int(s[:2])

    # get the first two characters

    if last_two == 'AM':
        if hour == 12:
            hour = '00'
        else:
            hour = s[:2]
    else:
        if hour != 12:
            hour +=  12

    return str(hour) + s[2:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
