"""
Max depth of btree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root: TreeNode) -> int:  # ugly
    d = 0
    if root:
        stack = [root]
        d += 1

        while stack:
            moreLayer = False
            subNodes = [stack.pop() for _ in range(len(stack))]

            for subNode in subNodes:
                if subNode.left:
                    stack.append(subNode.left)
                    moreLayer = True
                if subNode.right:
                    stack.append(subNode.right)
                    moreLayer = True

            if moreLayer:
                d += 1

    return d


def maxDepth_v2(root: TreeNode) -> int:
    """DFS method"""
    if not root:
        return 0
    else:
        leftHeight = maxDepth_v2(root.left)
        rightHeight = maxDepth_v2(root.right)
        return max(leftHeight, rightHeight) + 1
