class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        map = {}
        for v in arr:
            if v in map:
                map[v] = map.get(v)+1
            else:
                map[v] = 1
        
        for v in arr:
            if map.get(v) == 1:
                k -= 1
            if k == 0:
                return v;

        return ''