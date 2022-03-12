def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    lst = phrase.split(" ")
    new_lst = []
    for item in lst:
        new_item = item.lower().capitalize()
        new_lst.append(new_item)
    
    return " ".join(new_lst)