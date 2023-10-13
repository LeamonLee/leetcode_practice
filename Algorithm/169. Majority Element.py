'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        主要元素(Majority Element)的定義就是數量超過整個array長度的一半，
        使用Boore Majority vote algorithm
        可以將主要元素(Ex:1)看成一個整體，其餘不等於主要元素的(Ex:2,3,4,5,6)看成一個整體，
        由於主要元素超過整個array的一半，因此主要元素的count會比其他不等於主要元素的整體的count多
        '''
        currMaxCountNum = 0
        count = 0

        for num in nums:
            if count == 0:
                currMaxCountNum=num
            
            if num == currMaxCountNum:
                count+=1
            else:
                count-=1
        
        return currMaxCountNum