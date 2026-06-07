class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        res = ''
        i, j, carry = 0, 0, 0

        while i < len(num1) or j < len(num2):
            temp = carry
            if i < len(num1):
                temp += ord(num1[i]) - ord('0')
                i += 1
            if j < len(num2):
                temp += ord(num2[j]) - ord('0')
                j += 1
            carry = 1 if temp >= 10 else 0
            res += str(temp % 10)
        
        if carry == 1:
            res += str(carry)

        return res[::-1]