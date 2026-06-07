class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_detail = {}
        for i, c in enumerate(order):
            order_detail[c] = i
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j] and order_detail[word1[j]] > order_detail[word2[j]]:
                    return False
                elif word1[j] != word2[j] and order_detail[word1[j]] < order_detail[word2[j]]:
                    break
                elif len(word1) > len(word2) and j == len(word2) - 1 and word1[j] == word2[j]:
                    return False

        return True