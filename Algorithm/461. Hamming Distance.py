class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y
        res=0

        while result > 0:
            res+=1
            result = result & (result-1)
        
        return res