from common import Test as test

#
# When we submit to code-wars, We don't need define this dictionary. It's already defined.
#
MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
              '....': 'H',  '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
              '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
              '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
              '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
              '-.-.--': '!', '.-.-.-': '.',
              '...---...': 'SOS'}


def decodeMorse(morse_code):
    return ''.join([MORSE_CODE[m] if m != '' else ' ' for m in morse_code.strip().split(' ')]).replace('  ', ' ')


def test_and_print(got, expected):
    if got == expected:
        test.expect(True)
    else:
        print "<pre style='display:inline'>Got {}, expected {}</pre>".format(got, expected)
        test.expect(False)


test.describe("Example from description")
test_and_print(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
test_and_print(decodeMorse(' . '), 'E')
