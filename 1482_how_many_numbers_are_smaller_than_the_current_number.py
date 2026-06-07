class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = [0] * 101

        for i in nums:
            freq[i] += 1
        
        for i in range(1, len(freq)):
            freq[i] += freq[i-1]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 0
                continue
            nums[i] = freq[nums[i] - 1]

        return nums