class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dir1 = {}
        heap = []
        for num in nums:
            dir1[num] = dir1.get(num, 0)+1
        for n , f in dir1.items():
            heapq.heappush(heap, [f,n])
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
