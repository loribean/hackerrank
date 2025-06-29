class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()

        return not stack  # If stack is empty, all parentheses are matched

print(Solution().isValid("([[W]])"))