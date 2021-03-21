import os
import unittest

def count_line(file):

    fp = open(file)
    line_count = 0
    for line in fp.readlines():
        if not line.split():
            continue
        line_count += 1
    fp.close()
    return line_count

def count_file_in_path(path):
    res = []
    for root, dirs, files in os.walk(path):
        for d in dirs: #find the sub folder first
            res += count_file_in_path(root+ '//' + d)
        for f in files: #count the files in current folder
            lines = count_line(root + "//" + f)
            print(root + "//"+ f, "lines: " , lines)
            res.append(f)
            res.append(lines)
        return res



class ut(unittest.TestCase):

    def test_read_test_folder(self):
        self.assertEquals(['d', 4, 'c', 1, "a", 3, "b", 4], count_file_in_path("../test"))


if __name__ == '__main__':
    unittest.main()