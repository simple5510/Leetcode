''''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
'''
from functools import reduce


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def back(stack, c):
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
            return stack

        return reduce(back, S, []) == reduce(back, T, [])

    def backspaceCompare2(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        st1 = []
        st2 = []
        for c in S:
            if c != '#':
                st1.append(c)
            else:
                if st1:
                    st1.pop()

        for c in T:
            if c != '#':
                st2.append(c)
            else:
                if st2:
                    st2.pop()
        return st1 == st2


class Solution2(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i, j = len(S) - 1, len(T) - 1

        while i >= 0 and j >= 0:
            i = self.find_next(S, i)
            j = self.find_next(T, j)

            if i < 0 and j < 0:
                return True

            if i < 0 or j < 0 or S[i] != T[j]:
                return False

            j -= 1
            i -= 1

        i = self.find_next(S, i)
        j = self.find_next(T, j)

        return i < 0 and j < 0

    def find_next(self, S, i):
        skip_i = 0

        while i >= 0 and (S[i] == '#' or skip_i):
            if S[i] == '#':
                skip_i += 1
            else:
                skip_i -= 1
            i -= 1

        return i
