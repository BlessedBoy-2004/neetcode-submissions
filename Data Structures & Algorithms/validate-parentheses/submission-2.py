class Solution:
    def isValid(self,s):
        mapping={")":"(","]":"[","}":"{"}
        stack=[]
        for char in s:
            if char in mapping:
                if not stack:
                    return False
                top_element=stack.pop()
                if top_element!=mapping[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0