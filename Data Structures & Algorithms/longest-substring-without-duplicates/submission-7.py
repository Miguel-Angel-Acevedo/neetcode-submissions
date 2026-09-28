class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        char = set()

        l, r = 0, 0

        while r < len(s):
            if s[r] not in char:
                char.add(s[r])
                r += 1
                longest= max(longest, r - l)
            else:
                char.remove(s[l])
                l += 1
        return longest

                
            
        
        
            