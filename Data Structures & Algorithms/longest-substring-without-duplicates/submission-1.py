class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        in_window = set() 
        left = 0 
        best = 0 
        for right, ch in enumerate(s): 
            while ch in in_window: 
                in_window.remove(s[left]) 
                left += 1 
            in_window.add(ch) 
            best = max(best, right - left + 1) 
        return best 