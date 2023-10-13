'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        temp = []
        for i in range(rowIndex+1): # 因為index從0開始，如果rowIndex=0，至少要跑一次迴圈
            temp.insert(0, 1)

            for j in range(1, len(temp)-1):
                temp[j] = temp[j]+temp[j+1]
        
        return temp