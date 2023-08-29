# given a riddle, return a copy of the string with all the question marks replaces by lowercase
# letters from a to z, such that the same letters don't occur next to each other

# ie: "ab?ac?" -> "abcaca" or "abxacv"


def solution(riddle):

    #loop through string
    #if we see a question mark, replace it with the next letter in the alphabet

    string = ""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    previous = ""

    for i in range(len(riddle)):
        current = riddle[i]
        if current == "?":
            next_letter = ""
            if i < len(riddle) - 1:
                next_letter = riddle[i+1]
        
            for letter in alphabet:
                if letter != previous and letter != next_letter:
                    string += letter
                    break
            previous = string[-1]
        else:
            string += current
            previous = current

    
    return string


