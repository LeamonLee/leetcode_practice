'''
Description
You are given a m x n 2D grid initialized with these three possible values.
-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF

Example1:
Input:
[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

Output:
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Explanation:
the 2D grid is:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

the answer is:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

Example2:
Input:
[[0,-1],[2147483647,2147483647]]

Output:
[[0,-1],[1,2]]
'''

from typing import (
    List,
)
from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here

        queue = deque()
        visited = set()
        ROWS = len(rooms)
        COLS = len(rooms[0])
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c]==0:
                    queue.appendleft((r,c))
                    visited.add((r,c))
        
        # dirs = {(-1,0),(1,0),(0,-1),(0,1)}
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        curr = 0
        while queue:
            qLen = len(queue)
            for _ in range(qLen):
                room = queue.pop()
                r = room[0]
                c = room[1]
                rooms[r][c] = min(rooms[r][c], curr)

                for _dir in dirs:
                    
                    new_r = r + _dir[0]
                    new_c = c + _dir[1]
                    
                    if new_r<0 or new_r>=ROWS or \
                        new_c<0 or new_c>=COLS or \
                        (new_r, new_c) in visited:
                        continue
                    if rooms[new_r][new_c]!=2147483647:
                        continue
                    
                    queue.appendleft((new_r,new_c))
                    visited.add((new_r,new_c))

            curr+=1



