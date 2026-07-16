class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sFreq = [0] * 26
        tFreq = [0] * 26
        for char in s: 
            idx = ord(char) - 97
            sFreq[idx] += 1

        for char in t:
            idx = ord(char) - 97
            tFreq[idx] += 1

        if sFreq == tFreq:
            return True
        else:
            return False
            