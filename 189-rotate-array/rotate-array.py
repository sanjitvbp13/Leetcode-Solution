class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, li, ri):
            while li < ri:
                temp = nums[li]
                nums[li] = nums[ri]
                nums[ri] = temp
                li += 1
                ri -= 1

        k = k % len(nums)
        if k < 0:
            k += len(nums)
        reverse(nums, 0, len(nums) - k - 1)
        reverse(nums, len(nums) - k, len(nums) - 1)
        reverse(nums, 0, len(nums) - 1)
        