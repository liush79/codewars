braces = {'(': ')', '[': ']', '{': '}'}


def validBraces(string):
    stack = []
    for s in string:
        if s in braces:
            stack.append(s)
        else:
            if not stack or braces[stack.pop()] != s:
                return False
    return True if not stack else False


print validBraces("()")         # True
print validBraces("([{}])")     # True
print validBraces("([{}]))")    # False
print validBraces("([{{(")      # False
