class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        def letterCount(s):
            letterC = {}
            for char in s:
                if(char in letterC):
                    letterC[char] += 1
                else:
                    letterC[char] = 1
            return letterC
        return letterCount(s) == letterCount(t)