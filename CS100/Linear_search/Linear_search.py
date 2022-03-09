'''
<Time complexity>
Best Case: Θ(1)
Worst Case: O(n)
Average Case: The algorithm makes N/2 comparisons: n/2 => O(n)

'''

number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33

# Linear_search function
def linear_search(search_list, target_value):

    # Compare each element and target_element
    for idx in range(len(search_list)):

        # If there is same element as target-element, return the index
        if search_list[idx] == target_value:
            return idx
            
    # Or raise error        
    raise ValueError("{0} not in list".format(target_value))


## Testing
try:
    result = linear_search(number_list, target_number)
    print(result)
except ValueError as error_message:
    print("{0}".format(error_message))