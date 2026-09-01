class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_list = set()
        for x in nums:
            if x in seen_list:
                return True
            seen_list.add(x)
        return False
    