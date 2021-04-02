import os
import unittest
import re
import GetContent

class TestGetContentPy(unittest.TestCase):

    path = ".\\GetContentPyTest.txt"
    # Create File for test 
    def setUp(self):
        file = open(self.path, "w")
        for i in range(20):
            file.write("This is line %d\n" % (i+1))
        file.close()

    def test_filePath_is_folder(self):
        with self.assertRaises(Exception):
            GetContent.GetContentPy(".\\") ,

    def test_both_tail_totalCount_set(self):
        with self.assertRaises(Exception):
            GetContent.GetContentPy(self.path, TotalCount=10, Tail=10)

    def test_read_from_tail(self):
        result = GetContent.GetContentPy(self.path, Tail=4)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], "This is line 17\n")
        self.assertEqual(result[3], "This is line 20\n")

    def test_read_from_start(self):
        result = GetContent.GetContentPy(self.path, TotalCount=4)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], "This is line 1\n")
        self.assertEqual(result[3], "This is line 4\n")

    def test_totalcount_exceeded(self):
        result = GetContent.GetContentPy(self.path, TotalCount=9999)
        self.assertEqual(len(result), 20)
        self.assertEqual(result[0], "This is line 1\n")
        self.assertEqual(result[19], "This is line 20\n")

    def test_tail_exceeded(self):
        result = GetContent.GetContentPy(self.path, Tail=9999)
        self.assertEqual(len(result), 20)
        self.assertEqual(result[0], "This is line 1\n")
        self.assertEqual(result[19], "This is line 20\n")

    def test_readcount_over_totalcount(self):
        result = GetContent.GetContentPy(self.path, TotalCount=5, ReadCount=15)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], "This is line 1\n")
        self.assertEqual(result[4], "This is line 5\n")

    def test_readcount_zero(self):
        # if readcount = 0
        result = GetContent.GetContentPy(self.path, TotalCount=3, ReadCount=0)
        #print(result)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "This is line 1\n")
        self.assertEqual(result[2], "This is line 3\n")

    def tearDown(self):
        os.remove(self.path)

if __name__ == "__main__":
    unittest.main()