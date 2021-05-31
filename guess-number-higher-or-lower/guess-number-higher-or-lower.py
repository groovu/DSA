# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
#         answer = n // 2
#         found = False
#         while not found:
#             cur_guess = guess(answer)
#             if cur_guess == 0:
#                 return answer
#             if cur_guess == -1:
#                 answer = answer // 2
#             if cur_guess == 1:
#                 answer = answer + answer // 2
        head = 1
        tail = n
        while True:
            answer = head + (tail - head) //2
            curr_guess = guess(answer)
            if curr_guess == 0:
                return answer
            if curr_guess == -1:
                tail = answer - 1
            if curr_guess == 1:
                head = answer + 1
            