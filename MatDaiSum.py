class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)-1
        i = 0
        sum = 0
        for m in mat:
            if i == n-i:
                sum += m[i]
            else:
                sum += m[i]
                sum += m[n-i]
            i+=1
        return sum
        