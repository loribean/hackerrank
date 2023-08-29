# We are string consisting of N letter
# we want to find the alphabetically largest letter 
# that occurs in both lower and uppercase in S, or decide there is no such letter

# ie: in string "abCB", we return B
# in string "a", we return "NO"


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    letters = list(set(S))
    max_capital = None
    
    for letter in letters:
        if letter.isupper() and letter.lower() in letters:
            if max_capital is None or letter > max_capital:
                max_capital = letter
    
    if max_capital is None:
        return "NO"
    else:
        return max_capital

    
