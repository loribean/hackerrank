# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

from heapq import heappop, heapify


class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:

        #we can use a heap to solve this problem
        #a heap is a binary tree where the value of each node is greater than or equal to the value of its children
        #we can use a min heap to find the kth largest element
        #we can iterate through the array and add each element to the heap
        #if the size of the heap is greater than k, we can remove the smallest element from the heap

        #initialize a heap
        heapify(nums)
        #heaps are sorted in ascending order, so we can get the kth largest element by doing len(nums) - k
        for _ in range(len(nums) - k):
            heappop(nums)
        #return the kth largest element
        return heappop(nums)

#run the function
print(Solution().findKthLargest([3,2,1,5,6,4], 2))


