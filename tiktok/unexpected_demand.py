'''
A widget manfacturer has the following unexpected demand:
They would like to satisfy as many customers as possible.
Given the number of widgets available and a list of customer orders, what is the maximum number of orders that can be fulfilled?
order: array of integers representing customer orders
k : integer representing the number of widgets in stock
'''

def filledOrders(order, k):
    # Write your code here
    order.sort()
    count = 0
    for i in range(len(order)):
        if order[i] <= k:
            k -= order[i]
            count += 1
    return count
