class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        table = set(jewels)
        count = 0

        for stone in stones:
            if stone in table:
                count += 1
        return count