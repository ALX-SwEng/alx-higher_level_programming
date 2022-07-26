#!/usr/bin/python3
"""Defines an matrix_mul function."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices
    
    Args:
        m_a (list of lists of ints/floats): the first matrix.
        m_b (list of lists of ints/floats): the second matrix.
    
    Raises:
        TypeError: if either m_a or m_b is not list or list of lists is not an integer or a float 
                    or not a rectangle
        ValueError: if either m_a or m_b is empty, or can’t be multiplied
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row_ma, list) for row_ma in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row_mb, list) for row_mb in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all ((isinstance(ele_ma, int) or isinstance(ele_ma, float)) 
                for ele_ma in [value_ma for row_ma in m_a for value_ma in row_ma]):
        raise TypeError("m_a should contain only integers or floats")
    if not all ((isinstance(ele_mb, int) or isinstance(ele_mb, float))
                for ele_mb in [value_mb for row_mb in m_b for value_mb in row_mb]):
        raise TypeError("m_b should contain only integers or floats")

    if not all (len(row_ma) == len(m_a[0]) for row_ma in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all (len(row_mb) == len(m_b[0]) for row_mb in m_b):
        raise TypeError("each row of m_a must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_Matrix = []
    for row_a in m_a:
        new_row = []
        for c in range (len(m_b[0])):
            product = 0
            for r in range(len(row_a)):
                product += (row_a[r] * m_b[r][c])
            new_row.append(product)
        new_Matrix.append(new_row)

    return (new_Matrix)