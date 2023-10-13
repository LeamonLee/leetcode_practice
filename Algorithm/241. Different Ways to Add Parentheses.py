'''
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.
The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def divideNConquer(inputs):
            results=[]
            for i in range(len(inputs)):
                c = inputs[i]
                
                if c in ('+', '-', '*'):
                    lefts = divideNConquer(inputs[:i])
                    rights = divideNConquer(inputs[i+1:])

                    for l in lefts:
                        for r in rights:
                            if c == '+':
                                results.append(l + r)
                            elif c == '-':
                                results.append(l - r)
                            elif c == '*':
                                results.append(l * r)
                    
            if not results:
                return [int(inputs)]

            return results


        res = divideNConquer(expression)
        return res