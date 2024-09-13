class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] = arr[i] ^ arr[i-1]
        ans = [0]*len(queries)
        for i in range(0,len(queries)):
            if queries[i][0] is 0:
                ans[i] = arr[queries[i][1]]
            else:
                ans[i] = arr[queries[i][0]-1] ^ arr[queries[i][1]]
            
        return ans

        