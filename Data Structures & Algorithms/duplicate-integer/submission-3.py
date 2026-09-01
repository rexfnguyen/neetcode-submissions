# Python
class Solution:
    def hasDuplicate(self, nums):
        seen_list = set()
        for item in nums:
            if item in seen_list:
                return True
            seen_list.add(item)
        return False