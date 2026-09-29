class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0
        l = 0
        seen = set()

        for r, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            length = max(length, r-l +1)
        return length