def pig_it(text):
    result = ''
    split_text = text.split(' ')
    for s_text in split_text:
        if s_text[0].isalpha():
            result += '%s%say ' % (s_text[1:], s_text[0])
        else:
            result += '%s ' % s_text
    return result[:-1]


print pig_it('Pig latin is cool')       # 'igPay atinlay siay oolcay'
print pig_it('This is my string')       # 'hisTay siay ymay tringsay'
