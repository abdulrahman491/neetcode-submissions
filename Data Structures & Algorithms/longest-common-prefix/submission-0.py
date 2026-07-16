class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minLen = len(strs[0])
        for string in strs:
            if string == "":
                return ""
            if len(string) < minLen:
                minLen = len(string)


        charIdx = 0
        out = ""
        while charIdx < minLen:
            strsIdx = 0
            lastChar = strs[strsIdx][charIdx]
            strsIdx = 1
            while strsIdx < len(strs):
                if lastChar != strs[strsIdx][charIdx]:
                    return out
                strsIdx += 1
            out += lastChar
            charIdx += 1

        return out

