from random import randrange
from Max_heap import MaxHeap 

## Testing Max_heap
max_heap = MaxHeap()

# populate max_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
  max_heap.add(el)

# test it out, is the maximum number at index 1?
print(max_heap.heap_list)


