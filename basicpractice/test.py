import unittest
def div(a, b):
    return a/b

class ut(unittest.TestCase):


    #@unittest.skip
    def test_input_exception(self):

        self.assertRaises(ZeroDivisionError, div(0, 0), 1, 1)
        #self.assertRaisesRegexp(ZeroDivisionError, "division by zero", 0/0)
        # self.assertEqual(False, check(input))
        self.failureException
#
if __name__ == "__main__":
    unittest.main()