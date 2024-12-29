class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        max = num
        for i in range(t):
            max += 2
        return max