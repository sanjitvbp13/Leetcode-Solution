class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        setty = set(['a','e','i','o','u'])
        l = [1 if s[i] in setty else 0 for i in range(len(s))]
        sm = sw = sum(l[:k])

        for i in range(k, len(s)):
            sw += l[i] - l[i - k]
            sm = max(sw, sm)

        return sm