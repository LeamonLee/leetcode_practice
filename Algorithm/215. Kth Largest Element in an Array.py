'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ''' Priority queue solution '''
        nums = [-elem for elem in nums] # 因為python的priority queue是用min heap實作，為了要將最大的
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)


        ''' quick sort solution '''
        if not nums: return 0

        def quickSort(left, right):
            pivot = left
            l = left+1
            r = right

            while l <= r:
                if nums[l] < nums[pivot] and nums[r] > nums[pivot]:
                    nums[l], nums[r] = nums[r], nums[l]
                    l+=1
                    r-=1
                    print(f"case1 quickSort nums:{nums}, l:{l}, r:{r}")    
                if nums[l] >= nums[pivot]:
                    l+=1
                    print(f"case2 quickSort nums:{nums}, l:{l}, r:{r}")
                if nums[r] <= nums[pivot]:
                    r-=1
                    print(f"case3 quickSort nums:{nums}, l:{l}, r:{r}")
                print("---------------------------------------")

            nums[pivot], nums[r] = nums[r], nums[pivot]
            return r

        left = 0
        right = len(nums) - 1

        while True:
            pivot = quickSort(left, right)  # 回傳的pivot index是array理面的第幾大
            print(f"nums: {nums}, left:{left}, right:{right}, pivot:{pivot}")

            # pivot是array的index，所以要+1才會變成第幾大，舉例index 0是第一大，index 1是第二大
            if pivot + 1 == k:
                return nums[pivot]
            elif pivot+1 > k:   # 代表k在array左邊
                right = pivot - 1
            else:               # 代表k在array右邊
                left = pivot + 1