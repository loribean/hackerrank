#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def printFizzBuzz(n):
    # Write your code here

    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0 and n % 5 != 0:
        print('Fizz')
    elif n % 3 != 0 and n % 5 == 0:
        print('Buzz')
    else:
        print(n)


def fizzBuzz(n):
    # Write your code here

    for i in range(1, n+1):
        printFizzBuzz(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
