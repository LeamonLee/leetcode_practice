'''
Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        '''
        這種旋轉題都是左半邊的最小值比右半邊的最大值還要大，例如下面這樣
        5,6,7

             1,2,3,4

        解題思路: 用right和mid做比較，如果mid比right大，說明mid目前在左半邊，所以要把left指針換成mid現在位置
        '''
        while l+1<r:
            mid = (l+r)//2          # 這題這兩種求mid的寫法都可以
            # mid = l + (r-l)//2    # 這題這兩種求mid的寫法都可以
            if nums[mid] > nums[r]:
                l=mid
            else:
                r=mid
        
        if nums[l] < nums[r]:
            return nums[l]
        else:
            return nums[r]