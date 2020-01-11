"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ''' O(n^3) / O(n) '''
        if len(s) == 0:
            return 0
        
        max_len = 0
        for i in range(len(s)):
            visited = set()
            len_i = 0
            for j in range(i, len(s)):
                ch = s[j]
                if not ch in visited:
                    visited.add(ch)
                    len_i += 1
                    if len_i > max_len:
                        max_len = len_i
                else:
                    break
            if i + max_len > len(s):
                break
        return max_len
