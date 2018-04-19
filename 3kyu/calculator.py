class Calculator(object):
    def evaluate(self, string):
        res = eval(string)
        return float('%f' % res) if isinstance(res, float) else res


print Calculator().evaluate("2 / 2 + 3 * 4 - 6")
str = "1.1 * 2.2 * 3.3"
print Calculator().evaluate(str)
print Calculator().evaluate(str) == 7.986
