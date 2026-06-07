class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        anwser = []
        for i in range(1,n+1):
            if (i)%3 == 0 and (i)%5 == 0:
                anwser.append("FizzBuzz")
            elif (i)%3 == 0:
                anwser.append("Fizz")
            elif (i)%5 == 0:
                anwser.append("Buzz")
            else:
                anwser.append(str(i))
        
        return anwser