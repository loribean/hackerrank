# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.

class Solution:
    def singleNumber(self, nums) -> int:
        #initialize a dictionary
        d = {}
        #iterate through the array
        for num in nums:
            #if the number is not in the dictionary, add it
            if num not in d:
                d[num] = 1
            #if the number is in the dictionary, increment its value by 1
            else:
                d[num] += 1
        #iterate through the dictionary
        for key, value in d.items():
            #if the value is equal to 1, return the key
            if value == 1:
                return key
            
print(Solution().singleNumber([2,2,3,2]))
