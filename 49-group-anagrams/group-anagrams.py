class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count) #Because python dosent accept arrays as keys

            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        
        return list(res.values())
