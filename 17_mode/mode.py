def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_dic = {}
    set_nums = set(nums)
    for num in set_nums:
        num_dic[num] = nums.count(num)
    
    num_dic_keys = list(num_dic.keys())
    high_count_key = num_dic_keys[0]

    for key in num_dic.keys():
        if num_dic[key] > num_dic[high_count_key]:
            high_count_key = key

    return high_count_key
        