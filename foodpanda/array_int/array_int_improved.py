# We are string consisting of N letter
# we want to find the alphabetically largest letter 
# that occurs in both lower and uppercase in S, or decide there is no such letter

# ie: in string "abCB", we return B
# in string "a", we return "NO"


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def get_max_char(S):

    #letters = list(set(S))
    #we can directly use a set and loop through it
    #O(N) Time, O(N) Space
    unique_letters = set(S)
    max_capital = None
    
    #O(N) Time
    for letter in  unique_letters:
        #this is O(1) Time now that we are using a set
        if letter.isupper() and letter.lower() in  unique_letters:
            if max_capital is None or letter > max_capital:
                max_capital = letter
    
    if max_capital is None:
        return "NO"
    else:
        return max_capital
    #Total Time Complexity: O(N)
    