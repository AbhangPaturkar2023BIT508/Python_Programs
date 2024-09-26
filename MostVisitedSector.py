class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        first = rounds[0]
        last = rounds[-1]
        
        if last>=first:
            return [i for i in range(first,last+1)]
        else:
            rec = []
            for i in range(1, n+1):
                if i<=last or i>=first:
                    rec.append(i)
            return sorted(rec)