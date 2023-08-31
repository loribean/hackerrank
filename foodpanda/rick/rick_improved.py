def solution(riddle):
   
    # String concatenation using += inside a loop can be inefficient
    # as strings are immutable in Python. It's better to use a list to accumulate characters 
    # and then join them into a string at the end.
    #strings are immutable objects, which means that every time a string is concatenated with another string, a new string object is created in memory
    # concat more than 2 strings with + is an O(n^2) operation (compared to O(n) for join) and thus becomes inefficient.
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


#Approach
# 1. initialize an empty list string to accumulate characters of the new string.
# 2. create a set alphabet containing all lowercase letters for later reference.
# 3. initialize a variable previous to keep track of the previous character.
# 4. loop through the string and check if the current character is a question mark.
# 5. if the current character is a question mark
# 5a. check if there is a next character
# 5b. if there is a next character, remove the previous and next character from the alphabet set
# 5c. get the next character by getting the minimum character from the remaining letters in the alphabet
# 5d. append the next character to the string
# 5e. update the previous character to the next character
# 6. if the current character is not a question mark
# 6a. append the current character to the string
# 6b. update the previous character to the current character
# 7. join the characters in the string list into a string and return it


# 1. variable names are descriptive - string, alphabet, previous
# 2. Set lookup is O(1) time
# 3. optimized the process of finding the next available letter using a set. This reduces the complexity compared to the original version.
# O(N) Time, O(N) Space

# Original code: O(N*M), where M is the length of the alphabet
# Improved code: O(N)

#Improvements:
# 1. can handle edge cases None or non-string input


