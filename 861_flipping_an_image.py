class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        for i in range(n):
            col = image[i]
            for j in range(n//2):
                temp = col[j]
                col[j] = col[n-1-j]
                col[n-1-j] = temp

            for x in range(n):
                if col[x] == 0:
                    col[x] = 1
                else:
                    col[x] = 0
        
        return image