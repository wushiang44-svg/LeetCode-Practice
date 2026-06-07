class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        new_arr = sorted(arr)
        result = []

        minimun = new_arr[-1] - new_arr[0]

        for i in range(1, len(new_arr)):
            if (new_arr[i] - new_arr[i-1]) < minimun:
                minimun = (new_arr[i] - new_arr[i-1])

        for i in range(1, len(new_arr)):
            if (new_arr[i] - new_arr[i-1]) == minimun:
                result.append([new_arr[i-1], new_arr[i]])
        
        return result