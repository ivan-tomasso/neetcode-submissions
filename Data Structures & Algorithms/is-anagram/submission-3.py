class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seenS, seenT = {}, {}
        for letter in s:
            seenS[letter] = seenS.get(letter, 0) + 1
        for letter in t:
            seenT[letter] = seenT.get(letter, 0) + 1
        
        return seenS == seenT   
