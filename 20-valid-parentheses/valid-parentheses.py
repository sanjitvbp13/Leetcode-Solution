class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        pairs={')':'(', ']':'[','}':'{'}
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or stack[-1]!= pairs[char]:
                    return False
                stack.pop()
        return not stack                    

        