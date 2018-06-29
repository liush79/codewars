from common import Test


# def reverse_fun(n):
#     res = list(n)
#     len_n = len(n) / 2
#     for i in range(0, len_n):
#         res[i * 2] = n[-(i+1)]
#         res[i * 2 + 1] = n[i]
#     if len(n) % 2 > 0:
#         res[-1] = n[len_n]
#     return ''.join(res)

# def reverse_fun(n):
#     len_n = len(n) / 2
#     res = ''
#     for i in range(0, len_n):
#         res += n[-(i+1)] + n[i]
#     if len(n) % 2 > 0:
#         res += n[len_n]
#     return res

# def reverse_fun(n):
#     res = [n[-(i + 1)] + n[i] for i in range(0, len(n) / 2)]
#     if len(n) % 2 > 0:
#         res += n[len(n) / 2]
#     return ''.join(res)

def reverse_fun(n):
    n = list(n)
    len_n = len(n)
    for i in range(0, len_n - 1):
        for j in range(i, i + (len_n - i) / 2):
            n[j], n[-((j-i)+1)] = n[-((j-i)+1)], n[j]
    return ''.join(n)

Test.describe("reverse_fun example testcases")
Test.it("should work for even length")
Test.assert_equals(reverse_fun('012345'), '504132')
Test.assert_equals(reverse_fun('0123456'), '6051423')
Test.it("should work for odd length too")
Test.assert_equals(reverse_fun('3689aefghjlpqrtuyz01234678cefgijnopqrsvwy0124579abdgijlsxz1234568bfhkostuy01249cfghjmnsvz01478bhjlmoruwx04679aeghmoswxy1346acdehirsuwx1234689bcefhjlnopqstvwxyz02568abdefghklnptuxz237bdfghkmnoprvyz0125789bdegoqsuvxz47abdfijklmpqrstuvwxy126789abcefghikmnotwyz489blnrux456789acdhijklmnstvwyz123679abdhiknrsuwyz168aekmnoprtxyz0123469adhiklnsuvy12456789adgmnopqstuvwxy01567bdhlnpqtwxy013467bdghnpsuvwxy13456bcdghijlqrsz03478abefhmnpqrsuvwx01245789ceiklnqrsvwx34789ceklmqstuv12359acdfilnopswxz025678abceghijkmnp'), 'p3n6m8k9jaiehfggehcjblap8q7r6t5u2y0zz0x1w2s3p4o6n7l8icfedfcgai9j5n3o2p1qvrustvswqym0l1k2e4c597897a4b3dxgwivjslrsqxnzl1k2i3e4c596887b5f4h2k1o0sxtwuvyu0s1r2q4p9ncmfhgfhejbman8s7v4z3001z4s7r8qblhjjilhmgodrcubw6x50443617y9xawevguhsmponshwgxdyb17364463a1c0dyexhwitrqspunwlxh1d2b3746658190bycxewfvhujtlsnqoppoqnsmtgvdwax9y8z70625546281aybvduesfnglhkkilhndpat9u6x4z3223170bzdyfxgthrkpmonnompkrevay8z6011z2y5w7u8s9rbndkeighodqbsau9v7x6z34271azbydwfvitjsknlmmlpkqjrishtducvaw9x8y71625647x8u9ranblcbe9f8g4hziykwmtno')
Test.assert_equals(reverse_fun('3689aefghjlpqrtuyz01234678cefgijnopqrsvwy0124579abdgijlsxz1234568bfhkostuy01249cfghjmnsvz01478bhjlmoruwx04679aeghmoswxy1346acdehirsuwx1234689bcefhjlnopqstvwxyz02568abdefghklnptuxz237bdfghkmnoprvyz0125789bdegoqsuvxz47abdfijklmpqrstuvwxy126789abcefghikmnotwyz489blnrux456789acdhijklmnstvwyz123679abdhiknrsuwyz168aekmnoprtxyz0123469adhiklnsuvy12456789adgmnopqstuvwxy01567bdhlnpqtwxy013467bdghnpsuvwxy13456bcdghijlqrsz03478abefhmnpqrsuvwx01245789ceiklnqrsvwx34789ceklmqstuv12359acdfilnopswxz025678abceghijkmnp'), 'p3n6m8k9jaiehfggehcjblap8q7r6t5u2y0zz0x1w2s3p4o6n7l8icfedfcgai9j5n3o2p1qvrustvswqym0l1k2e4c597897a4b3dxgwivjslrsqxnzl1k2i3e4c596887b5f4h2k1o0sxtwuvyu0s1r2q4p9ncmfhgfhejbman8s7v4z3001z4s7r8qblhjjilhmgodrcubw6x50443617y9xawevguhsmponshwgxdyb17364463a1c0dyexhwitrqspunwlxh1d2b3746658190bycxewfvhujtlsnqoppoqnsmtgvdwax9y8z70625546281aybvduesfnglhkkilhndpat9u6x4z3223170bzdyfxgthrkpmonnompkrevay8z6011z2y5w7u8s9rbndkeighodqbsau9v7x6z34271azbydwfvitjsknlmmlpkqjrishtducvaw9x8y71625647x8u9ranblcbe9f8g4hziykwmtno')
Test.assert_equals(reverse_fun('3689aefghjlpqrtuyz01234678cefgijnopqrsvwy0124579abdgijlsxz1234568bfhkostuy01249cfghjmnsvz01478bhjlmoruwx04679aeghmoswxy1346acdehirsuwx1234689bcefhjlnopqstvwxyz02568abdefghklnptuxz237bdfghkmnoprvyz0125789bdegoqsuvxz47abdfijklmpqrstuvwxy126789abcefghikmnotwyz489blnrux456789acdhijklmnstvwyz123679abdhiknrsuwyz168aekmnoprtxyz0123469adhiklnsuvy12456789adgmnopqstuvwxy01567bdhlnpqtwxy013467bdghnpsuvwxy13456bcdghijlqrsz03478abefhmnpqrsuvwx01245789ceiklnqrsvwx34789ceklmqstuv12359acdfilnopswxz025678abceghijkmnp'), 'p3n6m8k9jaiehfggehcjblap8q7r6t5u2y0zz0x1w2s3p4o6n7l8icfedfcgai9j5n3o2p1qvrustvswqym0l1k2e4c597897a4b3dxgwivjslrsqxnzl1k2i3e4c596887b5f4h2k1o0sxtwuvyu0s1r2q4p9ncmfhgfhejbman8s7v4z3001z4s7r8qblhjjilhmgodrcubw6x50443617y9xawevguhsmponshwgxdyb17364463a1c0dyexhwitrqspunwlxh1d2b3746658190bycxewfvhujtlsnqoppoqnsmtgvdwax9y8z70625546281aybvduesfnglhkkilhndpat9u6x4z3223170bzdyfxgthrkpmonnompkrevay8z6011z2y5w7u8s9rbndkeighodqbsau9v7x6z34271azbydwfvitjsknlmmlpkqjrishtducvaw9x8y71625647x8u9ranblcbe9f8g4hziykwmtno')
Test.assert_equals(reverse_fun('3689aefghjlpqrtuyz01234678cefgijnopqrsvwy0124579abdgijlsxz1234568bfhkostuy01249cfghjmnsvz01478bhjlmoruwx04679aeghmoswxy1346acdehirsuwx1234689bcefhjlnopqstvwxyz02568abdefghklnptuxz237bdfghkmnoprvyz0125789bdegoqsuvxz47abdfijklmpqrstuvwxy126789abcefghikmnotwyz489blnrux456789acdhijklmnstvwyz123679abdhiknrsuwyz168aekmnoprtxyz0123469adhiklnsuvy12456789adgmnopqstuvwxy01567bdhlnpqtwxy013467bdghnpsuvwxy13456bcdghijlqrsz03478abefhmnpqrsuvwx01245789ceiklnqrsvwx34789ceklmqstuv12359acdfilnopswxz025678abceghijkmnp'), 'p3n6m8k9jaiehfggehcjblap8q7r6t5u2y0zz0x1w2s3p4o6n7l8icfedfcgai9j5n3o2p1qvrustvswqym0l1k2e4c597897a4b3dxgwivjslrsqxnzl1k2i3e4c596887b5f4h2k1o0sxtwuvyu0s1r2q4p9ncmfhgfhejbman8s7v4z3001z4s7r8qblhjjilhmgodrcubw6x50443617y9xawevguhsmponshwgxdyb17364463a1c0dyexhwitrqspunwlxh1d2b3746658190bycxewfvhujtlsnqoppoqnsmtgvdwax9y8z70625546281aybvduesfnglhkkilhndpat9u6x4z3223170bzdyfxgthrkpmonnompkrevay8z6011z2y5w7u8s9rbndkeighodqbsau9v7x6z34271azbydwfvitjsknlmmlpkqjrishtducvaw9x8y71625647x8u9ranblcbe9f8g4hziykwmtno')
Test.assert_equals(reverse_fun('3689aefghjlpqrtuyz01234678cefgijnopqrsvwy0124579abdgijlsxz1234568bfhkostuy01249cfghjmnsvz01478bhjlmoruwx04679aeghmoswxy1346acdehirsuwx1234689bcefhjlnopqstvwxyz02568abdefghklnptuxz237bdfghkmnoprvyz0125789bdegoqsuvxz47abdfijklmpqrstuvwxy126789abcefghikmnotwyz489blnrux456789acdhijklmnstvwyz123679abdhiknrsuwyz168aekmnoprtxyz0123469adhiklnsuvy12456789adgmnopqstuvwxy01567bdhlnpqtwxy013467bdghnpsuvwxy13456bcdghijlqrsz03478abefhmnpqrsuvwx01245789ceiklnqrsvwx34789ceklmqstuv12359acdfilnopswxz025678abceghijkmnp'), 'p3n6m8k9jaiehfggehcjblap8q7r6t5u2y0zz0x1w2s3p4o6n7l8icfedfcgai9j5n3o2p1qvrustvswqym0l1k2e4c597897a4b3dxgwivjslrsqxnzl1k2i3e4c596887b5f4h2k1o0sxtwuvyu0s1r2q4p9ncmfhgfhejbman8s7v4z3001z4s7r8qblhjjilhmgodrcubw6x50443617y9xawevguhsmponshwgxdyb17364463a1c0dyexhwitrqspunwlxh1d2b3746658190bycxewfvhujtlsnqoppoqnsmtgvdwax9y8z70625546281aybvduesfnglhkkilhndpat9u6x4z3223170bzdyfxgthrkpmonnompkrevay8z6011z2y5w7u8s9rbndkeighodqbsau9v7x6z34271azbydwfvitjsknlmmlpkqjrishtducvaw9x8y71625647x8u9ranblcbe9f8g4hziykwmtno')
Test.assert_equals(reverse_fun('jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'
                               'jointhedarksidejointhedarksidejointhedarksidejointhedarksidejointhedarkside'),
                   'ejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaeddeahrtknsiiodjeejdoiisnktrhaed')
