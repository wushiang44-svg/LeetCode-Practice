class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = roman[s[-1]]

        for i in range(1, len(s)):
            if roman[s[len(s) - 1 - i]] < roman[s[len(s) - i]]:
                result -= roman[s[len(s) - 1 - i]]
            else:
                result += roman[s[len(s) - 1 - i]]

        return result