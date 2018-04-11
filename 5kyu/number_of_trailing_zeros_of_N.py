def zeros(n):
    return 0 if n < 1 else int(n / 5) + zeros(n / 5)


print zeros(10)
print zeros(100)
print zeros(1000)
print zeros(10000)
