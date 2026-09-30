class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        longest = 0
        l = 0

        for r in range (len(s)):
            dic[s[r]] = 1 + dic.get(s[r], 0)

            while (r-l)+1 - max(dic.values()) > k:
                dic[s[l]] -= 1
                l += 1

            longest = max(longest, (r-l) +1)
        return longest