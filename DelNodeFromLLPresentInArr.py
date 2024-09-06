# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        nums = set(nums)

        while curr != None:
            if curr.val in nums:
                if prev is None:
                    curr = head = curr.next
                else:
                    prev.next = curr = curr.next
            else:
                prev = curr
                curr = curr.next
        
        return head
        