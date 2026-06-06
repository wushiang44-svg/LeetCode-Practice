class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)

        return list(common.elements())