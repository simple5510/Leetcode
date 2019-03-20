'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


# BFS
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        result = []
        queue = collections.deque()
        queue.append(root)

        # 因为是树结构不用记录访问过的节点，如果是其他结构，比如图需要记录访问节点
        # visited = set(root)

        while queue:
            # 取出当前层的总长度
            level_size = len(queue)
            current_level = []
            # 依次取出当前行的元素，并递归到下一行
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)

        return result


# DFS方法
class Solution2(object):
    def levelOrder(self, root):
        if not root: return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        # 递归终止条件
        if not node: return
        # 二维数组的长度比层数还小，说明当前层没有元素，先建立空数组
        if len(self.result) < level + 1:
            self.result.append([])
        # result是二维数组，level是层，也是下标
        self.result[level].append(node.val)
        # 递归左右子树
        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)
