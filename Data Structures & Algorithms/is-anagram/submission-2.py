class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dir1 = {}
        for ch in s:
            dir1[ch] = dir1.get(ch,0)+1
        for ch in t :
            if ch not in dir1:
                return False
            dir1[ch] -=1
            if dir1[ch] < 0:
                return False
        return True

            