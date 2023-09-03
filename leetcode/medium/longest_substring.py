# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialize a dictionary to keep track of the last seen index of each character
        last_seen = {}
        #initialize a variable to keep track of the start index of the current substring
        start = 0
        #initialize a variable to keep track of the length of the longest substring
        longest = 0
        
        #loop through the string
        for i in range(len(s)):
            #get the current character
            char = s[i]
            #check if the current character is in the dictionary
            if char in last_seen:
                #if the current character is in the dictionary, update the start index to the maximum of the current start index and the last seen index of the current character
                start = max(start, last_seen[char] + 1)
            #update the last seen index of the current character to the current index
            last_seen[char] = i
            #update the longest substring length to the maximum of the current longest substring length and the difference between the current index and the start index plus 1
            longest = max(longest, i - start + 1)
        #return the longest substring length
        return longest

#sliding window approach
#call function
print(Solution().lengthOfLongestSubstring("dvdf"))