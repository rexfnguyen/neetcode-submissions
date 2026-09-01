class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for w in strs:
            sorted_w = "".join(sorted(w))

            if sorted_w not in group:
                group[sorted_w] = []
        
            group[sorted_w].append(w)

        return list(group.values())