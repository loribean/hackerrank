#Given a set of hotels and its guest reviews,
#sort hotels based on a list of words specified by a user
#The criteria to sort the hotels should be as follows:
#how many times the words specified by the user is mentioned in the hotel reviews.


# Input:
# The first line contains a space-separated set of words which we want to find mentions in the hotel reviews.
# The second line contains one integer M, which is the number of reviews.
# This is followed by M+M lines, which alternates an hotel ID and a review belonging to that hotel.
# Output:
# A list of hotel IDs sorted, in descending order, by how many mentions they have of the words specified in the input.

from re import sub
from collections import defaultdict, Counter

def hotel_reviews():
    # Make all words lowercase
    words = set(input().lower().split())
    num_reviews = int(input())

    hotel_reviews = defaultdict(int)
    for _ in range(num_reviews):
        hotel_id = int(input())
        review = input().lower()
        review = sub(r'[^\w\s]', '', review)
        review_words = review.split()
        review_word_counts = Counter(review_words)
        for word in words:
            hotel_reviews[hotel_id] += review_word_counts[word]

    # Sort hotel reviews by number of mentions in descending order, if same number of mentions, sort by hotel id
    sorted_hotel_reviews = sorted(hotel_reviews.items(), key=lambda x: (-x[1], x[0]))

    return [hotel[0] for hotel in sorted_hotel_reviews]

print(hotel_reviews())
