def string_evaluation(strng, conditions):
    result = []
    for cond in conditions:
        left = cond[0] if cond[0].isdigit() else str(strng.count(cond[0]))
        right = cond[-1] if cond[-1].isdigit() else str(strng.count(cond[-1]))
        result.append(eval('%s%s%s' % (left, cond[1:-1], right)))
    return result


print string_evaluation('abb', ['a>b', 'b==a', 'b<=a', 'b>a', 'b!=b', 'a==1', 'b==1'])
#  [False, False, False, True, False, True, False])
