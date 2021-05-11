class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_indices = [i for i, x in enumerate(wordsDict) if x == word1]
        word2_indices = [i for i, x in enumerate(wordsDict) if x == word2]
        
        min_so_far = math.inf
        for i in word1_indices:
            for j in word2_indices:
                if min_so_far > abs(i - j):
                    min_so_far = abs(i - j)
        
        return min_so_far