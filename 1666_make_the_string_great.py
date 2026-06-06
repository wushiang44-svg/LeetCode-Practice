class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for x in s:
            stack.append(x)
            if len(stack) >= 2 and stack[-1].swapcase() == stack[-2]:
                stack.pop()
                stack.pop()
        
        result = "".join(stack)

        return result