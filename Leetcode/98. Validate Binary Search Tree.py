''''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.inorder == list(sorted(set(self.inorder))) or self.helper(root)

    # 中序遍历一次，如果是BST则应该是升序，但使用了过多的内存，空间不划算
    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    # 中序遍历，只需记录前驱结点，当前节点与前继节点比较
    # 前驱节点val值小于该节点val值并且值最大的节点
    # 后继节点val值大于该节点val值并且值最小的节点
    def helper(self, root):
        # 空树是BST
        if root is None:
            return True
        # 验证左子树
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)

    def comparation(self, root, min=None, max=None):
        if root is None:
            return True
        if (min is not None and root.val <= min):
            return False
        if (max is not None and root.val >= max):
            return False
        return self.comparation(root.left, min, root.val) and self.comparation(root.right.root.val, max)
