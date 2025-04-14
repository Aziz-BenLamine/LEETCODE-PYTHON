class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = {}
        for num in nums:
            if num not in me:
                me[num] = 1
            else:
                me[num] += 1
            if me[num] >= len(nums)/2 :
                return num