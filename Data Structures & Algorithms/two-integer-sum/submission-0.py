class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hashmap to keep track of key:value
        #key = nums[i], value = i
        seen = {}

        for i in range(len(nums)):
            current_num = nums[i]
            complement = target - current_num

            if complement in seen:
                return [seen[complement], i]

            seen[current_num] = i
            