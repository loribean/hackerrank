from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix
        min_length = min(len(s) for s in strs)
        for i in range(min_length):
            current_char = strs[0][i]
            for s in strs:
                if s[i] != current_char:
                    return prefix
            prefix += current_char

        return prefix
    
print(Solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"