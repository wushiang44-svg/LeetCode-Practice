class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # three pointer
        m_index = m - 1
        n_index = n - 1
        current = m + n - 1

        # iteration is not n_index!
        while n_index >= 0:
            if m_index >= 0 and nums1[m_index] > nums2[n_index]:
                nums1[current] = nums1[m_index]
                m_index -= 1
            else:
                nums1[current] = nums2[n_index]
                n_index -= 1

            current -= 1