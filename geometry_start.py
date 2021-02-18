#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Import """
from geometry_define import segment, angle, degree
from geometry_define import sum_units, multiply_units
from geometry_initial import Graph

""" Translate math str """
def math_str_to_unit(this_unit_math_str):
    """ judge unit type"""
    if ('+' not in this_unit_math_str) and ('*' not in this_unit_math_str):
        if '°' in this_unit_math_str:
            return degree(int(this_unit_math_str[:-1]))
        elif '∠' in this_unit_math_str:
            return angle(this_unit_math_str[1], this_unit_math_str[2], this_unit_math_str[3])
        else:
            return segment(this_unit_math_str[0], this_unit_math_str[1])
    """ complex split """
    split_sum_list = []
    sub_sum = ''
    for sub_sum_part in this_unit_math_str.split('+'):
        sub_sum = sub_sum + sub_sum_part + '+'
        if sub_sum.count('(') - sub_sum.count(')') == 0:
            split_sum_list.append(sub_sum[:-1])
            sub_sum = ''
    result_unit = sum_units()
    for sub_sum in split_sum_list:
        split_multiply_list = []
        sub_multiply = ''
        for sub_multiply_part in sub_sum.split('*'):
            sub_multiply = sub_multiply + sub_multiply_part + '*'
            if sub_multiply.count('(') - sub_multiply.count(')') == 0:
                if sub_multiply[0] == '(' and sub_multiply[-2] == ')':
                    sub_multiply = sub_multiply[1:-2]
                else:
                    sub_multiply = sub_multiply[:-1]
                split_multiply_list.append(sub_multiply)
                sub_multiply = ''
        result_sub_sum_unit = multiply_units()
        for sub_multiply in split_multiply_list:
            result_sub_sum_unit = multiply_units(result_sub_sum_unit, math_str_to_unit(sub_multiply))
        result_unit = sum_units(result_unit, result_sub_sum_unit)
    return result_unit
    
def math_str_to_equal(this_equal_math_str):
    result_equal = set()
    for each_unit_str in this_equal_math_str.split('='):
        result_equal.add(math_str_to_unit(each_unit_str))
    return result_equal

""" Start Program """
def start(name, point_list, condition_str_list, need_prove_str, 
          deduce_num=5, auxiliary_num=2, 
          deduce_config={'angle_complex_max_len': 3, 
                         'pre_check_triangle': False}):
    """ input info """
    this_problem = Graph(name)
    for this_point_info in point_list:
        this_problem.add_point(this_point_info[0], this_point_info[1], this_point_info[2])
    for this_condition_str in condition_str_list:
        if '∠' in this_condition_str:
            this_problem.add_equal(math_str_to_equal(this_condition_str), 'angle')
        else:
            this_problem.add_equal(math_str_to_equal(this_condition_str), 'segment')
    print('Graph info input success!')
    """ need prove """
    has_proved = False
    need_prove_equal = math_str_to_equal(need_prove_str)
    if '∠' in need_prove_str:
        need_prove_type = 'angle'
    else:
        need_prove_type = 'segment'
    """ deduce """
    for deduce_no in range(deduce_num):
        this_problem.deduce(deduce_no, deduce_config)
        if this_problem.query(need_prove_equal, need_prove_type):
            has_proved = True
            print('Has proved!!!')
            break
    """ auxiliary deduce """
    if not has_proved:
        
        return 0
    return this_problem, has_proved

name = '中国联赛第一题'
point_list = [
              ['A', -2.03, 6.83], 
              ['B', 5.88, 6.71], 
              ['C', 10.27, 0.78]
              ]
condition_str_list = [
                      'AB=AC', 
                      '∠ABC+∠ADC=180°', 
                      '∠ABC+∠AMC=180°'
                      ]
need_prove_str = 'CM=CN'
t, ok = start(name, point_list, condition_str_list, need_prove_str, 
              deduce_num=3, auxiliary_num=1, 
              deduce_config={'angle_complex_max_len': 3, 
                             'pre_check_triangle': False})