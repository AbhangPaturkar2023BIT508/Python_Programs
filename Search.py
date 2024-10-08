class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            pro = arr[i]*2
            start, end = 0, len(arr)-1

            while start<=end:
                mid = (start + end)//2
                if arr[mid] == pro and mid != i:
                    return True
                elif arr[mid] < pro:
                    start = mid+1
                else:
                    end = mid-1
    
        return False