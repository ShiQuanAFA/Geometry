#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from geometry_initial import Graph
from geometry_start import math_str_to_equal

t = Graph('中国联赛第一题')
t.add_point('A', -2.03, 6.83)
t.add_point('B', 5.88, 6.71)
t.add_point('C', 10.27, 0.78)
t.add_point('D', 2.17, -1.08)
t.add_point('E', 2.01, 4.84)
t.add_point('F', 1.9, 6.77)
t.add_point('G', 8.08, 3.74)

condition_str_list = [
                      '∠ABC+∠ADC=180°', 
                      '∠ABC+∠AMC=180°'
                      ]
for this_condition_str in condition_str_list:
    if '∠' in this_condition_str:
        t.add_equal(math_str_to_equal(this_condition_str), 'angle')
    else:
        t.add_equal(math_str_to_equal(this_condition_str), 'segment')

deduce_config={'angle_complex_max_len': 2, 
               'pre_check_triangle': False}

t.deduce(0, deduce_config)
t.deduce(1, deduce_config)

t.display()


## deep equal
#{
#FrozenMultiset(['b' , 'a'])
#} == {
#FrozenMultiset(['a' , 'b'])
#}
## value equal
#FrozenMultiset(
#FrozenMultiset(['b' , 'a'])
#) == FrozenMultiset(
#FrozenMultiset(['a' , 'b'])
#)