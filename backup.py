def backup(answer) :
    """
    >>> backup('Yes')
    'Pass'
    >>> backup('Y')
    'Pass'
    >>> backup('y')
    'Pass'
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
    >>> backup('123')
    'Fail'
    """
<<<<<<< HEAD
    if answer == 'Yes' or answer == 'Y' or answer == 'y' :
        return "Pass"
    return "Fail"


# def backup(answer) :
#     """
#     >>> backup('123')
#     'Fail'
#     >>> backup('ube 123')
#     'Fail'
#     """
#     x = re.search("\s", answer)
#
#     print(x)
#
# backup("The rain in Spain")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
=======
    if answer == 'Ye' or answer == 'No' or answer == 'N' or answer == 'n' \
         or answer == 'Maybe' or answer == ' ' or answer == '"' or answer =="'" \
         or answer.isnumeric() :
        return "Fail"
    return "Pass"
>>>>>>> 230a139c81ccefd8f5c6bffa0753e9502bf47c1d
