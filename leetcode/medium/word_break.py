# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if("".join(wordDict) == s):
            return True
        if (len("".join(wordDict)) > len(s)):
            return False
        #initialize a dictionary
        d = {}
        #iterate through the wordDict
        for word in wordDict:
            if word not in s:
                return False
            #if word is in the s add it to the dictionary
            if word in s:
                #if the word is not in the dictionary, add it
                if word not in d:
                    d[word] = 1
                #if the word is in the dictionary, increment its value by 1
                else:
                    d[word] += 1

        #iterate through the dictionary
        for key, value in d.items():
            if value != 1:
                return False
        
        return True
            
print(Solution().wordBreak("applepenapple", ["apple","pen"]))