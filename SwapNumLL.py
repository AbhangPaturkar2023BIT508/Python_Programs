# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lswap = rswap = head
        for i in range(1, k):
            lswap = lswap.next

        tmp = lswap.next

        while tmp:
            tmp = tmp.next
            rswap = rswap.next

        lswap.val, rswap.val = rswap.val, lswap.val

        return head