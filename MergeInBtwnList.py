# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1

        for _ in range(a-1):
            list1 = list1.next

        l1end = list1

        for _ in range((b-a)+2):
            list1 = list1.next

        l1end.next = list2
        
        while l1end.next:
            l1end = l1end.next
        
        l1end.next = list1

        return head
        