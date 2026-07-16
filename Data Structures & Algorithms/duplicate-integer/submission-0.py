class Solution:
    def hasDuplicate(self,nums):
        seen=[]
        for i in range(len(nums)):
            current=nums[i]
            if current in seen:
                return True
            else:
                seen.append(current)
        return False        