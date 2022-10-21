#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if (not list_of_integers):
        return None

    if (len(list_of_integers) <= 2):
        return max(list_of_integers)

    peak = None
    if (list_of_integers[0] >= list_of_integers[1]):
        peak = list_of_integers[0]
    if (list_of_integers[-1] >= list_of_integers[-2]):
        peak = list_of_integers[-1]
    if (peak):
        return peak

    i = 1
    while (i < len(list_of_integers) - 1):
        if (list_of_integers[i] >= list_of_integers[i + 1] and
                list_of_integers[i] >= list_of_integers[i - 1]):
            return list_of_integers[i]
        else:
            i += 1
    return peak