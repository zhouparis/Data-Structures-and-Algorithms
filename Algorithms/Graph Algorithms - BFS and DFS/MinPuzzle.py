def minEffort(puzzle):
    # Initialize the number of rows and columns
    m = len(puzzle)
    n = len(puzzle[0])
    
    # Initialize a queue, start from the origin which takes no effort to get to
    queue = [(0, 0, 0)]
    
    # Create a dictionary to track minimum effort required to reach each point
    # Initialize the origin's minimum effort to 0
    min_effort = {(0, 0): 0}
    
    # add a list of neighboring directions
    neighbor = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # Use a BFS traversal
    while queue:
        # Pop from the queue to begin traversal
        x, y, effort = queue.pop(0)
        
        # Check if the current coordinate is the destination, return the minimum effort to reach this point if we are at the destination
        if x == m-1 and y == n-1:
            return min_effort[(x, y)]
        
        # Assuming we are not yet at the destination
        # Check neighbooring points and add them if unvisited
        for dx, dy in neighbor:
            nx: int = int(x)+int(dx)
            ny: int = int(y)+int(dy)

            # Ensure neighbors are within the bounds of the puzzle
            if (0 <= nx) and (nx < m) and (0 <= ny) and (ny < n):
                # Update neighbor point's min effort
                
                new_effort = max(effort, abs(puzzle[nx][ny]-puzzle[x][y]))
                # Check if neighboring point is unvisited, or if the updated effort is less than the effort it takes to reach the orignal point
                if (nx, ny) not in min_effort or new_effort < min_effort[(nx, ny)]:
                    # Add the neighbor to the min effort dictionary and to the queue, including its effort
                    min_effort[(nx, ny)] = new_effort
                    queue.append((nx, ny, new_effort))
    
    # Returning implies the whole puzzle was traversed 
    return -1