# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next :
            return head

        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        curr = head
        front = head.next

        while front:
            gcdVal = gcd(curr.val, front.val)
            newNode = ListNode(gcdVal)
            
            newNode.next = front
            curr.next = newNode

            curr = front
            front = front.next
        
        return head

        