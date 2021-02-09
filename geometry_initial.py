#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Import """
from geometry_define import segment, angle, degree
from geometry_define import sum_units, multiply_units, complex_units, equal
from geometry_define import get_unit_type, get_unit_len, is_complex_type
from geometry_define import get_complexunit_set
from geometry_define import get_complexunit_except_unit, get_complexunit_inner_complexunit
from geometry_define import get_unit_flatten_set
from geometry_define import get_equal_except_unit
from geometry_formula import is_isosceles, is_congruent
from itertools import combinations

"""
Define Entire Graph
"""
class Graph:
    
    def __init__(self, name):
        self.name = name
        self.points = {}
        """ Graph Known Conditions """
        self.angle_values = {}
        self.segment_equals = []
        self.angle_equals = []
        
    """ Basic Fuction """
    def add_point(self, point_name, point_location_x, point_location_y):
        self.points[point_name] = {'location_x': point_location_x, 
                                   'location_y': point_location_y}
    
    def add_angle_value(self, this_angle_unit, this_value):
        self.angle_values[this_angle_unit] = this_value
    
    def add_equal(self, this_equal, equal_type):
        
        def check_and_add(this_equal, equals_list):
            already_in = False
            """ repeat in """
            for each_equal in equals_list:
                if this_equal.issubset(each_equal):
                    already_in = True
                    break
            """ need merge """
            if not already_in:
                original_equals_list = equals_list.copy()
                need_merge = []
                for each_equal in original_equals_list:
                    if len(this_equal.intersection(each_equal)) >= 1:
                        need_merge.append(each_equal)
                        equals_list.remove(each_equal)
                if len(need_merge) >= 1:
                    merged_equal = this_equal.copy()
                    for each_need_merge_equal in need_merge:
                            merged_equal.update(each_need_merge_equal)
                    equals_list.append(merged_equal)
                    already_in = True
            """ not in """
            if not already_in:
                equals_list.append(this_equal)
        
        if equal_type == 'segment':
            check_and_add(this_equal, self.segment_equals)
        elif equal_type == 'angle':
            check_and_add(this_equal, self.angle_equals)
        else:
            raise Exception('add equal type error!')

    """ Deduction """
    def deduce(self):
        
        """ complex units equal transform """
        def complex_units_equal_transform(graph, equals_list, equal_type):
            for each_equal in equals_list:
                for each_complex_unit in each_equal:
                    if is_complex_type(each_complex_unit):
                        complex_type = get_unit_type(each_complex_unit)
                        """ replace sub unit """
                        """ AB+BM=MN, BM=BC ---> AB+BM=AB+BC=MN """
                        """ AB*BM=MN*ML, BM=BC ---> AB*BM=AB*BC=MN*ML """
                        """ AB*AB=MN*ML, AB=BC ---> AB*AB=AB*BC=BC*BC=MN*ML """
                        for each_sub_unit in get_complexunit_set(each_complex_unit):
                            for each_another_equal in equals_list:
                                if each_sub_unit in each_another_equal:
                                    for each_another_sub_unit in get_equal_except_unit(each_another_equal, each_sub_unit):
                                        graph.add_equal(equal(
                                            complex_units(complex_type, 
                                                          get_complexunit_except_unit(each_complex_unit, each_sub_unit), 
                                                          each_another_sub_unit), 
                                            each_complex_unit), equal_type)                      
                        """ eliminate sub unit """
                        """ AB+BM=AB+BC ---> BM=BC ; AB+BM+MN=AB+BC ---> BM+MN=BC """
                        """ AB*BM=AB*BC ---> BM=BC ; AB*BM*MN=AB*BC*DE ---> BM*MN=BC*DE """
                        """ AB*AB=AB*BC ---> AB=BC ; AB*AB*MN=AB*BC*DE ---> AB*MN=BC*DE """
                        for each_another_complex_unit in get_equal_except_unit(each_equal, each_complex_unit):
                            if get_unit_type(each_another_complex_unit) == complex_type:
                                if get_unit_len(get_complexunit_inner_complexunit(each_complex_unit, each_another_complex_unit)) >= 1:
                                     graph.add_equal(equal(
                                             get_complexunit_except_unit(each_complex_unit, each_another_complex_unit),
                                             get_complexunit_except_unit(each_another_complex_unit, each_complex_unit)
                                             ), equal_type)
                        """ multiply allocate """
                        """ (AE+EB)*AC=AB*AC ---> (AE+EB)*AC=AE*AC+EB*AC=AB*AC """
                        """ (AE+EM+MB)*AC=AB*AC ---> (AE+EM+MB)*AC=AE*AC+EM*AC+MB*AC=AB*AC """
                        """ (AE+AE+MB)*AC=AB*AC ---> (AE+AE+MB)*AC=AE*AC+AE*AC+MB*AC=AB*AC """
                        if complex_type == 'multiply':
                            for each_sub_unit in get_complexunit_set(each_complex_unit):
                                if get_unit_type(each_sub_unit) == 'sum':
                                    excepted_unit = get_complexunit_except_unit(each_complex_unit, each_sub_unit)
                                    allocated_complex_unit = sum_units()
                                    for each_sub_sub_unit in get_complexunit_set(each_sub_unit):
                                        allocated_complex_unit = sum_units(allocated_complex_unit, 
                                                                           multiply_units(each_sub_sub_unit, excepted_unit))
                                    graph.add_equal(equal(allocated_complex_unit, each_complex_unit), equal_type)
                        """ multiply associate """
                        """ AE*AC+EB*AC=AB*AC ---> AE*AC+EB*AC=(AE+EB)*AC=AB*AC """
                        """ AE*AC+EM*AC+MB*AC=AB*AC ---> AE*AC+EM*AC+MB*AC=(AE+EM)*AC+MB*AC=AB*AC """
                        """ (AE+EM)*AC+MB*AC=AB*AC ---> (AE+EM)*AC+MB*AC=(AE+EM+MB)*AC=AB*AC """
                        if complex_type == 'sum':
                            for each_sub_unit in get_complexunit_set(each_complex_unit):
                                if get_unit_type(each_sub_unit) == 'multiply':
                                    excepted_unit = get_complexunit_except_unit(each_complex_unit, each_sub_unit)
                                    if get_unit_type(excepted_unit) == 'sum':
                                        for each_another_sub_unit in get_complexunit_set(excepted_unit):
                                            if get_unit_type(each_another_sub_unit) == 'multiply':
                                                inner_unit = get_complexunit_inner_complexunit(each_sub_unit, each_another_sub_unit)
                                                excepted_2_unit = get_complexunit_except_unit(excepted_unit, each_another_sub_unit)
                                                for inner_sub_unit in get_unit_flatten_set(inner_unit, 'multiply'):                                                    
                                                    associated_complex_unit = sum_units(
                                                        multiply_units(inner_sub_unit, 
                                                                       sum_units(get_complexunit_except_unit(each_sub_unit, inner_sub_unit), 
                                                                                 get_complexunit_except_unit(each_another_sub_unit, inner_sub_unit))
                                                                       ), 
                                                        excepted_2_unit)
                                                    graph.add_equal(equal(associated_complex_unit, each_complex_unit), equal_type)
                                    elif get_unit_type(excepted_unit) == 'multiply':
                                        inner_unit = get_complexunit_inner_complexunit(each_sub_unit, excepted_unit)
                                        for inner_sub_unit in get_unit_flatten_set(inner_unit, 'multiply'):
                                            associated_complex_unit = multiply_units(inner_sub_unit, 
                                                                                     sum_units(get_complexunit_except_unit(each_sub_unit, inner_sub_unit), 
                                                                                               get_complexunit_except_unit(excepted_unit, inner_sub_unit))
                                                                                     )
                                            graph.add_equal(equal(associated_complex_unit, each_complex_unit), equal_type)
                                                            
        """ space and collinear transform """
        def space_and_collinear_transform(graph):
            
            return 0
        
        """ theorem transform """
        def triangle_theorem_transform(graph):
            triangles_list = list(combinations(graph.points.keys(), 3))
            triangles_num = len(triangles_list)
            for no_1 in range(triangles_num):
                this_triangle = triangles_list[no_1]
                """ interior angle summation 180° """
                graph.add_equal(equal(sum_units(angle(this_triangle[1], this_triangle[0], this_triangle[2]), 
                                                angle(this_triangle[0], this_triangle[1], this_triangle[2]), 
                                                angle(this_triangle[0], this_triangle[2], this_triangle[1])), 
                                      degree(180)), 'angle')
                """ isosceles """
                yes_isosceles, vertex_point, aside_points = is_isosceles(graph, this_triangle)
                if yes_isosceles:
                    graph.add_equal(equal(segment(vertex_point, aside_points[0]), 
                                          segment(vertex_point, aside_points[1])), 'segment')
                    graph.add_equal(equal(angle(vertex_point, aside_points[0], aside_points[1]), 
                                          angle(vertex_point, aside_points[1], aside_points[0])), 'angle')
                """ congruent and similar """
                for no_2 in range(no_1+1, triangles_num):
                    another_triangle = triangles_list[no_2]        
                    """ congruent """
                    yes_congruent, three_points_1, three_points_2 = is_congruent(graph, this_triangle, another_triangle)                            
                    if yes_congruent:
                        graph.add_equal(equal(segment(three_points_1[0], three_points_1[1]), 
                                              segment(three_points_2[0], three_points_2[1])), 'segment')
                        graph.add_equal(equal(segment(three_points_1[0], three_points_1[2]), 
                                              segment(three_points_2[0], three_points_2[2])), 'segment')
                        graph.add_equal(equal(segment(three_points_1[1], three_points_1[2]), 
                                              segment(three_points_2[1], three_points_2[2])), 'segment')
                        graph.add_equal(equal(angle(three_points_1[1], three_points_1[0], three_points_1[2]), 
                                              angle(three_points_2[1], three_points_2[0], three_points_2[2])), 'angle')
                        graph.add_equal(equal(angle(three_points_1[0], three_points_1[1], three_points_1[2]), 
                                              angle(three_points_2[0], three_points_2[1], three_points_2[2])), 'angle')
                        graph.add_equal(equal(angle(three_points_1[0], three_points_1[2], three_points_1[1]), 
                                              angle(three_points_2[0], three_points_2[2], three_points_2[1])), 'angle')
                    """ similar """
                    
            return 0
        
        def quadrilateral_theorem_transform(graph):
            
            return 0
        
        complex_units_equal_transform(self, self.segment_equals, 'segment')
        complex_units_equal_transform(self, self.angle_equals, 'angle')
        space_and_collinear_transform(self)
        triangle_theorem_transform(self)
        quadrilateral_theorem_transform(self)
    
    """ Query """
    def query(self, query_equal):
        
        return 0
    
    """ Display """
    def display(self):
        
        def unit_to_math_str(this_unit):
            if get_unit_type(this_unit) == 'degree':
                return str(this_unit[1])+'°'
            elif get_unit_type(this_unit) == 'segment':
                return this_unit[1]
            elif get_unit_type(this_unit) == 'angle':
                return '∠' + this_unit[1]
            elif get_unit_type(this_unit) == 'sum':
                this_complex_unit_math_str = '('
                for this_sub_unit in get_complexunit_set(this_unit):
                    this_complex_unit_math_str += unit_to_math_str(this_sub_unit) + '+'
                this_complex_unit_math_str = this_complex_unit_math_str[:-1] + ')'
                return this_complex_unit_math_str   
            elif get_unit_type(this_unit) == 'multiply':
                this_complex_unit_math_str = ''
                for this_sub_unit in get_complexunit_set(this_unit):
                    this_complex_unit_math_str += unit_to_math_str(this_sub_unit) + '*'
                this_complex_unit_math_str = this_complex_unit_math_str[:-1]
                return this_complex_unit_math_str            
        
        def get_simplified_unit_math_str(this_unit):
            this_unit_math_str = unit_to_math_str(this_unit)
            if this_unit_math_str[0] == '(' and this_unit_math_str[-1] == ')':
                return this_unit_math_str[1:-1]
            else:
                return this_unit_math_str

        def equal_to_math_str(this_equal):
            this_equal_math_str = ''
            for each_unit in this_equal:
                this_equal_math_str = this_equal_math_str + '=' + get_simplified_unit_math_str(each_unit)
            return this_equal_math_str[1:]
                
        print('Graph Name:  ', self.name)
        print('points num:  ', len(self.points))
        print('segment equals:  ', len(self.segment_equals))
        for each_segment_equal in self.segment_equals:
            print('  ', equal_to_math_str(each_segment_equal))
        print('angle equals:  ', len(self.angle_equals))
        for each_angle_equal in self.angle_equals:
            print('  ', equal_to_math_str(each_angle_equal))