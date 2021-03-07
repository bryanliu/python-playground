def divide_field_for_max_available_squire(width, height):
    """

    :type width: object
    """
    print 'start ', width, height
    large, small = width, height

    if height > width:
        large, small = height, width

    # print large, small

    if small > 0:
        if large / float(small)%2 == 0:
            return small
        else:
            # print large - small, small

            return divide_field_for_max_available_squire(large - small*(large/small), small)
    else:
        return None


width = 640
heigh = 400

print divide_field_for_max_available_squire(width, heigh)
print divide_field_for_max_available_squire(300, 105)
print divide_field_for_max_available_squire(123456, 1400)
