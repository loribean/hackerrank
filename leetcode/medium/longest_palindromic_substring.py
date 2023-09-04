# Given a string s, return the longest 
# palindromic substring in s
 
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            #single character palindrome center
            current = self.get_longest_palindrome_from(s, i, i)
            if len(current) > len(longest):
                longest = current
            #two character palindrome center
            current = self.get_longest_palindrome_from(s, i, i + 1)
            if len(current) > len(longest):
                longest = current
        return longest
    
    def get_longest_palindrome_from(self, string, left, right):
         #loop while the left index is greater than or equal to 0 and the right index is less than the length of the string and the characters at the left and right indices are the same
        while left >=0 and right < len(string) and string[left] == string[right]:
            left -= 1 #decrement the left index
            right += 1 #INCREMENT the right index
        return string[left + 1:right]
#call function
print(Solution().longestPalindrome("cbbd"))