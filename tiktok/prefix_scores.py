'''
For an array arr of n integers, in the ith operation, 
the ith element of the the array gets incremented by the current max value of the array
the score of the arry is defined as the sum of elements of the final array after performing n operations
Given arr, report an array of n integers, where the ith integer denotes the score of the prefix array that consists
of the first i elements of the given array.
As the answes can be large, report it modulo 10^9 +7
Example: 
Suppose n = 3 and arr = 1,2,3
After the first operation, prefix = [1] result arr =[2], so score = 2
After the second operation,prefix = [1, 2] result arr = [3,5] so score = 8
After the third operation, prefix =[1,2,3] arr = [4,6,9] so score = 19
The final array is [2,8,19] 
'''

def getPrefixScores(arr):
    # Write your code here
    n = arr[0]
    prefix = [0] * n
    result = [0] * n

    for i in range(1,n):
        prefix[i] = arr[i]
        current = arr[:i+1]
        current_sum = sum(current) + max(current) * (n - i - 1)
        result[i] = current_sum
        print (current_sum)

    return result

    
