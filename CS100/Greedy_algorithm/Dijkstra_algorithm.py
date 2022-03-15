from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }


def dijkstras(graph, start):
    distances = {}
    
    # Set the initial status
    for vertex in graph:
        # All vertices to be infinity
        distances[vertex] = inf
    # Distance to start is Zero
    distances[start] = 0
    vertices_to_explore = [(0, start)]
  
    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)

        # Iterate through neighbor vertices
        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight
            # Checking the new_distance and original distance(inf or distance) 
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                # Adding linked neighbors from the original neighbor
                heappush(vertices_to_explore, (new_distance, neighbor))
        
    return distances

## Testing
distances_from_d = dijkstras(graph, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))
