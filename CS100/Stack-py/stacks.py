from node import Node

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit
    
    # stacking on top of head
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the pizza stack!".format(value))
        else:
            print("No room for {}!".format(value))
    
    # Take an item from the top (LIFO)
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Delivering " + item_to_remove.get_value())
        return item_to_remove.get_value()
        print("All out of pizza.")

    # Check out value of the top of the stack
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
            print("Nothing to see here!")

    # Checking whether the stack is overflowing
    def has_space(self):
        return self.limit > self.size

    # Checking if the stack is currently empty
    def is_empty(self):
        return self.size == 0