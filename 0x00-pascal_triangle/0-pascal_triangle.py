#!/usr/bin/python3
""" Paschal Triangle Interview """


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to row n.

    Args:
        n (int): Number of rows in the Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle up to row n.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
