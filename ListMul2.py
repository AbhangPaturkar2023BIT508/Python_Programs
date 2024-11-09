# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
    
        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = rev = self.reverse(head)
        cr = 0
        while rev:
            ans = rev.val * 2 + cr
            rev.val = ans % 10
            cr = ans // 10
            rev = rev.next

        head = self.reverse(tmp)
        if cr:
            newNode = ListNode(cr, head)
            head = newNode
        return head
            
