def solution(riddle):
   
    # String concatenation using += inside a loop can be inefficient
    # as strings are immutable in Python. It's better to use a list to accumulate characters 
    # and then join them into a string at the end.
    string = []
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    previous = ""

    for i in range(len(riddle)):
        current = riddle[i]
        
        if current == "?":
            next_letter = riddle[i + 1] if i < len(riddle) - 1 else ""
            #we avoid using a for loop here by using a set
            # we remove the previous and next letter from the alphabet
            available_letters = alphabet - {previous, next_letter}
            next_char = min(available_letters)
            string.append(next_char)
            previous = next_char
        else:
            string.append(current)
            previous = current
    
    return "".join(string)