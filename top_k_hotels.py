#!/bin/python3

import math
import os
import random
import re
import sys
from re import sub
from collections import defaultdict, Counter


#
# Complete the 'awardTopKHotels' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING positiveKeywords
#  2. STRING negativeKeywords
#  3. INTEGER_ARRAY hotelIds
#  4. STRING_ARRAY reviews
#  5. INTEGER k
#

def awardTopKHotels(positiveKeywords, negativeKeywords, hotelIds, reviews, k):
    # Write your code here
    positive_array = set(positiveKeywords.lower().split())
    negative_array = set(negativeKeywords.lower().split())

    hotel_reviews = defaultdict(int)

    for i in range(len(reviews)):
        hotel_id = hotelIds[i]
        review = reviews[i].lower()

        review = sub(r'[^\w\s]','', review)
        review_words = review.split()
        score = 0
        
        for word in review_words:
            if word in positive_array:
                score += 3
            elif word in negative_array:
                score -= 1
        
        hotel_reviews[hotel_id] += score

    sorted_hotel_reviews = sorted(hotel_reviews.items(), key=lambda x:(-x[1], x[0]))
    hotel_numbers = min(k, len(hotel_reviews.keys()))

    return [sorted_hotel_reviews[i][0] for i in range(hotel_numbers)]











if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    positiveKeywords = input()

    negativeKeywords = input()

    hotelIds_count = int(input().strip())

    hotelIds = []

    for _ in range(hotelIds_count):
        hotelIds_item = int(input().strip())
        hotelIds.append(hotelIds_item)

    reviews_count = int(input().strip())

    reviews = []

    for _ in range(reviews_count):
        reviews_item = input()
        reviews.append(reviews_item)

    k = int(input().strip())

    result = awardTopKHotels(
        positiveKeywords, negativeKeywords, hotelIds, reviews, k)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
