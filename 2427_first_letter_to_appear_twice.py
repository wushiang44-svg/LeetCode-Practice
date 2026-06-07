class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            if count[char] == 2:
                return char