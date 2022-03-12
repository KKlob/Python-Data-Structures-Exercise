def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here

    # Setup alpha_val as dictionary of values for each char in alphabet
    alphabet_lst = list("abcdefghijklmnopqrstuvwxyz")
    alpha_val = {}
    for x in range(0, len(alphabet_lst)):
        alpha_val[alphabet_lst[x]] = x + 1

    word_sum = 0
    for char in word.lower():
        word_sum += alpha_val[char]

    if word_sum % 2 == 0:
        return False
    
    return True