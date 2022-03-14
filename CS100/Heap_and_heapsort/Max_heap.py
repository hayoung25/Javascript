class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    ## methods for getting parent and child indices
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1
  
    ## Adding new element in the max_heap list
    def add(self, element):
        self.count += 1
        print("Adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()
    
    ## re_arrange the order by swaping parents and child elements
    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        
        # Loop until parent is exist
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            
            # if parent value is smaller than child, swap!
            if parent < child:
                print("swapping {0} with {1}".format(parent, child))
                
                # Swapping
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            
            # Checking next parent 
            idx = self.parent_idx(idx)
    
        print("Heap Restored {0}".format(self.heap_list))
