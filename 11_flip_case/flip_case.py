def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    swap_phrase = ""
    if to_swap.islower():
        for char in phrase:
            if char.lower() == to_swap:
                swap_phrase = swap_phrase + char.swapcase()
            else:
                swap_phrase = swap_phrase + char

    elif to_swap.isupper():
        for char in phrase:
            if char.upper() == to_swap:
                swap_phrase = swap_phrase + char.swapcase()
            else:
                swap_phrase = swap_phrase + char

    return swap_phrase
