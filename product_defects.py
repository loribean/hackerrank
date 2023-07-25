#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findLargestSquareSize' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY samples as parameter.
#

def findLargestSquareSize(samples):
    # Write your code here
    # create a variable to hold the largest square size
    largest_square_size = 0

    # flood fill algorithm
    # loop through the rows
    for row in range(len(samples)):
        # loop through the columns
        for column in range(len(samples[row])):
            # if the element is 1
            if samples[row][column] == 1:
                # if the element is in the first row or first column
                if row == 0 or column == 0:
                    # set the element to 1
                    samples[row][column] = 1
                # else
                else:
                    # set the element to the minimum of the left, top, and top left element + 1
                    samples[row][column] = min(
                        samples[row][column-1], samples[row-1][column], samples[row-1][column-1]) + 1
                # if the element is larger than the largest square size
                if samples[row][column] > largest_square_size:
                    # set the largest square size to the element
                    largest_square_size = samples[row][column]
            # else
            else:
                # set the element to 0
                samples[row][column] = 0
    # return the largest square size
    return largest_square_size


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    samples_rows = int(input().strip())
    samples_columns = int(input().strip())

    samples = []

    for _ in range(samples_rows):
        samples.append(list(map(int, input().rstrip().split())))

    result = findLargestSquareSize(samples)

    fptr.write(str(result) + '\n')

    fptr.close()
