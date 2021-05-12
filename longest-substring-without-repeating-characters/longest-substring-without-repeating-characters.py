class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        longest_so_far = 0
        for i in range(len(s)):
            runner = i
            seen = set()
            while runner < len(s):
                if s[runner] not in seen:
                    seen.add(s[runner])
                    runner += 1
                else:
                    break
            if (runner - i) > longest_so_far:
                longest_so_far = runner - i
            runner = len(s)
        return longest_so_far