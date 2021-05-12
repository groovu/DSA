class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = defaultdict(list)
        self.length = len(wordsDict)
        
        for index, word in enumerate(wordsDict):
            self.words[word].append(index)
        

    def shortest(self, word1: str, word2: str) -> int:
        word1Indices = self.words[word1]
        word2Indices = self.words[word2]
        index1 = 0
        index2 = 0
        min_so_far = math.inf

        while index1 < len(word1Indices) and index2 < len(word2Indices):
            word1Index = word1Indices[index1]
            word2Index = word2Indices[index2]
            min_so_far = min(min_so_far, abs(word1Index - word2Index))
            if word1Index < word2Index:
                index1 += 1
            else:
                index2 += 1
        return min_so_far

# Time Complexity
# O(len of words) to construct
# O(number of indicies for word1 and 2) to search

# Space Complexity
#O(len of words), storing all words
#O(1) to search, just checking indicies by referencing stored words.

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)