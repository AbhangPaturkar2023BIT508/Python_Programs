class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(arr)
        i = 1
        d = {}
        for val in sortedArr:
            if val not in d:
                d[val] = i
                i+=1

        for i in range(len(arr)):
            arr[i] = d[arr[i]]

        return arr
