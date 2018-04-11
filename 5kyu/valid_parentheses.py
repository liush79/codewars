braces = {'(': ')', '[': ']', '{': '}'}


def valid_parentheses(string):
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


print valid_parentheses("()")         # True
print valid_parentheses("([{}])")     # True
print valid_parentheses("([{}]))")    # False
print valid_parentheses("([{{(")      # False
