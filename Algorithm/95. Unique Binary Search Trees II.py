'''
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def helper(start, end):
            temp = []

            if start > end:
                temp.append(None)   # 這裡是關鍵
                return temp
            
            # i代表以i當做root節點
            for i in range(start, end+1):
                lstLeft = helper(start, i-1)
                lstRight = helper(i+1, end)

                # 假設左子樹有M種排列組合，右子樹有N種組合，
                # 每個左子樹的一種組合，都可以對應右子樹的N種組合
                # 因此要跑nested for loop
                for left in lstLeft:
                    for right in lstRight:
                        root = TreeNode(val=i)
                        root.left = left
                        root.right = right

                        temp.append(root)
            
            return temp

        return helper(1,n)