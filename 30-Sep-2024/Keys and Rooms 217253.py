# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()

        while queue:
            node = queue.popleft()

            visited.add(node)

            for nbr in rooms[node]:
                if nbr not in visited:
                    queue.append(nbr)

        n = len(rooms)
        for i in range(n):
            if i not in visited:
                return False

        return True