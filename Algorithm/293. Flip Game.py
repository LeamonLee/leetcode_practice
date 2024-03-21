'''
Description
You are playing the following Flip Game with your friend: Given a string that contains only two characters: + and -, you can flip two consecutive "++" into "--", you can only flip one time. Please find all strings that can be obtained after one flip.

Write a program to find all possible states of the string after one valid move.

Example1
Input:  s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]

Example2
Input: s = "---+++-+++-+"
Output: 
[
	"---+++-+---+",
	"---+++---+-+",
	"---+---+++-+",
	"-----+-+++-+"
]
'''

from typing import (
    List,
)

class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
             we will sort your return value in output
    """
    def generate_possible_next_moves(self, s: str) -> List[str]:
        # write your code here

        res=[]
        for i in range(1,len(s)):
            if s[i]=='+' and s[i-1]=='+':
                temp = list(s)
                temp[i]='-'
                temp[i-1]='-'
                res.append("".join(temp))
        
        return res