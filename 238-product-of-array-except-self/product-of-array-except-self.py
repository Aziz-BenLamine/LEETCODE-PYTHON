class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            j = - i -1
            res[i] *= prefix
            prefix *= nums[i]
            res[j] *= postfix
            postfix *= nums[j]
        return res