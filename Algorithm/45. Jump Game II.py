'''
You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and i + j < n

Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currFarthestIdx = 0     # 目前可以跳到最遠的index是多少，會不斷比較更新成最大的
        nextStopIdx = 0         # 下次檢查當前這幾步中可以跳最遠的那一個index，例如一開始在index=0可以跳到2，那就是到index=2的時候檢查從0~2這中間可以跳最遠的index是多少
        
        for idx in range(len(nums)-1):    # <-- len(nums)-1是關鍵，array最後一個item不遍歷。
            currFarthestIdx = max(currFarthestIdx, idx+nums[idx])

            if idx == nextStopIdx:
                jumps+=1
                nextStopIdx = currFarthestIdx
        
        return jumps