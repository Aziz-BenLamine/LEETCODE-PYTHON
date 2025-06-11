class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingP = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for c in s:
            if c in closingP:
                if stack and stack[-1] == closingP[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack