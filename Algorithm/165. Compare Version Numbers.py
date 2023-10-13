'''
Return the following:
If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 2:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".

Example 3:
Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1Arr = version1.split('.')
        v2Arr = version2.split('.')

        for i in range(max(len(v1Arr),len(v2Arr))):
            num1 = int(v1Arr[i]) if i < len(v1Arr) else 0
            num2 = int(v2Arr[i]) if i < len(v2Arr) else 0

            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0