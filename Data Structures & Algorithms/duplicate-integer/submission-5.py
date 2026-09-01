class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_list = set()
        for items in nums:
            if items in seen_list:
                return True
            seen_list.add(items)
        return False
