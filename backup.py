import re

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
    """
    if answer == 'Ye' or answer == 'No' or answer == 'N' or answer == 'n' :
        return "Fail"
    return "Pass"

# def backup(answer) :
#     """

#     >>> backup('Maybe')
#     'Fail'
#     >>> backup(' ')
#     'Fail'
#     >>> backup("'")
#     'Fail'
#     >>> backup('"')
#     'Fail'
#     """
#     return "Fail"
#
# def backup(answer) :
#     """
#     >>> backup('123')
#     'Fail'
#     >>> backup('ube123')
#     'Fail'
#     """
#     if answer.isalnum() :
#         return 'Fail'

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
