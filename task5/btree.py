class BinaryTree(object):

    def __init__(self, rootObj):
        self.root = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            tmp = BinaryTree(newNode)
            tmp.leftChild = self.leftChild
            self.leftChild = tmp

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            tmp = BinaryTree(newNode)
            tmp.rightChild = self.rightChild
            self.rightChild = tmp

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRoot(self, rootObj):
        self.root = rootObj

    def getRoot(self):
        return self.root

    def traversal(self, order='preorder'):
        if order == 'preorder':
            print(self.root)
            if self.leftChild:
                self.leftChild.traversal('preorder')
            if self.rightChild:
                self.rightChild.traversal('preorder')

        elif order == 'postorder':
            if self.leftChild:
                self.leftChild.traversal('postorder')
            if self.rightChild:
                self.rightChild.traversal('postorder')
            print(self.root)

        elif order == 'inorder':
            if self.leftChild:
                self.leftChild.traversal('inorder')
            print(self.root)
            if self.rightChild:
                self.rightChild.traversal('inorder')



if __name__ == '__main__':
    btree = BinaryTree(0)
    btree.insertLeft(1)
    btree.insertRight(2)
