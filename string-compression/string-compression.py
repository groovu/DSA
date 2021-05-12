# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         # result = []
#         # prev = chars[0]
#         # count = 0
#         # iterate through c in list
#         # if char == prev:
#         # add to counter
#         # if char != prev; we have a new char; save previous results and  reset
#         # if count == 1: don't add a number to string.
#         # prev char = new char
#         # counter = 1
#         # counter = 0
#         # for c in chars:
#         #     if c == prev:
#         #         counter += 1
#         #     if c != prev:
#         #         result.append(c)
#         #         if counter > 1:
#         #             result.append(str(counter))
#         #         prev = c
#         #         counter = 1
#         # result.append(chars[-1])
#         # result.append(str(counter))
#         # print(result)
#         # chars = result
#         # return len(result)
#         # lol right end result, but they want you to modify chars not just replace it.
        
#         # try two ptrs
#         # head, runner.
#         # runner moves until it finds a different char
#         # head moves forward, replaces char in position if needed by number of reps
#         # if it does replace, move head again, else head stays put
#         # runner returns to head.
#         # repeat
#         print(chars)
        
# #         head = 0
# #         runner = 0
        
# #         counter = 1
# #         while runner < len(chars) - 1:
# #             runner += 1
# #             if chars[head] == chars[runner]:
# #                 counter += 1
# #                 continue
# #             elif chars[head] != chars[runner]:
# #                 if counter > 1:
# #                     chars[head+1] = str(counter)
# #                     head = runner
# #                     counter = 1

# #         # head should be at last letter now.
# #         # 
# #         print(chars)

#         walker, runner = 0, 0
#         while runner < len(chars):
		
#             chars[walker] = chars[runner]
#             count = 1
			
#             while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
#                 runner += 1
#                 count += 1
			
#             if count > 1:
#                 for c in str(count):
#                     chars[walker+1] = c
#                     walker += 1
            
# 			runner += 1
#             walker += 1
        
#         return walker

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        walker, runner = 0, 0
        while runner < len(chars):
            chars[walker] = chars[runner]
            count = 1
			
            while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
                runner += 1
                count += 1
			
            if count > 1:
                for c in str(count):
                    chars[walker+1] = c
                    walker += 1
            runner += 1
            walker += 1
        
        return walker