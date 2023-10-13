'''
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        '''
        這題題目已經先給定一個由小到大排序好的array，所以直接使用二分搜尋法，
        找到中間值後當作root根節點，接著左半邊當左子樹，右半邊當右子樹，不斷recursion。
        使用dfs recursion的方式，不斷找到array中間的數值
        '''

        def dfs(start, end):
            if start > end: return None         # 注意是start>end
            mid = (start+end) // 2

            root = TreeNode(val=nums[mid])
            root.left = dfs(start, mid-1)
            root.right = dfs(mid+1, end)

            return root
        
        result = dfs(0, len(nums)-1)
        # print(f"result:{result}")
        return result