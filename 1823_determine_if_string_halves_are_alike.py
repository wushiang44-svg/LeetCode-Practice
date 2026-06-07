class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mid = len(s)//2
        a = s[:mid]
        b = s[mid:]
        counta = 0
        countb = 0

        vowels = set("aeiouAEIOU")

        for i in range(mid):
            if a[i] in vowels:
                counta += 1
            if b[i] in vowels:
                countb += 1

        return counta == countb