from unittest import TestCase


class CommonTest(TestCase):
    def runTest(self):
        pass

    def assert_equals(self, a, b):
        return self.assertEqual(a, b)


Test = CommonTest()
