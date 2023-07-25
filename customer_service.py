#at booking.com, our customer service is an important contributor to customer satisfaction. During busy times, howerever, there might be more calls to
#customer service than the number of employees can manage. 
# Fortunately we record data on that. We have collected information about the phone calls made to our call centers for the past year

# Given that the number of agents is X. Determine how many more people that we would need to hire
#to make sure that our customers woi;d not have to wait during peak hours ie: dont have more phone calls than customer service agents.

#Input:
# The first line of the input contains the number of agents X
# The second line contains the number of data points N
# The next N lines are whitespaced-sepeated pairs of timestamos 
# The time stamp is integer that represents seconds since epoch
# on the each line, the first number is the start of the call and the second number is the end of the call

#Output 
#single integer representing the number of additional agents that we need to hire
# if currently we have enough agents, output 0

def customer_service():
    number_of_agents = int(input())
    number_of_data_points = int(input())
    calls = []

    for _ in range(number_of_data_points):
        call = input().split()
        calls.append((int(call[0]), int(call[1])))

    # sort calls by start time
    calls.sort(key=lambda x: x[0])

    concurrent_calls = 1
    current_call = calls.pop(0)

    for call in calls:
        if call[0] < current_call[1]:
            concurrent_calls += 1
        else:
            current_call = call
    return max(concurrent_calls - number_of_agents, 0)


print(customer_service())

        


    