#  You are given an List of positions of cars as to where they are parked. You are also given an integer K. 
#  The cars needs to be covered with a roof. You have to find the minimum length of roof that takes to cover K cars.
 
#  Input : 12,6,5,2      K = 3
 
#  Explanation :  There are two possible roofs that can cover K cars. One that covers the car in 2,5,6 parking spots and
#  another roof which covers 5,6,12 parking spots. The length of these two roofs are 5 and 8 respectively. Return 5
#  since that's the roof with minimum length that covers K cars.

#  Output : 5

def min_length_to_cover_roof(cars, k):
    cars.sort()
    # set min_length to the length of the entire list of cars
    # we need to +1 because 5-5 is 0, but we need to cover 1 car
    # it is inclusive, so we need to add 1
    min_length = cars[-1] - cars[0] + 1
    for i in range(len(cars) - k + 1):
        # update min_length to the length of the current k cars
        min_length = min(min_length, cars[i + k - 1] - cars[i] + 1)
    return min_length


print(min_length_to_cover_roof([12, 6, 5, 2], 3)) 
# return 5