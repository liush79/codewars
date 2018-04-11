braces = {'(': ')', '[': ']', '{': '}'}


def group_check(string):
    stack = []
    for s in string:
        if s in braces:
            stack.append(s)
        else:
            if s.isalnum():
                continue
            if not stack or braces[stack.pop()] != s:
                return False
    return len(stack) == 0


print group_check("()")         # True
print group_check("([{}])")     # True
print group_check("([{}]))")    # False
print group_check("([{{(")      # False
