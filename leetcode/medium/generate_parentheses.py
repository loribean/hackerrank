# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8


class Solution:
    def generateParenthesis(self, n: int):
        result = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n: #exit condition, if the length of the string is equal to 2 * n (n pairs of parentheses)
                result.append(S)
                return
            if left < n: #if the number of left parentheses is less than n, add a left parenthesis
                backtrack(S + '(', left + 1, right)
            if right < left: #if the number of right parentheses is less than the number of left parentheses, add a right parenthesis
                backtrack(S + ')', left, right + 1)
        
        backtrack()
        return result
    
print(Solution().generateParenthesis(3))