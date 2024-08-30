# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        position = 1  
        direction = 1 
        
        for _ in range(time):
            position += direction
            
            if position == n:  
                direction = -1
            elif position == 1:
                direction = 1
        
        return position
