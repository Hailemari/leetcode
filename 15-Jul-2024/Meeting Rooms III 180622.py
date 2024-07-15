# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
    
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        ongoing_meetings = []
        
        room_usage_count = [0] * n
        
        for start, end in meetings:
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                end_time, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
                room_usage_count[room] += 1
            else:
                end_time, room = heapq.heappop(ongoing_meetings)
                new_end_time = end_time + (end - start)
                heapq.heappush(ongoing_meetings, (new_end_time, room))
                room_usage_count[room] += 1
        
        max_meetings = max(room_usage_count)
        for room in range(n):
            if room_usage_count[room] == max_meetings:
                return room
