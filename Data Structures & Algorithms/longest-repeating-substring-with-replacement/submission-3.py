class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            mostFreq = max(freq.values())

            if (r-l+1) - mostFreq <= k:
                longest = max(longest, r-l +1)
                r +=1
            else:
                freq[s[l]] -= 1
                l += 1

        return longest
        