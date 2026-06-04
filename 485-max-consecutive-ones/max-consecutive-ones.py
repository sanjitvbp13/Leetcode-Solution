class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_c =0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_c = max(max_c, count)
            else:
                count = 0
        return max_c
        