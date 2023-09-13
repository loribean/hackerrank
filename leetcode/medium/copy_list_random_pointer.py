# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        # create a copy of each node and insert it between the original node and the next node
        cur = head
        while cur:
            copy = Node(cur.val, cur.next, None)
            cur.next = copy
            cur = copy.next
        # set the random pointer for each copy node
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # separate the original list and the copy list
        cur = head
        copy_head = head.next
        copy_cur = copy_head
        while cur:
            cur.next = cur.next.next
            if copy_cur.next:
                copy_cur.next = copy_cur.next.next
            cur = cur.next
            copy_cur = copy_cur.next
        return copy_head
    
print(Solution().copyRandomList([[3,None],[3,0],[3,None]]))


        