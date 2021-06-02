class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_counter = defaultdict(int)
        longest = 0
        left = 0
        for right in range(len(s)):
            window_counter[s[right]] += 1
            while right - left + 1 - max(window_counter.values()) > k:
                window_counter[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
            