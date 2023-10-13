'''
Description
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.


Example 1:
Input:
map = 
[
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4]
end = [3,2]
Output:
false

Example 2:
Input:
map = 
[[0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4]
end = [4,4]
Output:
true
'''

from typing import (
    List,
)

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # write your code here

        visited=set()
        dirs={(-1, 0), (1, 0), (0,-1), (0,1)}
        
        def helper(curr):
            if curr[0] == destination[0] and curr[1] == destination[1]: return True
            if (curr[0], curr[1]) in visited: return False

            visited.add((curr[0], curr[1]))

            for _dir in dirs:
                
                r = curr[0]
                c = curr[1]
                while r+_dir[0] >= 0 and r+_dir[0] < len(maze) and \
                        c+_dir[1] >= 0 and c+_dir[1] < len(maze[0]) and \
                        maze[r+_dir[0]][c+_dir[1]] != 1:
                # while r >= 0 and r < len(maze) and \
                #         c >= 0 and c < len(maze[0]) and \
                #         maze[r][c] != 1:
                    r+=_dir[0]
                    c+=_dir[1]
                
                # if (r, c) in visited: continue
                if helper([r, c]):
                    return True
            
            return False

        return helper(start)
