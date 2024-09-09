# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = []
        for _ in range(m):
            ans.append([-1] * n)
        top = left = 0
        right, bottom = n, m

        while head:
            for i in range(left, right):
                if not head:
                    break
                ans[top][i] = head.val
                head = head.next
            top+=1
            for i in range(top, bottom):
                if not head:
                    break
                ans[i][right-1] = head.val
                head = head.next
            right-=1
            for i in range(right-1, left-1, -1):
                if not head:
                    break
                ans[bottom-1][i] = head.val
                head = head.next
            bottom-=1
            for i in range(bottom-1, top-1, -1):
                if not head:
                    break
                ans[i][left] = head.val
                head = head.next
            left+=1
        
        return ans

        