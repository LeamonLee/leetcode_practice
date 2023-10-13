'''
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) < 2: return [-1, -1]

        '''
        用two pointer
        '''

        l = 0
        r = len(numbers)-1
        while l < r:
            total = numbers[l]+numbers[r]
            if total == target:
                return [l+1,r+1]    # 因為題目要求index從1開始
            elif total > target:
                r-=1
            else:
                l+=1
        
        return [-1,-1]