from unittest import TestCase


class CommonTest(TestCase):
    def runTest(self):
        pass

    def assert_equals(self, a, b):
        return self.assertEqual(a, b)

    def describe(self, desc):
        print (desc)

    def expect(self, result, msg=None):
        if msg:
            print (msg)
        return self.assertTrue(result)


Test = CommonTest()
