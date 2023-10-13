'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order, 
return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # if not maxtrix or not k: return 
        heap=[]
        ROWS = len(matrix)
        COLS = len(matrix[0])

        '''
        先把第一個Column都放進priority queue
        '''
        for r in range(ROWS):
            heapq.heappush(heap, (matrix[r][0], r, 0))
        
        while heap and k > 0:
            curr = heapq.heappop(heap)
            k-=1

            r=curr[1]
            c=curr[2]
            if k==0:
                return matrix[r][c]

            # 第一個拿出來一定是最小的，因此要找第k小的，就在同一個row往右邊繼續找。
            # 要注意如果找到最右邊的了的話，要做+1判斷，否則會過界(out of index)
            if c+1 >= COLS: continue
            heapq.heappush(heap, (matrix[r][c+1], r, c+1))

