class Solution(object):
    def twoSum(self, nums, target):
        index=dict()
        for i in range(0,len(nums)):
            if nums[i] in index:
                return [index[nums[i]],i]
            else:
                index[target-nums[i]]=i
