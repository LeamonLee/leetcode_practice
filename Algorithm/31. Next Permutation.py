'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(arr, l, r):
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
            
            return arr

        '''
        這題只能硬記解法
        1,5,8,4,7,6,5,3,1
          i
            j
        '''

        ''' Step1 從後往前遍歷，找到第一個降序index '''
        i = len(nums)-2                         # 從倒數第二個開始，因為下一行while條件用i和i+1比較
        while i>=0 and nums[i] >= nums[i+1]:    # 是 "大於等於" ，如果只有大於會失敗
            i-=1
        
        if i<0:
            nums.sort()
            return
        
        ''' Step2 從後往前遍歷，找到第一個比nums[i]大的index '''
        j = len(nums) - 1                       # 這邊從最後一個element開始
        while j>=0 and nums[j] <= nums[i]:      # 是 "小於等於" ，如果只有小於會失敗
            j-=1
        
        ''' Step3 Swap '''
        nums[i], nums[j] = nums[j], nums[i]

        ''' Step4 將i以後的數字重新排列 '''
        nums = reverse(nums, i+1, len(nums)-1)
        return 

        
        