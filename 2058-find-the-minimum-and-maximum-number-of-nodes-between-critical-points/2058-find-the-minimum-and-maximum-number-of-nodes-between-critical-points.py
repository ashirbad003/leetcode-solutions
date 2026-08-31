# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first_idx = -1
        last_idx = -1
        min_dist = float('inf')
        
        prev = head
        curr = head.next
        idx = 1
        
        while curr.next:
            nxt = curr.next
            is_critical = (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val)
            
            if is_critical:
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - last_idx)
                last_idx = idx
            
            prev = curr
            curr = nxt
            idx += 1
        
        if first_idx == -1 or first_idx == last_idx:
            return [-1, -1]
        
        max_dist = last_idx - first_idx
        return [min_dist, max_dist]