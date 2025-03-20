class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 0
        return sorted(res, key=res.get, reverse=True)[:k]