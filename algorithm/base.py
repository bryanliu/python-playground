import json
"""
module algorithm.base
导入方法：from algorithm.base import *  # 如果在目录里面要加上目录的名称，也就是package的名称
"""

def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def integerListToString(nums, len_of_list=None):
    """
    :param nums: array that need to convert
    :param len_of_list: lenth of arry
    :return: formatted string
    """

    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])
