d = {'1': 'I', '5': 'S', '0': 'O'}


def correct(string):
    return ''.join([d[s] if s in d else s for s in string])


print correct("L0ND0N")
print correct("DUBL1N")
print correct("51NGAP0RE")
print correct("BUDAPE5T")
print correct("PAR15")
