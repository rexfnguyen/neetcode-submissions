class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the length matches
        if len(s) != len(t):
            return False
        
        #create dicts to keep track of the char appearances
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT