class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dir1 = {}
        for ch in s:
            dir1[ch] = dir1.get(ch,0)+1
        dir2 = {}
        for ch in t:
            dir2[ch] = dir2.get(ch,0)+1
        if dir1 == dir2:
            return True
        return False

            