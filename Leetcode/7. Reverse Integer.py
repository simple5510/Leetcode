"""
给定一个 32 位有符号整数，将整数中的数字进行反转。
示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""


class Solution:
    # 整除得到每位数
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        :type r: int
        """
        r = 0
        a = abs(x)
        while (a != 0):
            r = r * 10 + a % 10
            a = int(a / 10)
        if x > 0 and r < 2 ** 31:
            return r
        elif x < 0 and r <= 2 ** 31:
            return -r
        else:
            return 0

    # 转换成字符串的方法
    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        # [:-1]是为了去掉负号
        x_rev = int(str(x)[::-1]) if x >= 0 else - int(str(x)[::-1][:-1])
        return x_rev if x_rev > -1 * 2 ** 31 and x_rev < 2 ** 31 - 1 else 0
