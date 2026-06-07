class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b_appear = False
        for i in range(len(s)):
            if s[i] == 'b':
                b_appear = True
            if s[i] == 'a' and b_appear:
                return False
        
        return True