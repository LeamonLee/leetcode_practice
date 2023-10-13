'''
Example1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ''' 使用雙指針，紀錄的是index '''
        l=0
        r=len(height)-1
        maxArea = 0

        while l<r:
            minHeight = min(height[l], height[r])
            maxArea = max(maxArea, minHeight*(r-l))
            
            # 看哪一邊比較小，就那一邊移動，例如: 左邊9, 右邊7
            # 這時先用右邊7的算面積，但有可能右邊下一個是8，這時候用8算比用原本的7算面積還大，
            # 且又小於左邊的9
            # 因為算面積要取左右兩邊較小的
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        
        return maxArea