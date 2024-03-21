'''
Description
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example1
Input:  s = "++++"
Output: true
Explanation:
The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Example2
Input: s = "+++++"
Output: false 
Explanation:
The starting player can not win 
"+++--" --> "+----"
"++--+" --> "----+"
'''

class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    def can_win(self, s: str) -> bool:
        # write your code here
        for i in range(1, len(s)):
            if s[i]=='+' and s[i-1]=='+':
                temp=list(s)
                temp[i]='-'
                temp[i-1]='-'
                if not self.can_win("".join(temp)):
                    return True
        
        return False