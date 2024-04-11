# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()

        while queue:
            node = queue.popleft()

            visited.add(node)

            for neighbor in rooms[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        
        for i in range(len(rooms)):
            if i not in visited:
                return False

        return True