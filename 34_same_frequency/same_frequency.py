def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1_set = set(str(num1))
    num2_set = set(str(num2))

    num1_dic = {}
    num2_dic = {}

    for item in num1_set:
        num1_dic[item] = str(num1).count(str(item))

    for item in num2_set:
        num2_dic[item] = str(num2).count(str(item))

    if num1_dic == num2_dic:
        return True
    
    return False
