'''
Given an integer n, return the number of structurally unique BST's (binary search trees) 
which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1
'''
class Solution:
    def __init__(self):
        self.dp={}
    def numTrees(self, n: int) -> int:
        if n <= 1: return 1 # 這裡要寫小於等於答案才會對，只寫等於會有問題，因為n=1的時候的確只會有1種BST組合
        
        # 用dp紀錄當n等於多少節點數量時，總共會有多少種排列組合的BST
        if n in self.dp:
            return self.dp[n]

        result = 0
        for i in range(n): # n代表有n個根節點的個數，i是左子樹的節點數量
            result += self.numTrees(i) * self.numTrees(n-1-i)   # 左子樹代表有i個節點數量，根節點也算一個節點，總共有n節點，右子樹總共有n-1-i的節點，因此有多少種組合就是左子樹*右子樹的排列組合總數   
        
        self.dp[n] = result
        return result