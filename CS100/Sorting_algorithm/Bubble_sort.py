nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))

def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

def bubble_sort_unoptimized(arr):
    iteration_count = 0
    for el in arr:

        # N-1 times comparison 
        for index in range(len(arr) - 1):
            iteration_count += 1
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)

    print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))
# Big O runtime = N(N-1) = O(N^2)

def bubble_sort(arr):
    iteration_count = 0
    for i in range(len(arr)):
        # Iterate through unplaced elements
        for idx in range(len(arr) - i - 1):
            iteration_count += 1
            if arr[idx] > arr[idx + 1]:
                # replacement for swap function
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        
    print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))
# Big O runtime = (N-1) + (N-2) + (N-3) + ... + 2 + 1 
# Big O runtime = N(N-1) / 2 = O(N^2)


## Testing
bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)
print("POST SORT: {0}".format(nums))