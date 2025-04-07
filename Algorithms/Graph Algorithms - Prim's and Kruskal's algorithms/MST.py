# Paris Zhou
import heapq

def Prims(G):
    """Prims(G) implements Prim's Algorithm for finding the minimum spanning tree (MST) of a graph.
    Outputs a list of tuples where each tuple represents an edge of the MST. Utilizes min heap"""

    result = []
    visited = {}

    current_node = G[0]
    current_node_index = 0
    visited[current_node_index] = 0
    node_heap = []
    
    while len(visited) < len(G):

        # Initialize starting node, mark it as visited

        # Check every edge of the current vertex
        
        
        for index in range(len(current_node)):

            # Check only vertices with valid edges
            if current_node[index] != 0:

                # Check only unvisited vertices
                if visited.get(index) == 0:
                    continue
                else:
                    # Add vertex to the heapqueue
                    heapq.heappush(node_heap, (current_node[index], index, current_node_index))

        min_edge = heapq.heappop(node_heap)
        
        while visited.get(min_edge[1]) == 0:
            min_edge = heapq.heappop(node_heap)
        result.append((min_edge[2], min_edge[1], min_edge[0]))
        current_node = G[min_edge[1]]
        current_node_index = min_edge[1]
        visited[current_node_index] = 0

        
    return result



if __name__ == "__main__":
    input = [
        [0, 8, 5, 0, 0, 0, 0],
        [8, 0, 10, 2, 18, 0, 0],
        [5, 10, 0, 3, 0, 16, 0],
        [0, 2, 3, 0, 12, 30, 14],
        [0, 18, 0, 12, 0, 0, 4],
        [0, 0, 16, 30, 0, 0, 26],
        [0, 0, 0, 14, 4, 26, 0]
    ]
    print(Prims(input))