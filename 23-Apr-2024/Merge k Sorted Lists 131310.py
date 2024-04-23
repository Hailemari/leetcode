# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current_node = dummy

        min_heap = []
        for idx, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst.val, idx, lst))
        
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current_node.next = node
            current_node = current_node.next
        
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
            
        return dummy.next
