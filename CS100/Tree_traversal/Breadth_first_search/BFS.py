from collections import deque

## Breadth-first search function
def bfs(root_node, goal_value):

    # initialize frontier queue
    path_queue = deque()

    # Add root path to the frontier
    initial_path = [root_node]
    path_queue.appendleft(initial_path)
  
    # Search loop that continues as long as
    # There are paths in the frontier
    while path_queue:
        # Get the next path and node 
        # Then output node value
        current_path = path_queue.pop()
        current_node = current_path[-1]
        print(f"Searching node with value: {current_node.value}")

    # Check if the goal node is found
        if current_node.value == goal_value:
            return current_path

    # Add paths to children to the  frontier
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)

    # return an empty path if goal not found
    return None