def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    parens_count = 0
    quote_count = 0

    for char in str(parens):
        if char == "(":
            parens_count += 1

        elif char == ")":
            parens_count -= 1

    first_paren = parens.find('"')

    if parens_count == 0 and not parens[first_paren + 1] == ")":
        return True
    
    return False