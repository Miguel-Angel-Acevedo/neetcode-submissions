class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        words = {}

        for w in s:
            words[w] = words.get(w, 0) + 1
        for w in t:
            words[w] = words.get(w, 0) - 1
        
        for value in words.values():
            if value != 0:
                return False

        return True

        