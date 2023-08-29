#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json


#
# Complete the 'getCapitalCity' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING country as parameter.
# API URL: https://jsonmock.hackerrank.com/api/countries?name=<country>
#

def getCapitalCity(country):
    # Write your code here
    # call the API
    url = "https://jsonmock.hackerrank.com/api/countries?name=" + country
    response = requests.get(url)
    data = response.json()['data']

    # if data is empty array/ length is 0 return -1, else return capital
    if len(data) == 0 or data == None or data == []:
        return '-1'
    else:
        return data[0]['capital']


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    country = input()

    result = getCapitalCity(country)

    fptr.write(result + '\n')

    fptr.close()
