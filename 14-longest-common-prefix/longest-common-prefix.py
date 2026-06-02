class Solution(object):
    def longestCommonPrefix(self, s):
       
        
        v = sorted(s)
        ans =""
        first = v[0]
        last = v[-1]
        for i in range(min(len(first),len(last))):
            if first[i]!= last[i]:
                return ans
            ans += first[i]
        return ans