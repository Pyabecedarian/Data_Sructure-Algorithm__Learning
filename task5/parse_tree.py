from task5.btree import BinaryTree
import operator as op


def buildParseTree(fpexp):
    """Parse a math formula into a binary tree"""
    pStack = []
    eTree = BinaryTree('')
    currTree = eTree

    for token in fpexp:
        if token == ' ':
            continue

        if token == '(':
            currTree.insertLeft('')
            pStack.append(currTree)
            currTree = currTree.getLeftChild()
        elif token in ['+', '-', '*', '/']:
            currTree.setRoot(token)
            currTree.insertRight('')
            pStack.append(currTree)
            currTree = currTree.getRightChild()
        elif token == ')':
            try:
                currTree = pStack.pop()
            except IndexError:  # pop from empty list
                return eTree

        else:
            try:
                currTree.setRoot(float(token))
                currTree = pStack.pop()
            except ValueError:
                raise ValueError('Token %s is not a valid number!' % token)


def evaluate(parseTree):
    """Compute the result of bTree"""
    ops = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()

    if leftChild and rightChild:
        f = ops[parseTree.getRoot()]
        return f(evaluate(leftChild), evaluate(rightChild))

    else:
        return parseTree.getRoot()


def preorder(btree):
    """External version of preorder traversal """
    if btree:
        print(btree.getRoot())
        preorder(btree.getLeftChild())
        preorder(btree.getRightChild())


def postorder(btree):
    """External version of postorder traversal"""
    if btree:
        postorder(btree.getLeftChild())
        postorder(btree.getRightChild())
        print(btree.getRoot())


def inorder(btree):
    """External version of inorder traversal"""
    if btree:
        inorder(btree.getLeftChild())
        print(btree.getRoot())
        inorder(btree.getRightChild())


def postordereval(parseTree):
    """Compute the result inline with postorder"""
    ops = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

    if parseTree:
        evalLeft = postordereval(parseTree.getLeftChild())
        evalRight = postordereval(parseTree.getRightChild())
        if evalLeft and evalRight:
            return ops[parseTree.getRoot()](evalLeft, evalRight)
        else:
            return parseTree.getRoot()


def printexp(btree):
    """Retrieve the hold math formula string from bTree"""
    s = ''
    if btree:
        s += '(' + printexp(btree.getLeftChild())
        s += str(btree.getRoot())
        s += printexp(btree.getRightChild()) + ')'

    return s


def printexp_v2(btree):
    """Retrieve the hold math formula string from bTree (better version)"""
    s = ''
    if btree:
        leftC = btree.getLeftChild()
        righC = btree.getRightChild()
        if leftC and righC:
            s += '(' + printexp_v2(leftC)
            s += str(btree.getRoot())
            s += printexp_v2(righC) + ')'
        else:
            s += str(btree.getRoot())

    return s


if __name__ == '__main__':
    fpexp = '( ( 1 + 5 ) * 3 )'
    parseTree = buildParseTree(fpexp)

    # print(evaluate(parseTree))
    print(postordereval(parseTree))  # 18.0


    # print(fpexp)
    # preorder(parseTree)
    # postorder(parseTree)
    # inorder(parseTree)
    # print(printexp(parseTree))
    print(printexp_v2(parseTree))   # ((1.0+5.0)*3.0)
