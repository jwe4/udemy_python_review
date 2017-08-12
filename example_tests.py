import unittest


def ret2():
    return 2


class FooTest(unittest.TestCase):
    def test2(self):
        self.assertTrue(2 == ret2())

# needs to start with string 'test'
    def testDivide(self):
        a = 1
        b = 0
        with self.assertRaises(ZeroDivisionError):
            a/b
