class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_pair = 0
        freq = Counter(nums)

        for value in freq.values():
            total_pair += ((value * (value-1))/2)
        
        return total_pair