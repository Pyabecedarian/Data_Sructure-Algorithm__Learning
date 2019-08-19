class TreeNode(object):
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChild(self):
        return self.leftChild or self.rightChild

    def hasBothChild(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, k, v):
        self.key = k
        self.payload = v

    def findSuccessor(self):
        """
        There are three cases to consider when looking for a successor:
            1. If the node has a right child, then the successor is the smallest key
                in the right subtree
            2. If the node has no right child and is the left child of its parent,
                then the parent is the successor
            3. If the node is the right child of its parent, and itself has no right
                child, then the successor to this node is the successor of its parent,
                excluding this node.
        """
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self

        return succ

    def findMin(self):
        """Find the minimum key in a subtree, which is the leftmost child of the subtree"""
        curr = self
        while curr.hasLeftChild():
            curr = curr.leftChild
        return curr

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChild():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __setitem__(self, k, v):
        self.put(k, v)

    def __getitem__(self, k):
        return self.get(k)

    def __contains__(self, k):
        if self._get(k, self.root):
            return True
        else:
            return False

    def __iter__(self):
        return self.root.__iter__()

    def __delitem__(self, k):
        self.delete(k)

    @property
    def length(self):
        return self.size

    def to_sequence(self):
        """Put the keys and values of bst into a list from top to bottom order"""
        queue = [self.root]
        seq_k = []
        seq_v = []

        while queue:
            res = queue.pop(0)
            seq_k.append(res.key)
            seq_v.append(res.payload)
            if res.hasLeftChild():
                queue.append(res.leftChild)
            if res.hasRightChild():
                queue.append(res.rightChild)

        return seq_k, seq_v

    def put(self, k, v):
        if not self.root:
            self.root = TreeNode(k, v)
        else:
            self._put(k, v, self.root)

        self.size += 1

    def _put(self, k, v, currNode):
        """Put the k-v pair as a leftChild or rightChild node in compliance with bst property"""
        if k < currNode.key:
            if currNode.hasLeftChild():
                self._put(k, v, currNode.leftChild)
            else:
                currNode.leftChild = TreeNode(k, v, parent=currNode)

        elif k > currNode.key:
            if currNode.hasRightChild():
                self._put(k, v, currNode.rightChild)
            else:
                currNode.rightChild = TreeNode(k, v, parent=currNode)

        else:
            currNode.payload = v
            self.size -= 1

    def get(self, k):
        if self.root:
            resNode = self._get(k, self.root)
            if resNode:
                return resNode.payload

        return

    def _get(self, k, currNode):
        """Get the node of which key is equal to the query key"""
        if not currNode:
            return
        if k < currNode.key:
            return self._get(k, currNode.leftChild)
        elif k > currNode.key:
            return self._get(k, currNode.rightChild)
        elif k == currNode.key:
            return currNode

    def delete(self, k):
        """Delete the k-v node in bst, if no such key in bst, raise KeyError"""
        if self.root:
            nodeToRemove = self._get(k, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                KeyError('No such key exists:', k)
        else:
            raise KeyError('BST is empty.')

    def remove(self, node):
        if node.isLeaf():  # the node has no child, just remove
            if node.isRoot():  # node itself is also a root node with no child
                self.root = None
            elif node.isLeftChild():
                node.parent.leftChild = None
            elif node.isRightChild():
                node.parent.rightChild = None

        elif node.hasAnyChild():  # the node has only one child, just promote the child to take it's place
            theChild = node.leftChild if node.hasLeftChild() else node.rightChild
            if node.isRoot():
                self.root = theChild
                theChild.parent = None
            elif theChild.isLeftChild():
                theChild.parent = node.parent
                node.parent.leftChild = theChild
            elif theChild.isRightChild():
                theChild.parent = node.parent
                node.parent.rightChild = theChild

        elif node.hasBothChild():  # the node has two children, complex procedure!
            # 1. find a successor
            succ = node.findSuccessor()
            # 2. remove a successor (use a new method)
            self.remove(succ)
            # succ.spliceOut()
            # 3. replace k-v pair
            node.key = succ.key
            node.payload = succ.payload


if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[3] = "red"
    mytree[4] = "blue"
    mytree[6] = "yellow"
    mytree[2] = "at"

    print(mytree[6])
    print(mytree[2])
    mytree.delete(4)
    print(mytree.to_sequence()[0])

    for i in mytree:
        print(i)