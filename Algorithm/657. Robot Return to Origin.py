class Solution:
    def judgeCircle(self, moves: str) -> bool:
        row = 0
        col = 0

        for c in moves:
            if c=="U": col-=1
            elif c=="D": col+=1
            elif c=="L": row-=1
            elif c=="R": row+=1
        
        return col == 0 and row == 0