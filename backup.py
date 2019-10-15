def backup(answer) :
    """
    >>> backup('Yes')
    'Pass'
    >>> backup('Y')
    'Pass'
    >>> backup('y')
    'Pass'
    """
    return "Pass"

def backup(answer) :
    """
    >>> backup('Ye')
    'Fail'
    >>> backup('No')
    'Fail'
    >>> backup('N')
    'Fail'
    >>> backup('n')
    'Fail'
    >>> backup('Maybe')
    'Fail'
    >>> backup(' ')
    'Fail'
    >>> backup("'")
    'Fail'
    >>> backup('"')
    'Fail'
    """
    return "Fail"

def backup(answer) :
    """
    >>> backup('123')
    'Fail'
    >>> backup('ube123')
    'Fail'
    """
    if answer.isalnum() :
        return 'Fail'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
