class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 1:
        #     return 1
        # longest_so_far = 0
        # for i in range(len(s)):
        #     runner = i
        #     seen = set()
        #     while runner < len(s):
        #         if s[runner] not in seen:
        #             seen.add(s[runner])
        #             runner += 1
        #         else:
        #             break
        #     if (runner - i) > longest_so_far:
        #         longest_so_far = runner - i
        #     runner = len(s)
        # return longest_so_far
        if 0 <= len(s) <= 1:
            return len(s)
        longest = 0
        left = 0
        right = 0
        seen = set()
        while right < len(s):
            char = s[right]
            if char not in seen:
                seen.add(char)
                longest = max(longest, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
            
        return longest
            