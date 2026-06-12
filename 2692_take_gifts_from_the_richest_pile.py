class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-x for x in gifts]

        heapq.heapify(heap)

        for i in range(k):
            largest = -heapq.heappop(heap)

            new_value = int(math.sqrt(largest))

            heapq.heappush(heap, -new_value)
        
        return -sum(heap)