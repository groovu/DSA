class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        
        count = defaultdict(int)
        
        for i in A:
            count[i] += 1
        
        max_val = -1
        for key, value in count.items():
            if value == 1:
                max_val = max(max_val, key)
        
        return max_val
        
