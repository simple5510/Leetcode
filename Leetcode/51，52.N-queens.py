'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1: return []
        self.result = []

        self.cols = set()
        self.pie = set()
        self.na = set()

        self.DFS(n, 0, [])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        # 递归的终止条件，row>n说明超出行数
        if row >= n:
            self.result.append(cur_state)
            return
        # 对每一层遍历所有的列
        for col in range(n):
            # 筛选条件：出现在皇后的攻击路线上，则continue
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue
            # 如果可以放置皇后，则把皇后放置当前位置并更新皇后位置条件
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)
            # 递归下一行
            self.DFS(n, row + 1, cur_state + [col])
            # 还原棋盘，看其他位置是否有解
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    # 输出结果
    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append('.' * i + 'Q' + '.' * (n - i - 1))
        return [board[i:i + n] for i in range(0, len(board), n)]

    # 简洁版
    def solveNQueens2(self, n):
        def DFS(queens, xy_dif, xy_sum):
            row = len(queens)
            if row == n:
                result.append(queens)
                return None
            for col in range(n):
                if col not in queens and row - col not in xy_dif and row + col not in xy_sum:
                    DFS(queens + [col], xy_dif + [row - col], xy_sum + [row + col])

        result = []
        DFS([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in result]
