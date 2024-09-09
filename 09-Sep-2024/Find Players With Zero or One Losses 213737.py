# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = defaultdict(int)
        players = set()

        for winner, loser in matches:
            loss[loser] += 1
            players.add(winner)
            players.add(loser)
        
        lose_zero_match = []
        lose_one_match = []
 
        for player in players:
            if loss[player] == 0:
                lose_zero_match.append(player)
            elif loss[player] == 1:
                lose_one_match.append(player)
    
        return [sorted(lose_zero_match), sorted(lose_one_match)]