# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        visited = set(deadends)
        queue = deque([("0000", 0)])

        while queue:
            combination, turns = queue.popleft()

            if combination == target:
                return turns
            
            visited.add(combination)
            for i in range(4):
                slot = int(combination[i])

                for diff in [-1, 1]:
                    new_slot = (slot + diff) % 10
                    new_combination = combination[:i] + str(new_slot) + combination[i+1:]

                    if new_combination not in visited:
                        visited.add(new_combination)
                        queue.append((new_combination, turns + 1))

        
        return -1


        