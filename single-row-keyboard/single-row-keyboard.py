class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        arr = list(keyboard)
        key_map = {}
        for i in range(len(arr)):
            key_map[arr[i]] = i
        
        prev = 0
        dist = 0
        for c in list(word):
            print(c)
            print(key_map[c])
            dist += abs(key_map[c] - prev)
            prev = key_map[c]
        
        print(dist)
        return dist