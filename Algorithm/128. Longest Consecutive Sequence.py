'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

 
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0 

        '''
        題目給的nums是沒有排序過的
        因為題目要求要O(n)，所以不能排序
        '''

        numSet = set(nums)
        res=1
        for num in nums:
            if num in numSet:   # 使用hashset找是否存在，時間複雜度為1，因為不用遍歷整個array
                numSet.remove(num)
                upperNum = 0
                lowerNum = 0

                ''' 假設從2開始，往上找3,4,5... '''
                while (num+upperNum+1) in numSet:
                    numSet.remove(num+upperNum+1)
                    upperNum+=1
                
                ''' 假設從2開始，往下找1,0... '''
                while (num - lowerNum - 1) in numSet:
                    numSet.remove(num-lowerNum-1)
                    lowerNum+=1
                
                res = max(res, 1+upperNum+lowerNum) # 假設從2開始，除了加上upperNum和lowerNum之外，還要加上自己一個，因此1就是2本身
        
        return res