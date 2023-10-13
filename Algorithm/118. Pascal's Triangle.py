'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        temp = []
        '''
        這一層可以發現一個規律就是每一層的左右兩邊都有1
        '''
        for i in range(numRows):
            # temp = [1,2,1]
            temp.insert(0, 1)   # 因為第一個element一定都是1開頭
            # temp = [1,1,2,1] => [1, 1+2, 2+1, 1] => [1,3,3,1]
            
            # 從第二個遍歷到倒數第二個，然後前後相加
            for j in range(1, len(temp)-1):
                temp[j] = temp[j]+temp[j+1]
            
            res.append(temp.copy())
        
        return res