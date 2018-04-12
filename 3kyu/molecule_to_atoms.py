braces = {"(": ")", "[": "]"}
result = {}

def add_result(key, cnt=1):
    if key:
        if key in result:
            result[key] += cnt
        else:
            result[key] = cnt
    return ""   # reset key

def parse_molecule(formula):
    key = ""
    for f in formula:
        if f.isupper():
            if key:
                key = add_result(key)
            else:
                key += f
        elif f.islower():
            key += f
        elif f.isdigit():
            key = add_result(key, int(f))
        else:
            # TODO: find brace
            pass
    if key:
        add_result(key)
    print result
    return result


def equals_atomically(obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for k in obj1:
        if obj1[k] != obj2[k]:
            return False
    return True


print equals_atomically(parse_molecule("H2O"), {'H': 2, 'O': 1})
print equals_atomically(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O': 2, 'H': 2})
print equals_atomically(parse_molecule("K4[ON(SO3)2]2"), {'K': 4, 'O': 14, 'N': 2, 'S': 4})