class Solution:
    def twoSum(self, nums,target):
        seen={}
        for i in range(len(nums)):
            current=nums[i]
            needed=target-current
            if needed in seen:
                return [seen[needed],i]
            else:
                seen[current]=i
