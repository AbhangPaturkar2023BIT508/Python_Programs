class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        plates = []

        starCnt = 0
        psStar = []
        for ch in s:
            if ch is '*':
                starCnt+=1
            psStar.append(starCnt)

        for query in queries:
            lc = s.find('|', query[0], query[1]+1)
            rc = s.rfind('|', query[0], query[1]+1)
            if lc == -1 or rc == -1:
                plates.append(0)
            else:
                plates.append(psStar[rc]-psStar[lc])

        return plates