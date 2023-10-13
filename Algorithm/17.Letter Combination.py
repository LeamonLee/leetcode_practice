'''
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digi2CharTable ={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8": "tuv",
            "9":"wxyz"
        }

        # digits="234"
        def backtracking(i, combinedLetters):
            print(f"i:{i}, combinedLetters:{combinedLetters}")
            if len(combinedLetters) == len(digits):     # 如果combinedLetters長度等於digits="23"
                res.append(combinedLetters)
                return
            chars = digi2CharTable[digits[i]]    # 2 -> "abc", 3-> "def", 4->"ghi"
            for char in chars:  # a -> b -> c
                backtracking(i+1, combinedLetters+char)
            

        if digits:        
            backtracking(0, '')
        
        return res