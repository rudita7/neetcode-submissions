class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        output = []
        if len(s) % 2:
            return False

        for i, c in enumerate(s):
            p = None
            closer = None
            if stack:
                p = stack[-1]
            if p == "(":
                closer = ")"
            elif p == "{":
                closer = "}"
            elif p == "[":
                closer = "]"
            if c == closer:
                stack.pop()
            elif c != closer:
                stack.append(c)
        if not stack:
            return True 
        else:
            return False



                
                
                
