class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max = 0
        ind = 0
        for i in range(len(mat)):
            count = 0
            for j in mat[i]:
                if j == 1:
                    count+=1
            if max < count:
                max = count
                ind = i
        return [ind, max]