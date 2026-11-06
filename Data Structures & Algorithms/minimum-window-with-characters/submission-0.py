class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s): 
            return "" 
        need = Counter(t) 
        have_count = {} 
        have, required = 0, len(need) 
        best_len = float("inf") 
        best_start = 0 
        left = 0 

        for right, ch in enumerate(s): 
            have_count[ch] = have_count.get(ch, 0) + 1 
            if ch in need and have_count[ch] == need[ch]: 
                have += 1 
                
            while have == required: 
                if right - left + 1 < best_len: 
                    best_len = right - left + 1 
                    best_start = left 

                left_ch = s[left] 
                have_count[left_ch] -= 1 
                if left_ch in need and have_count[left_ch] < need[left_ch]: 
                    have -= 1 
                left += 1 

        return "" if best_len == float("inf") else s[best_start : best_start + best_len]




