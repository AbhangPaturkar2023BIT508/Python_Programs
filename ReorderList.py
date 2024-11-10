# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        tmp = head

        while tmp:
            arr.append(tmp)
            tmp = tmp.next

        for i in range(0, len(arr)//2):
            tmp = arr[i].next
            arr[i].next = arr[~i]
            arr[~i].next = tmp
        
        arr[len(arr)//2].next = None

        return head
        