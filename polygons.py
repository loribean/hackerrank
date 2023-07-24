# Identity whether four sides (given by 4 integers) can form a square, rectangle, or neither

# Input
# Each line of input descirbes a single polygon, and contains four space seperated integers S1, S2, S3 and S4
# Each represents the length of a side of the polygon

# Output
# a single line which contains 3 space seperated integers, representing the number of squares, rectangles or polygons with 4 sides

# constraints
# The four integers representing the sides will be such that -2000 <= X <- 2000

# Sample Input
# 36 30 36 30
# 15 15 15 15
# 46 96 90 100
# 86 86 86 86
# 100 200 100 200
# -100 200 -100 200

# Sample Output
# 2 2 2

# Explanation
# There are 2 squares, 2 rectangles and 2 other polygons possible with the given set of sides

def shape_finder():

    squares = 0
    rectangles = 0
    others = 0

    while True:
        try:
            sides = input().split()
            if len(sides) != 4:
                break
            unique_sides = set(sides)
            if len(unique_sides) == 1:
                squares += 1
            # check if unique sides is 2 and both sides are either negaitve or positive
            elif len(unique_sides) == 2:
                unique_list = [int(x) for x in list(unique_sides)]
                if unique_list[0] < 0 and unique_list[1] < 0 or unique_list[0] > 0 and unique_list[1] > 0:
                    rectangles += 1
                else:
                    others += 1
            else:
                others += 1
        except EOFError:
            break

    print(squares, rectangles, others)


shape_finder()
