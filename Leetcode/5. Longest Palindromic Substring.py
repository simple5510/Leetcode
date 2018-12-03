"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。

示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2 or s == s[::-1]:
            return s

        l = len(s)

        # 可以扩展的最大长度最小是1
        start,longestLen = 0, 1

        # i为回文串的右侧边界
        for i in range(1, l):
            odd = s[i - longestLen - 1:i + 1]  # 取得奇数串
            even = s[i - longestLen:i + 1]  # 取得偶数串
            if i - longestLen > 0 and odd == odd[::-1]:
                start = i - longestLen - 1
                longestLen += 2
            elif i - longestLen >= 0 and even == even[::-1]:
                start = i - longestLen
                longestLen += 1
        return s[start:start + longestLen]
