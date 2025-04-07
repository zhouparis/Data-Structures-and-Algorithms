# Paris Zhou

import copy

def solve_puzzle(board,source,destination):
    
    #Rows and columns of the board
    row = len(board)
    column = len(board[0])

    # Initialize the bfs_queue in the format of storing the current location and path from source, in a tuple with directions from source to current location 
    bfs_queue = []
    bfs_queue.append([source,[source],""]) 

    # Array that tracks cells traversed of the puzzle
    visited = []
    
    # Intialize a list to help with traversal 
    directions = [[0,-1,'L'],[0,1,'R'],[-1,0,'U'],[1,0,'D']]
    
    # Traverse while queue is not empty
    while len(bfs_queue)>0: 
        grid = bfs_queue.pop(0)
        (x,y) = grid[0]
        index = grid[1]
        direction = grid[2]

        # Mark our current position as traversed
        visited.append((x,y)) 

        # Return if we have reached the destination
        if((x,y) == destination):
            return (index,direction)
        
        # From our directions, traverse to unvisited neighbors
        for dx,dy,d in directions:
            
            new_x = dx+x
            new_y = dy+y
          
             # Rule out coordinates that are out of bounds of puzzle, previously traversed, or marked as impassable
            if new_x<0 or new_x>=row or new_y<0 or new_y >=column:
                continue
            if (new_x,new_y) in visited:
                continue 
            if board[new_x][new_y]=='#':
                continue

            #Deep copy of index to keep track of our path
            newIndex = copy.copy(index) 
            
            #Append where we are now to the path for this node
            newIndex.append((new_x,new_y)) 

            # Queue new values to continue BFS
            bfs_queue.append([(new_x,new_y),newIndex,direction+d]) 
    
    # If traversal finishes without exiting by finding the destination then it is
    return None
