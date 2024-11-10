# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.li = []
        while head:
            self.li.append(head.val)
            head = head.next
        

    def getRandom(self) -> int:
        return self.li[random.randrange(len(self.li))]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()