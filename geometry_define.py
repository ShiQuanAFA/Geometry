#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Import """
from multiset import Multiset, FrozenMultiset

"""
Define Basic Unit
"""
point = 'A'

def segment(point_1, point_2):
    point_1, point_2 = sorted((point_1, point_2))
    return ('segment', point_1 + point_2)

def angle(point_aside_1, point_vertex, point_aside_2):
    point_aside_1, point_aside_2 = sorted((point_aside_1, point_aside_2))
    return ('angle', point_aside_1 + point_vertex + point_aside_2)

def degree(value):
    return ('degree', value)

"""
Define Complex Unit
"""
def sum_units(*args):
    this_units = Multiset()
    for each_unit in args:
        if get_unit_type(each_unit) == 'sum':
            this_units.update(get_complexunit_set(each_unit))
        else:
            this_units.add(each_unit)
    if len(this_units) == 1:
        return list(this_units)[0]
    else:
        return ('sum', FrozenMultiset(this_units))

def multiply_units(*args):
    this_units = Multiset()
    for each_unit in args:
        if get_unit_type(each_unit) == 'multiply':
            this_units.update(get_complexunit_set(each_unit))
        else:
            this_units.add(each_unit)
    if len(this_units) == 1:
        return list(this_units)[0]
    else:
        return ('multiply', FrozenMultiset(this_units))

def complex_units(complex_type, *args):
    if complex_type == 'sum':
        return sum_units(*args)
    elif complex_type == 'multiply':
        return multiply_units(*args)
    else:
        raise Exception('unknown complex type!')

"""
Define Relationship
"""
def equal(*args):
    this_equal = set()
    for each_unit in args:
        this_equal.add(each_unit)
    if len(this_equal) == 1:
        return set()
    else:
        return this_equal

"""
Get unit and relationship values
"""
def is_complex_type(this_unit):
    return get_unit_type(this_unit) in ['sum', 'multiply']

def get_unit_type(this_unit):
    try:
        return this_unit[0]
    except:
        raise Exception('unknown unit type!')

def get_unit_len(this_unit):
    if this_unit == 'no unit':
        return 0
    elif is_complex_type(this_unit):
        return len(get_complexunit_set(this_unit))
    else:
        return 1
        
def get_segment_points(this_segment_unit):
    points_str = this_segment_unit[1]
    return (points_str[0], points_str[1])

def get_angle_points(this_angle_unit):
    points_str = this_angle_unit[1]
    return {'vertex': points_str[1], 'aside': (points_str[0], points_str[2])}

def get_complexunit_set(this_complex_unit):
    return this_complex_unit[1]

def get_complexunit_except_unit(this_complex_unit, another_unit):
    this_complex_unit_type = get_unit_type(this_complex_unit)
    this_complex_unit_set = get_complexunit_set(this_complex_unit)
    if this_complex_unit_type == get_unit_type(another_unit):
        another_unit_set = get_complexunit_set(another_unit)
    else:
        another_unit_set = {another_unit}
    excepted_set = this_complex_unit_set.difference(another_unit_set)
    if len(excepted_set) >= 2:
        return (get_unit_type(this_complex_unit), excepted_set)
    elif len(excepted_set) == 1:
        return list(excepted_set)[0]
    elif len(excepted_set) == 0:
        return (get_unit_type(this_complex_unit), excepted_set)
        
def get_complexunit_inner_complexunit(this_complex_unit, another_complex_unit):
    this_complex_unit_set = get_complexunit_set(this_complex_unit)
    another_complex_unit_set = get_complexunit_set(another_complex_unit)
    inner_set = this_complex_unit_set.intersection(another_complex_unit_set)
    if len(inner_set) >= 2:
        return (get_unit_type(this_complex_unit), inner_set)
    elif len(inner_set) == 1:
        return list(inner_set)[0]
    elif len(inner_set) == 0:
        return (get_unit_type(this_complex_unit), inner_set)

def get_unit_flatten_set(this_unit, complex_type):
    if get_unit_type(this_unit) == complex_type:
        return get_complexunit_set(this_unit)
    else:
        return {this_unit}

def get_equal_except_unit(this_equal, this_unit):
    return this_equal.difference({this_unit})