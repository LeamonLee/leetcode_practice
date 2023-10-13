'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        看到搜索題目可以往DFS和BFS去做
        這題反向思考: 從太平洋和大西洋開始由低處往高處找(水由高處往低處流，反向思考就是低往高流)
        '''
        ROWS = len(heights)
        COLUMNS = len(heights[0])

        lstPacific = [[False] * COLUMNS for _ in range(ROWS)]
        lstAtlantic = [[False] * COLUMNS for _ in range(ROWS)]
        # visited = set()   # 這題直接用lstPacific或lstAtlantic判斷是否曾經走過就好，不用另外開visited
        res=[]

        def dfs(r,c, pre, lstOcean):
            if r < 0 or c < 0 or \
                r >= ROWS or c >= COLUMNS:
                return
            
            # 代表遍歷過了
            if lstOcean[r][c] == True: return 
            
            # 由於是反向思考，所以要比上一個節點大
            if heights[r][c] < pre: return
            
            # print((r,c))
            # print(lstOcean)
            lstOcean[r][c] = True

            dfs(r-1, c, heights[r][c], lstOcean)
            dfs(r+1, c, heights[r][c], lstOcean)
            dfs(r, c-1, heights[r][c], lstOcean)
            dfs(r, c+1, heights[r][c], lstOcean)


        # Iterate First and last Column，因為緊靠大西洋和太平洋，代表一定可以流入海洋
        for r in range(ROWS):
            dfs(r, 0, float("-inf"), lstPacific)
            dfs(r, COLUMNS-1, float("-inf"), lstAtlantic)
        
        # Iterate First and last Row，因為緊靠大西洋和太平洋，代表一定可以流入海洋
        for c in range(COLUMNS):
            dfs(0, c, float("-inf"), lstPacific)
            dfs(ROWS-1, c, float("-inf"), lstAtlantic)
       
        # 最後看有哪些點既可以流到太平洋，也可以流到大西洋
        for r in range(ROWS):
            for c in range(COLUMNS):
                # print(f"lstPacific[{r}][{c}]: {lstPacific[r][c]}, lstAtlantic[{r}][{c}]: {lstAtlantic[r][c]}")
                
                if lstPacific[r][c] and lstAtlantic[r][c]:
                    res.append([r,c])
        
        return res