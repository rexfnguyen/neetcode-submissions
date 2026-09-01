class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            gap = target - nums[i]
            if gap in seen:
                return [seen[gap], i]
            
            seen[nums[i]] = i

"""
nums = [4,5,6], target = 10
i = 0, gap = 10 - 4 = 6
seen = {4:0}

i = 1, gap = 10 - 5 = 5
seen = {4:0, 5:1}

i = 2, gap = 10 - 6 = 4 --> found! return [0, 2]
seen = {4:0, 5:1}

"""