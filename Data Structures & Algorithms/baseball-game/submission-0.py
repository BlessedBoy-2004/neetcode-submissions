class Solution:
    def calPoints(self, operations):
        stack=[]
        new_score=0
        for char in operations:
            if char=="+":
                new_score=stack[-1]+stack[-2]
                stack.append(new_score)
            elif char=="C":
                stack.pop()
            elif char=="D":
                new_score=stack[-1]*2
                stack.append(new_score)
            else:
                score=int(char)
                stack.append(score)
        return sum(stack)
        