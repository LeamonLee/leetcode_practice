'''
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

可以和81題比較
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        這題關鍵在給定的nums不會重複，但81題的nums會有重複的element
        '''
        l=0
        r=len(nums)-1

        while l+1<r:    # 因為要找mid，所以是l+1<r
            mid = l+(r-l)//2
            if nums[mid] == target: return mid

            ''' 先判斷是在上半區還是下半區，用mid和l的大小比較來判斷 '''
            # Ex: 4,5,6,7,  0,1,2
            #     l     mid     r
            if nums[l] <= nums[mid]:    # 說明在左半段
                ''' 接著看target和mid, left的關係 '''
                if target >= nums[l] and target <= nums[mid]:
                    r = mid
                else:
                    l = mid
            
            # Ex: 4,5,6,7,0,  1,2,3
            #     l       mid     r
            else:
                ''' 接著看target和mid, right的關係 '''
                if target >= nums[mid] and target <= nums[r]:
                    l = mid
                else:
                    r = mid
        
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1