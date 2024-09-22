# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    prev = curr = front = None

    def recursive_reverse(self, prev : Optional[ListNode], curr : Optional[ListNode]) -> Optional[ListNode]:
        if curr is None:
            return prev
        
        self.front = curr.next
        curr.next = prev
        return self.recursive_reverse(curr, self.front)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.curr = head
        return self.recursive_reverse(self.prev, self.curr)
    
    
