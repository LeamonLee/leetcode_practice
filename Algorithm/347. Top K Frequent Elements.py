'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1] 
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        用hashmap紀錄每個character出現的次數
        並初始化一個array(也可以叫bucket)，並append出現次數一樣的character
        '''
        count={}
        freq = [[]for _ in range(len(nums)+1)]

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        for num, c in count.items():
            freq[c].append(num)
        
        res=[]
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res