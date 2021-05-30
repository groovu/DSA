class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right  = len(letters) - 1
        
        result = 0
        
        while left <= right: 
            mid = left + (right - left) // 2
            if letters[mid] > target: # search left side
                result = mid # found val that is larger than target
                right = mid - 1 # update right to contintue searching left of mid
            else:
                left = mid + 1 # continue search to right of mid to find val > target
        
        # once left and right cross over, our result should have been the last mid we found that was greater than target
        return letters[result]