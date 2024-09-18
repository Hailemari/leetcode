# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        dir = 1
        pos = 1  
        
        for _ in range(time):
            pos = pos + dir
            
            if pos == 1:  
                dir = 1
            elif pos == n:
                dir = -1
        
        return pos
