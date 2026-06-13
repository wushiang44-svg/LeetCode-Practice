class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        units = [
            "", "Thousand", "Million", "Billion"
        ]


        result = ""
        times = 0

        while num > 0:
            part = num % 1000
            num = num // 1000
            if part != 0:
                result = self.helper(part) + " " + units[times] + " " + result

            times += 1
        
        return result.strip()
            

    def helper(self, part):
        below_20 = [
            "", "One", "Two", "Three", "Four",
            "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        units = [
            "", "Thousand", "Million", "Billion"
        ]


        result = ""
        if part == 0:
                result = ""
            
        elif part < 20:
            result = below_20[part]
        
        elif part < 100:
            one = part % 10
            ten = part // 10
            result = tens[ten] + " " + below_20[one]
        
        elif part < 1000:
            hundred = part // 100
            remainder = part % 100
            result = below_20[hundred] + " Hundred " + self.helper(remainder) 

        return result.strip()