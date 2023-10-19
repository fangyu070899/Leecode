

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for item in s:
        if item == '(' or item == '[' or item == '{':
            stack.append(item)
        elif len(stack) == 0: 
            return False
        else:
            if item == ')' and stack[-1] == '(':
                stack.pop()
            elif item == ']' and stack[-1] == '[':
                stack.pop()
            elif item == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
        print(stack)

    if len(stack) != 0:
        return False
    return True
            

if __name__=='__main__':
    s="([]])"
    print(isValid(s))
