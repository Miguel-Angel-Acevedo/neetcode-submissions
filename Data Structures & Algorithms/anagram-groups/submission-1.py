class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for w in strs:
            key = ''.join(sorted(w))

            if key in seen:
                seen[key].append(w)
            else:
                seen[key] = [w]
        return list(seen.values())