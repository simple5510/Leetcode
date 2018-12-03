"""
实现 atoi，将字符串转为整数。

该函数首先根据需要丢弃任意多的空格字符，直到找到第一个非空格字符为止。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

若函数不能执行有效的转换，返回 0。

说明：

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。如果数值超过可表示的范围，则返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−231) 。
"""


class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        ###better to do strip before sanity check (although 8ms slower):
        ls = list(s.strip())
        if len(ls) == 0: return 0

        # if len(s) == 0: return 0
        # ls = list(s.strip())

        # 判断正负
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']: del ls[0]

        ret, i = 0, 0

        # isdigit()
        # Returns true if string contains only digits and false otherwise.
        # ord(c)
        # Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
        # For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().

        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord(
                '0')  # 当前数字unicode减去0的unicode获得当前数字，不直接使用int是因为int conversion increases time significantly.
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))

    # 穷举列出数字表
    def myAtoi2(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+']
        k = len(str)
        for i in range(len(str)):
            if str[i] == ' ':
                continue
            if str[i] in nums:
                k = i
                break
            else:
                return 0
        e = len(str)
        for i in range(k + 1, len(str)):
            if str[i] in num:
                continue
            else:
                e = i
                break
        if str[k:e] == '-' or str[k:e] == '' or str[k:e] == '+':
            return 0
        r = int(str[k:e])
        INT_MIN = -pow(2, 31)
        INI_MAX = pow(2, 31) - 1
        if r < INT_MIN:
            return INT_MIN
        if r > INI_MAX:
            return INI_MAX
        return r

    # 正则表达式匹配法
    def myAtoi3(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re

        pattern = r"[\s]*[+-]?[\d]+"
        match = re.match(pattern, str)
        if match:
            res = int(match.group(0))
            if res > 2 ** 31 - 1:
                res = 2 ** 31 - 1
            if res < - 2 ** 31:
                res = - 2 ** 31
        else:
            res = 0
        return res
