class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes = [0] + gain
        biggest = 0

        for i in range(1, len(altitudes)):
            altitudes[i] += altitudes[i-1]
            if biggest < altitudes[i]:
                biggest = altitudes[i]

        return biggest