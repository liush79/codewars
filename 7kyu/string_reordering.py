def cmp_item(a, b):
    if int(a.keys()[0]) > int(b.keys()[0]):
        return 1
    return 0 if int(a.keys()[0]) == int(b.keys()[0]) else -1


def sentence(List):
    List.sort(cmp=cmp_item)
    return ' '.join([item.values()[0] for item in List])


List = [
        {'4': 'dog' }, {'2': 'took'}, {'3': 'his'},
        {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
       ]

print sentence(List)    # 'Vatsan took his dog for a spin')