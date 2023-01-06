#!/usr/bin/python3
"""
Moule 100-matrix_mul
Contain method that does matrix multiplication
Requires the same size lits/rows of matrix
"""


def matrix_mul(m_a, m_b):
    """Returns multiplication of matrix"""
    message1 = "m_a should contain only integers or floats"
    message2 = "m_b should contain only integers or floats"

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    samelen = len(m_a[0])
    for la_inner in m_a:
        if type(la_inner) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(la_inner) == 0:
            raise ValueError("m_a can't be empty")
        if len(la_inner) != samelen:
            raise TypeError("each row of m_a must be of the same size")
        for element in la_inner:
            if type(element) is not int and type(element) is not float:
                raise TypeError(message1)
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    samelen = len(m_b[0])
    for lb_inner in m_b:
        if type(lb_inner) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(lb_inner) == 0:
            raise ValueError("m_b can't be empty")
        if len(lb_inner) != samelen:
            raise TypeError("each row of m_b must be of the same size")
        for element in lb_inner:
            if type(element) is not int and type(element) is not float:
                raise TypeError(message2)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    outer_list = []
    for l_row in range(len(m_a)):
        inner_list = []
        for k in range(len(m_b[0])):
            sum = 0
            for l_col in range(len(m_b[0])):
                sum += m_a[l_row][l_col] * m_b[l_col][k]
            inner_list.append(sum)
        outer_list.append(inner_list)
    return outer_list
