def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    s_vowels = []
    vowels = "aeiou"

    for char in s:
        for vow in vowels:
            if vow == char.lower():
                s_vowels.append(char)

    s_lst = list(s)            

    for x in range(0,len(s)):
        for vow in vowels:
            if vow == s_lst[x].lower():
                s_lst[x] = s_vowels.pop(-1)
                break
                
    return "".join(s_lst)