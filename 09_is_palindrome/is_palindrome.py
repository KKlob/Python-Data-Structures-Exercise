def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    phrase = phrase.lower()
    no_space_lst = phrase.split(" ")
    og_phrase = "".join(no_space_lst)
    og_lst = list(og_phrase)
    rewind = og_lst.copy()
    rewind.reverse()
    if og_lst == rewind:
        return True
    else:
        return False
