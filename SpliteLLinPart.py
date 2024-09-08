# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        curr = head
        size = 0
        while curr != None:
            size += 1
            curr = curr.next
        
        curr = head
        splitSize = size // k
        reaminingPart = size % k

        for i in range(k):
            headNewPart = None
            tail = None

            currSize = splitSize
            if reaminingPart > 0:
                reaminingPart -= 1
                currSize += 1

            for j in range(currSize):
                newNode = ListNode(curr.val)
                if headNewPart == None:
                    headNewPart = newNode
                else:
                    tail.next = newNode
                
                tail = newNode
                curr = curr.next
            ans.append(headNewPart)

        return ans

        