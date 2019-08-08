from task2.stack import Stack


def isValid(s):
    stack = Stack()
    check = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    i = 0
    balanced = True

    while i < len(s) and balanced:
        bracket = s[i]
        if bracket in '([{':
            stack.push(bracket)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                if stack.pop() != check[bracket]:
                    balanced = False

        i += 1

    if balanced and stack.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(isValid('()([[}]])'))
