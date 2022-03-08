from random import randrange, shuffle

"""
Quicksort is a function to sortout a unsorted list by spliting lists by two comparing to the pivot element
One become elements less than pivot element, the other become elements more than pivot element
The split is conducted by swaping elements
    1. It compares each elements in the list from the first element to the end 
    and check if that is greater or lesser than Pivot value.
    2. If it is lesser than pivot than it is swapped with pivot which locates its value left side of the pivot
    3. After looping all elements in the list, the function is repeated on each sub-lists(recursion)
The function is repeated until it hits the base point which is "start >= end"
"""

def quicksort(list, start, end):
    # Base case
    if start >= end:
        return
    print("Running quicksort on {0}".format(list[start: end + 1]))

    # Pivot element
    # select random element to be pivot
    pivot_idx = randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    print("Selected pivot {0}".format(pivot_element))

    # swap random element with last element in sub-lists
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start
  
    for i in range(start, end):
        # we found an element out of place
        if list[i] < pivot_element:
        # swap element to the right-most portion of lesser elements
            print("Swapping {0} with {1}".format(list[i], pivot_element))
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            # tally that we have one more lesser element
            less_than_pointer += 1
            # move pivot element to the right-most portion of lesser elements
            list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
            print("{0} successfully partitioned".format(list[start: end + 1]))

    # recursively sort left and right sub-lists
    quicksort(list, start, less_than_pointer - 1)
    quicksort(list, less_than_pointer + 1, end)


    
## Testing
list = [5,3,1,7,4,6,2,8]
shuffle(list)
print("PRE SORT: ", list)
print(quicksort(list, 0, len(list) -1))
print("POST SORT: ", list)
