class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        count = Counter(nums1)
        result = []

        for num in nums2:
            if num in count:
                count[num] -= 1
                result.append(num)
                if count[num] == 0:
                    del count[num]
        
        return result