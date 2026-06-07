class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for left in range(len(s)//2):
            right = len(s) - 1 - left
            s[left], s[right] = s[right], s[left]
        
        return