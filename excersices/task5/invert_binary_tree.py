"""
Invert a Binary Tree

Input：

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root: TreeNode) -> TreeNode:
    if root:
        queue = [root]
        while queue:
            currTree = queue.pop(0)
            if currTree.left:
                queue.append(currTree.left)
            if currTree.right:
                queue.append(currTree.right)

            currTree.left, currTree.right = currTree.right, currTree.left

    return root


