class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        total=0

        mapTotal = {
            0:1
        }

        '''
        nums=[1,2,3]
        k=3
        mapTotal = {
            0:1,
            1:1,    <-- index 0
            3:1,    <-- index 1
            6:1     <-- 代表走到index 2時，array總和是6，如果將總和-k=3，且在mapTotal找到key，則該key的value代表之前有多少種方法 可以累加到k
        }
        '''

        for i in range(len(nums)):
            total+=nums[i]
            if (total-k) in mapTotal:
                res+=mapTotal[total-k]
            
            mapTotal[total] = mapTotal.get(total, 0) + 1
        
        return res
        