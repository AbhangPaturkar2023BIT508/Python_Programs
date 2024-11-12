class Solution:

    def binary_search(self, items, target_price):
        start, end = 0, len(items) - 1
        max_beauty = 0
        while start <= end:
            mid = (start + end) // 2
            if items[mid][0] > target_price:
                end = mid - 1
            else:
                max_beauty = max(max_beauty, items[mid][1])
                start = mid + 1
        return max_beauty

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x : x[0])

        max_beauty = items[0][1]
        for i in range(len(items)):
            max_beauty =  max(max_beauty, items[i][1])
            items[i][1] = max_beauty
        ans = []

        for q in queries:
            ans.append(self.binary_search(items, q))

        return ans

        