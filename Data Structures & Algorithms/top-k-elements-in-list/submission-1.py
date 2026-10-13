class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dir1 = {}
        arr = []
        for num in nums:
            dir1[num] = dir1.get(num, 0)+1
        for n , f in dir1.items():
            arr.append([f,n])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
