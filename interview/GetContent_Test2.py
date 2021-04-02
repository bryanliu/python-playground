import os
import unittest
import re
import GetContent

class TestGetContentPy(unittest.TestCase):

    path = ".\\GetContentPyTest1.txt"
    # Create File for test 
    def setUp(self):
        file = open(self.path, "w")
        for i in range(7):
            file.write("This is line %d\n" % (i+1))
        file.close()


    def test_readcount_over_totalcount(self):
        result = GetContent.GetContentPy(self.path, TotalCount=3, ReadCount=0)
        print(result)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "This is line 1\n")
        self.assertEqual(result[2], "This is line 3\n")

    def tearDown(self):
        os.remove(self.path)

if __name__ == "__main__":

    unittest.main()