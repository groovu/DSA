class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # given an array of words
        # create a square where each row is a word
        # a word square is valid if the word formed by the ith row == ith col
        # assumptions
        # num rows between 1 and 500
        # word length between 1 and 500
        # each word is in lower case
        #questions
        # are all words the same length?
        # can words have empty spaces in them?
        # idk what else
        # approaches
        # build an 2d array
        # where each row is the string broken into chars
        # iterate over num of rows
        # check that row i == col i
        # row i == str(row i)
        # col i = string builder of row[i]
        
#         array = []
#         for i in range(len(words)):
#             array.append(list(words[i]))
            
#         for i in range(len(words)):
#             row_word = "".join(array[i])
#             col_word = ""
            
#             print(row_word)
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
            
        return True
        
        