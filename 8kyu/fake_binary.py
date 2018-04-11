def fake_bin(x):
    return ''.join(['0' if int(y) < 5 else '1' for y in x])


print fake_bin("45385593107843568")
