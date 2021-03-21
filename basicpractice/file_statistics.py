import os
import unittest

'''
循环目录下的文件，统计每个文件的行数，并且不统计空行。可以参考：
https://blog.csdn.net/baidu_35692628/article/details/106960164?utm_medium=distribute.pc_relevant_download.none-task-blog-baidujs-3.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-baidujs-3.nonecase
'''


def count_line(file):

    line_count = 0
    # way 1: open and close files
    # fp = open(file)
    # for line in fp.readlines():
    #     if not line.split():
    #         continue
    #     line_count += 1
    # fp.close()
    with open(file, 'rb') as f:
        #way 2: open and readlines
        # for line in f.readlines():
        #     if not line.split():
        #         continue
        #     line_count += 1
        #way 3: open and readline
        while line:=f.readline():
            if not line.split():
                continue
            line_count += 1
        f.close()


    return line_count


def count_file_in_path(path):
    res = {}
    for root, dirs, files in os.walk(path):
        for d in dirs:  # find the sub folder first
            res.update(count_file_in_path(root + '//' + d))
        for f in files:  # count the files in current folder
            lines = count_line(root + "//" + f)
            # windowns 可以用 \ 或者 /的分隔符， 但是linux只能用 /
            print(root + "//" + f, "lines: ", lines)
            res[f] = lines
        return res


class ut(unittest.TestCase):

    def test_read_test_folder(self):
        self.assertEquals({'d': 4, 'c': 1, "a": 3, "b": 4, 'vcruntime140_1.dll': 165}, count_file_in_path("../test"))


if __name__ == '__main__':
    unittest.main()
