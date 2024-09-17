# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos = 1  
        dir = 1
        
        for _ in range(time):
            pos += dir
            
            if pos == n:  
                dir = -1
            elif pos == 1:
                dir = 1
        
        return pos
