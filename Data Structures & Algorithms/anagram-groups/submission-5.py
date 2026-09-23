class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hash map
        group = {}

        for word in strs:
            #sort the characters
            sorted_word = "".join(sorted(word))

            if sorted_word not in group:
                group[sorted_word] = []
            
            group[sorted_word].append(word)
        
        return list(group.values())