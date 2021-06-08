class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def stringToVal(word):
            word = word.lower()
            total = []
            for c in word:
                val = ord(c) - 97
                total.append(str(val))
            return int("".join(total))
        word1 = stringToVal(firstWord)
        word2 = stringToVal(secondWord)
        target = stringToVal(targetWord)
        print(word1, word2)
        if word1 + word2 == target:
            return True
        return False