#given a list of numbers as input eg:
#25626 25757 24367 24267 16 100 2 7277

#output a delta encoding for the sequence. In delta encoding, the first element is
# is reproduced as is. Each subsequent element is represented as the numeric difference
# from the element before it. Eg: for the sequence above, the delta encoding would be:
#25626 131 -1390 -100 -24251 84 -98 7275

#however, a difference value may be too large to fit in a single signed byte. ie -127 <= x <= 127
#in this case, we use an escape token, printing it.

#this will denote that the value following the escape token is a full fou-byte difference value, rather than a one-byte difference value 
# we will declare -128 as the escape token

# following the smae sequence above, the delta encoding would be:
# 25626 -128 131 -128 -1390 -100 -128 -24251 84 -98 -128 7275

def delta_encoding():
    # read in input
    input_list = [int(x) for x in input().split()]

    # initialize output list
    output_list = []

    # append first element of input list to output list
    output_list.append(input_list[0])

    # iterate through input list
    for i in range(1, len(input_list)):
        # calculate difference between current element and previous element
        difference = input_list[i] - input_list[i-1]

        # if difference is between -127 and 127, append difference to output list
        if -127 <= difference <= 127:
            output_list.append(difference)
        # otherwise, append -128 to output list, then append difference to output list
        else:
            output_list.append(-128)
            output_list.append(difference)

    # print output list
    print(output_list)


delta_encoding()
