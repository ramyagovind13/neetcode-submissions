class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        counts2 = {}
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            counts1[s1[i]] = 1 + counts1.get(s1[i], 0)
        
        l = 0
        for r in range(len(s2)):
            counts2[s2[r]] = 1+ counts2.get(s2[r], 0)
            if r-l+1 > len(s1):
                if counts2[s2[l]] == 1:
                    del counts2[s2[l]]
                else:
                    counts2[s2[l]] -= 1
                l += 1
            if counts1 == counts2:
                return True
        return False