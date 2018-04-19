base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def to_base_64(string):
    result = []
    add_zeros = 0
    if len(string) % 3 > 0:
        add_zeros = 3 - len(string) % 3
        for _ in range(0, add_zeros):
            string += '\0'
    for i in range(0, len(string), 3):
        s = string[i:i + 3]
        bits = str(bin(ord(s[0])))[2:].zfill(8) + str(bin(ord(s[1])))[2:].zfill(8) + str(bin(ord(s[2])))[2:].zfill(8)
        result += [base64[int(bits[j * 6:j * 6 + 6], 2)] for j in range(0, 4)]

    for _ in range(0, add_zeros):
        del result[-1]
    return ''.join(result)

def from_base_64(string):
    result = []
    if len(string) % 4 > 0:
        add_zeros = 4 - len(string) % 4
        for _ in range(0, add_zeros):
            string += '\0'
    for i in range(0, len(string), 4):
        s = string[i:i + 4]
        s = s.replace('\0', 'A')
        bits = str(bin(base64.index(s[0])))[2:].zfill(6) + str(bin(base64.index(s[1])))[2:].zfill(6) + str(bin(base64.index(s[2])))[2:].zfill(6) + str(bin(base64.index(s[3])))[2:].zfill(6)
        result += [chr(int(bits[j:j + 8], 2)) for j in range(0, 24, 8)]
    while True:
        if result[-1] != '\0':
            break
        del result[-1]
    return ''.join(result)


tests = [['uTrrd1YCXTXTEb8mseFG83QQ+NLQR', 'dVRycmQxWUNYVFhURWI4bXNlRkc4M1FRK05MUVI'],
         ["this is a string!!", "dGhpcyBpcyBhIHN0cmluZyEh"],
         ["this is a test!","dGhpcyBpcyBhIHRlc3Qh"],
         ["now is the time for all good men to come to the aid of their country.","bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
         ["1234567890  ", "MTIzNDU2Nzg5MCAg"],
         ["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
         ["the quick brown fox jumps over the white fence. ","dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
         ["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4","ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
         ["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna","VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
         ["TVRJek5EVTJOemc1TUNBZyAg","VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"]
         ]

for test in tests:
    result = to_base_64(test[0])
    print result
    print from_base_64(result)
