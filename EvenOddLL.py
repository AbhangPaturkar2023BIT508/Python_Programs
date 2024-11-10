# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        oddL = evenL = None
        curOdd = oddL
        curEven = evenL
        isOddInd = True

        while head:
            tmp = head
            head = head.next
            tmp.next = None
            if isOddInd:
                if oddL:
                    curOdd.next = tmp
                    curOdd = curOdd.next
                else:
                    oddL = curOdd = tmp
            else:
                if evenL:
                    curEven.next = tmp
                    curEven = curEven.next
                else:
                    evenL = curEven = tmp
            isOddInd = not isOddInd

        curOdd.next = evenL

        return oddL