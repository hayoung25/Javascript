"""You are given n activities with their start and finish times.
Select the maximum number of activities that can be performed by a single person, 
assuming that a person can only work on a single activity at a time.

Example 1 : Consider the following 3 activities sorted by
by finish time.
     start[]  =  {10, 12, 20};
     finish[] =  {20, 25, 30};
A person can perform at most two activities. The
maximum set of activities that can be executed
is {0, 2} [ These are indexes in start[] and
finish[] ]""" 

# Creating start finish array 
start = [10, 12, 20]
finish = [20, 25, 30]

# Create event array which contains start time and finish time
events = []


for time in start:
     event = []
     event.append(time)

for time in finish:
     event.append(time)

print(event)


#   length = len(input_array)
#   doubled_array = [0] * length
#   for i in range(length):
#     doubled_array[i] = input_array[i] * 2
#   return doubled_array




