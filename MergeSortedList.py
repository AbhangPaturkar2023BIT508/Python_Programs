# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        srtMergeNode = ListNode()
        tmp = srtMergeNode

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next

        if list1 == None:
            tmp.next = list2
        if list2 == None:
            tmp.next = list1

        return srtMergeNode.next