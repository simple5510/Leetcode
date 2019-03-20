'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._gen(0, 0, n, '')
        return self.list

    def _gen(self, left, right, n, result):
        # 左右括号都用完说明生产力一个答案
        if right == n and left == n:
            self.list.append(result)
            return
        # 左括号没用完添加一个左括号
        if left < n:
            self._gen(left + 1, right, n, result + '(')
        # 右括号比左括号少且右括号没用完才可以添加一个右括号
        if right < left and right < n:
            self._gen(left, right + 1, n, result + ')')
