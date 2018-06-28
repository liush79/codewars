from common import Test

def zero(arg=None): return int(eval('0' + arg)) if arg else '0'
def one(arg=None): return int(eval('1' + arg)) if arg else '1'
def two(arg=None): return int(eval('2' + arg)) if arg else '2'
def three(arg=None): return int(eval('3' + arg)) if arg else '3'
def four(arg=None): return int(eval('4' + arg)) if arg else '4'
def five(arg=None): return int(eval('5' + arg)) if arg else '5'
def six(arg=None): return int(eval('6' + arg)) if arg else '6'
def seven(arg=None): return int(eval('7' + arg)) if arg else '7'
def eight(arg=None): return int(eval('8' + arg)) if arg else '8'
def nine(arg=None): return int(eval('9' + arg)) if arg else '9'

def plus(arg): return '+' + arg
def minus(arg): return '-' + arg
def times(arg): return '*' + arg
def divided_by(arg): return '/' + arg

Test.describe('Basic Tests')
Test.assert_equals(seven(times(five())), 35)
Test.assert_equals(four(plus(nine())), 13)
Test.assert_equals(eight(minus(three())), 5)
Test.assert_equals(six(divided_by(two())), 3)
