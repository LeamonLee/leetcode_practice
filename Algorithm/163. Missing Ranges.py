'''
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example 1
Input:
nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
Output:
["2", "4->49", "51->74", "76->99"]
Explanation:
in range[0,99],the missing range includes:range[2,2],range[4,49],range[51,74] and range[76,99]

Example 2
Input:
nums = [0, 1, 2, 3, 7], lower = 0 and upper = 7
Output:
["4->6"]
Explanation:
in range[0,7],the missing range include range[4,6]
'''

from typing import (
    List,
)

class Solution:
    """
    @param nums: a sorted integer array
    @param lower: An integer
    @param upper: An integer
    @return: a list of its missing ranges
    """
    def find_missing_ranges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # write your code here

        res=[]

        for num in nums:
            if lower == num:
                lower+=1
            elif lower < num:
                if lower+1==num:
                    res.append(str(lower))
                else:
                    res.append(f"{lower}->{num-1}")
                lower=num+1
        
        if lower==upper:
            res.append(str(lower))
        elif lower < upper:
            res.append(f"{lower}->{upper}")
        
        return res