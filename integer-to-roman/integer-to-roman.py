class Solution:
    def intToRoman(self, num: int) -> str:
        values = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
        
        roman = ""
        
        for i in values:
            roman += (num//i) * values[i] 
            # floor divives num with value[i] to give number of times it fits in
            # * actual roman value.  So 3000 = 3 * "M"
            num = num % i
            # gives remainder after than roman value
        
        return roman