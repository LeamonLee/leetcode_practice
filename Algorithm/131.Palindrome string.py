'''
Given a string s, partition s such that every substring of the partition is a 
palindrome. Return all possible palindrome partitioning of s.


Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        partition=[]

        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            
            '''
            aab
            a -> a -> b 
            aa -> b
            '''
            for j in range(i, len(s)):
                subString = s[i:j+1]
                print(f"subString:{subString}")
                if self.isPalinDrome(subString):
                    print(f"subString:{subString} True")
                    partition.append(subString)
                    dfs(j+1)
                    partition.pop()
        
        dfs(0)
        return res
    
    def isPalinDrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            
            l+=1
            r-=1
        return True