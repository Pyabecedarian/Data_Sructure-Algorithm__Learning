"""
Path sum
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root: TreeNode, sum: int) -> bool:
    if not root:
        return False

    sum -= root.val
    if not (root.left or root.right):
        return sum == 0

    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)