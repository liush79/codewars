braces = {"(": ")", "[": "]", "{": "}"}


def add_result(result, key, cnt=1):
    if key:
        if key in result:
            result[key] += cnt
        else:
            result[key] = cnt
    return ''   # reset key


def find_num(string):
    str_num = ''
    for s in string:
        if not s.isdigit():
            break
        str_num += s
    return int(str_num)


def parse_molecule(formula, times=1):
    result = {}
    key = ''
    i = 0
    len_formula = len(formula)
    while i < len_formula:
        f = formula[i]
        if f.isupper():
            if key:
                key = add_result(result, key)
            key += f
        elif f.islower():   # for such as 'Mg'
            key += f
        elif f.isdigit():   # for such as 'O2' = {'O': 2}
            key = add_result(result, key, find_num(formula[i:]))
        else:
            # for ( ) or [ ]
            if f in braces:
                start = i + 1
                end = formula[start:].find(braces[f]) + start
                i = end
                cnt = 1
                if end < len_formula - 1 and formula[end + 1].isdigit():
                    cnt = find_num(formula[end + 1:])
                    i += 1
                # join dict
                sub_result = parse_molecule(formula[start:end], cnt)
                for k, v in sub_result.items():
                    if k in result:
                        result[k] += v
                    else:
                        result[k] = v
        i += 1
    if key:
        add_result(result, key)
    for k, v in result.items():
        result[k] = v * times

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

print parse_molecule("C6H12O6")
print parse_molecule("(C5H5)Fe(CO)2CH3")
