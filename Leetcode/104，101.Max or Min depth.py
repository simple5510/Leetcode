# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    # 递归
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # DFS
    def maxDepth2(self, root):
        stack = []
        if root is not None:
            # 传入节点和层数
            stack.append((root, 1))
        depth = 0
        while stack != []:
            root, current_depth = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((root.left, current_depth + 1))
                stack.append((root.right, current_depth + 1))
        return depth

    # BFS
    def maxDepth3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([(root, 1)])  # here the 2nd number is level
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            return level

    # DFS
    def minDepth(self, root):
        if not root: return 0
        if not root.left and not root.left:
            return 1
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    # BFS
    def minDepth2(self, root):
        if not root: return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))
