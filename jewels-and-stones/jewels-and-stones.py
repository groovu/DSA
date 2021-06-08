class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        total = 0
        for j in jewel_set:
            total += stones.count(j)
        return total