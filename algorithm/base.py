import json


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
