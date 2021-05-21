class Solution:
    def isPalindrome(self, x: int) -> bool:
        # given int x, if xis palin drome, return tre
        # same forward and backwards
        # x = 121 -> true
        # x = -121 -> false
        # x = 10 ->
        # follow, solve without converting.
        
        # min 3 digits
        # max 5 digits
        # 0 is valid
        # -101 = false
        
        # x = 12345 
        # 54321

        # x = 10101
        # 10101

        # convert to string
        # reverse string
        # compare: if the same == palindrome
        
        # two pointers
        # front and back
        # step them towards the middle
        # compare each item
        # if each item is the same, palindrome
        
        if x < 0:
            return False
        
        num_string = str(x)
        rev_string = num_string[::-1]
        
        if num_string == rev_string:
            return True
        else:
            return False
        
        
        