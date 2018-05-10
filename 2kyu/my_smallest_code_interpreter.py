def _find_pair(code):
    cnt = 0
    for i in range(0, len(code)):
        if code[i] == '[':
            cnt += 1
        elif code[i] == ']':
            cnt -= 1
        if cnt == 0:
            return i


def process(code, input, ptrs, idx):
    res = ''
    i = 0
    while i < len(code):
        if code[i] == ',':
            input_pop = ord(input.pop(0))
            if input_pop in (255, 0):
                break
            ptrs[idx] = input_pop
        elif code[i] == '[' and i != 0:
            e = _find_pair(code[i:])
            if ptrs[idx] > 0:
                sub, idx = process(code[i:i+e+1], input, ptrs, idx)
                res += sub
            i = i + e
        elif code[i] == ']':
            i = 0
            if ptrs[idx] == 0:
                break
        elif code[i] == '.':
            res += chr(ptrs[idx])
        elif code[i] == '+':
            ptrs[idx] = ptrs[idx] + 1 if ptrs[idx] < 255 else 0
        elif code[i] == '-':
            ptrs[idx] = ptrs[idx] - 1 if ptrs[idx] > 0 else 255
        elif code[i] == '>':
            idx += 1
        elif code[i] == '<':
            idx -= 1
        i += 1
    return res, idx


def brain_luck(code, input):
    ptrs = [0] * 100
    return process(code, list(input), ptrs, 0)[0]


# # Echo until byte(255) encountered
# print brain_luck(',+[-.,+]', 'Codewars' + chr(255))
#
# # Echo until byte(0) encountered
# print brain_luck(',[.[-],]', 'Codewars' + chr(0))
#
# print brain_luck('++++++++++'
#                  '[>+++++++>++++++++++>+++>+<<<<-]'
#                  '>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.', '')
# print brain_luck('>,>+++[-<-[.>[-]<+.>]<.>]', '1')
# Two numbers multiplier
# print brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9))    # chr(72)
# times table
# print brain_luck('>+++++++[<++++++>-]+>++++++[<++++++++++>-]++++++++++>++>++++++++>>+++++[<++++++++++>-]'
#                  '>+++++++++>>++++++[<++++++++>-]<<<<<[>>>[<+>->+<<<.<<<<<.>>>>>>>>.<<<<<<<.>>[->>>[->>>+>+<<<<]'
#                  '>>>>[-<<<<+>>>>]>+<<<<<<<<]>>>>>>>>[-<<<<<<<<+>>>>>>>>]>+<++++++++++<<'
#                  '[->+>-[>]>[<++++++++++<---------->>>>>+<]<<<<<]++++++[>++++++++<-]>>>>>>'
#                  '[<++++++[>++++++++<-]>.[-]]<<<[-]<[-]<.[-]<<<<<<<<.>>>>>]<[->+>-<<]<+<-<+>]', '')
# print brain_luck(',>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]', '1')
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55