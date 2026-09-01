class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count first to make sure the string lengths are the same
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        # count the character
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT