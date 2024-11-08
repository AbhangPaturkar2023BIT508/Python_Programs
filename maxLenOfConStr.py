class Solution:
    def maxLength(self, arr: List[str]) -> int:
        lst = []
        lent = 0
        for i in arr:
            if self.isuniq(i):
                lst.append(i)
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                if self.isuniq(lst[i]+lst[j]):
                    lst.append(lst[i]+lst[j])
        
        lst = sorted(lst, key=len)
        lent = len(lst)-1
        
        if len(lst)==0:
            return 0
        else:
            return len(lst[lent])


    def isuniq(self, cher: str) -> bool:

        for i in range(len(cher)):
            if cher[i] in cher[i+1:]:
                return False
        return True