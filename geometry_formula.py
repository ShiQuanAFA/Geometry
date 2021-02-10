#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Import """
from geometry_define import segment, angle, equal
from geometry_define import multiply_units
from math import pi, acos

""" Calculate functions """

""" judge three points collinear """
def is_collinear(graph, this_three_point):
    is_collinear_result = False
    vertex_point = '' 
    aside_points = ()
    for point_vertex in this_three_point:
        point_aside = tuple_del(this_three_point, point_vertex)
        distance_ends = cal_two_points_distance(graph, point_aside[0], point_aside[1])
        distance_sum = cal_two_points_distance(graph, point_vertex, point_aside[0]) + \
                        cal_two_points_distance(graph, point_vertex, point_aside[1])
        if abs(distance_sum - distance_ends) < 0.01:
            is_collinear_result = True
            vertex_point = point_vertex
            aside_points = point_aside
            return is_collinear_result, vertex_point, aside_points
    """ return judge result """
    return is_collinear_result, vertex_point, aside_points

""" judge triangle isosceles """
def is_isosceles(graph, this_triangle):
    is_isosceles_result = False
    vertex_point = '' 
    aside_points = ()
    """ every vertex """
    for point_vertex in this_triangle:
        point_aside = tuple_del(this_triangle, point_vertex)
        if (equal(segment(point_aside[0], point_vertex), 
                  segment(point_aside[1], point_vertex)) in graph.segment_equals 
            ) or ( 
            equal(angle(point_vertex, point_aside[0], point_aside[1]), 
                  angle(point_vertex, point_aside[1], point_aside[0])) in graph.angle_equals):
            is_isosceles_result = True
            vertex_point = point_vertex
            aside_points = point_aside
            return is_isosceles_result, vertex_point, aside_points
    """ return judge result """
    return is_isosceles_result, vertex_point, aside_points

""" judge triangle congruent """
def is_congruent(graph, triangle_1, triangle_2):
    is_congruent_result = False
    three_points_1 = ()
    three_points_2 = ()
    """ every double vertex """
    for point_vertex_1 in triangle_1:
        point_aside_1 = tuple_del(triangle_1, point_vertex_1)
        for point_vertex_2 in triangle_2:
            point_aside_2 = tuple_del(triangle_2, point_vertex_2)
            """ A or S """
            if equal(angle(point_aside_1[0], point_vertex_1, point_aside_1[1]), 
                     angle(point_aside_2[0], point_vertex_2, point_aside_2[1])) in graph.angle_equals:
                for point_aside_1_1 in point_aside_1:
                    point_aside_1_2 = tuple_del(point_aside_1, point_aside_1_1)[0]
                    point_aside_2_1 = point_aside_2[0]
                    point_aside_2_2 = point_aside_2[1]
                    """ AS """
                    if equal(segment(point_aside_1_1, point_vertex_1), 
                             segment(point_aside_2_1, point_vertex_2)) in graph.segment_equals:
                        """ ASS """
                        if equal(segment(point_aside_1_2, point_vertex_1), 
                                 segment(point_aside_2_2, point_vertex_2)) in graph.segment_equals:
                            is_congruent_result = True
                            three_points_1 = (point_aside_1_1, point_vertex_1, point_aside_1_2)
                            three_points_2 = (point_aside_2_1, point_vertex_2, point_aside_2_2)
                            return is_congruent_result, three_points_1, three_points_2
            elif equal(segment(point_aside_1[0], point_aside_1[1]), 
                       segment(point_aside_2[0], point_aside_2[1])) in graph.segment_equals:
                for point_aside_1_1 in point_aside_1:
                    point_aside_1_2 = tuple_del(point_aside_1, point_aside_1_1)[0]
                    point_aside_2_1 = point_aside_2[0]
                    point_aside_2_2 = point_aside_2[1]
                    """ SS or SA"""
                    if equal(segment(point_aside_1_1, point_vertex_1), 
                             segment(point_aside_2_1, point_vertex_2)) in graph.segment_equals:
                        """ SSS """
                        if equal(segment(point_aside_1_2, point_vertex_1), 
                                 segment(point_aside_2_2, point_vertex_2)) in graph.segment_equals:
                            is_congruent_result = True
                            three_points_1 = (point_aside_1_1, point_vertex_1, point_aside_1_2)
                            three_points_2 = (point_aside_2_1, point_vertex_2, point_aside_2_2)   
                            return is_congruent_result, three_points_1, three_points_2
                    elif equal(angle(point_vertex_1, point_aside_1_1, point_aside_1_2), 
                               angle(point_vertex_2, point_aside_2_1, point_aside_2_2)) in graph.angle_equals:
                        """ SAA """
                        if equal(angle(point_vertex_1, point_aside_1_2, point_aside_1_1), 
                                 angle(point_vertex_2, point_aside_2_2, point_aside_2_1)) in graph.angle_equals:
                            is_congruent_result = True
                            three_points_1 = (point_aside_1_1, point_vertex_1, point_aside_1_2)
                            three_points_2 = (point_aside_2_1, point_vertex_2, point_aside_2_2) 
                            return is_congruent_result, three_points_1, three_points_2
    """ return judge result """
    return is_congruent_result, three_points_1, three_points_2
    
""" judge triangle similar """
def is_similar(graph, triangle_1, triangle_2):
    is_similar_result = False
    three_points_1 = ()
    three_points_2 = ()
    """ every double vertex """
    for point_vertex_1 in triangle_1:
        point_aside_1 = tuple_del(triangle_1, point_vertex_1)
        for point_vertex_2 in triangle_2:
            point_aside_2 = tuple_del(triangle_2, point_vertex_2)
            for point_aside_1_1 in point_aside_1:
                point_aside_1_2 = tuple_del(point_aside_1, point_aside_1_1)[0]
                point_aside_2_1 = point_aside_2[0]
                point_aside_2_2 = point_aside_2[1]
                """ A or S """
                if equal(angle(point_aside_1[0], point_vertex_1, point_aside_1[1]), 
                         angle(point_aside_2[0], point_vertex_2, point_aside_2[1])) in graph.angle_equals:
                    """ AA """
                    if equal(angle(point_vertex_1, point_aside_1_1, point_aside_1_2), 
                             angle(point_vertex_2, point_aside_2_1, point_aside_2_2)) in graph.angle_equals:
                        is_similar_result = True
                        three_points_1 = (point_aside_1_1, point_vertex_1, point_aside_1_2)
                        three_points_2 = (point_aside_2_1, point_vertex_2, point_aside_2_2)
                        return is_similar_result, three_points_1, three_points_2
                    """ AS """
                    if equal(multiply_units(segment(point_aside_1_1, point_vertex_1), 
                                            segment(point_aside_2_2, point_vertex_2)), 
                             multiply_units(segment(point_aside_1_2, point_vertex_1), 
                                            segment(point_aside_2_1, point_vertex_2))) in graph.segment_equals:
                        is_similar_result = True
                        three_points_1 = (point_aside_1_1, point_vertex_1, point_aside_1_2)
                        three_points_2 = (point_aside_2_1, point_vertex_2, point_aside_2_2)
                        return is_similar_result, three_points_1, three_points_2
                elif equal(multiply_units(segment(point_aside_1_1, point_vertex_1), 
                                          segment(point_aside_2_2, point_vertex_2)), 
                           multiply_units(segment(point_aside_1_2, point_vertex_1), 
                                          segment(point_aside_2_1, point_vertex_2))) in graph.segment_equals:
                    """ SS """
                    if equal(multiply_units(segment(point_aside_1_1, point_vertex_1), 
                                            segment(point_aside_2_1, point_aside_2_2)), 
                             multiply_units(segment(point_aside_2_1, point_vertex_2), 
                                            segment(point_aside_1_1, point_aside_1_2))) in graph.segment_equals:
                        is_similar_result = True
                        three_points_1 = (point_aside_1_1, point_vertex_1, point_aside_1_2)
                        three_points_2 = (point_aside_2_1, point_vertex_2, point_aside_2_2)
                        return is_similar_result, three_points_1, three_points_2
    """ return judge result """
    return is_similar_result, three_points_1, three_points_2

""" cal two points distance """
def cal_two_points_distance(graph, point_1, point_2):
    location_1_x = graph.points[point_1]['location_x']
    location_1_y = graph.points[point_1]['location_y']
    location_2_x = graph.points[point_2]['location_x']
    location_2_y = graph.points[point_2]['location_y']
    distance = ((location_2_x-location_1_x)**2 + (location_2_y-location_1_y)**2)**0.5
    return distance

""" cal an angle degree """
def cal_an_angle_degree(graph, point_aside_1, point_vertex, point_aside_2):
    location_1_x = graph.points[point_aside_1]['location_x']
    location_1_y = graph.points[point_aside_1]['location_y']
    location_2_x = graph.points[point_aside_2]['location_x']
    location_2_y = graph.points[point_aside_2]['location_y']
    location_vertex_x = graph.points[point_vertex]['location_x']
    location_vertex_y = graph.points[point_vertex]['location_y']
    vec_1 = (location_1_x-location_vertex_x, location_1_y-location_vertex_y)
    vec_2 = (location_2_x-location_vertex_x, location_2_y-location_vertex_y)
    vec_1_len = (vec_1[0]**2 + vec_1[1]**2)**0.5
    vec_2_len = (vec_2[0]**2 + vec_2[1]**2)**0.5
    angle_cos = (vec_1[0]*vec_2[0] + vec_1[1]*vec_2[1]) / (vec_1_len * vec_2_len)
    angle_degree = (acos(angle_cos) / pi) * 180
    return angle_degree

""" tuple del """
def tuple_del(this_tuple, this_value):
    this_tuple_list = list(this_tuple)
    this_tuple_list.remove(this_value)
    return tuple(this_tuple_list)

def tuple_except_tuple(this_tuple, another_tuple):
    this_tuple_list = list(this_tuple)
    for this_value in another_tuple:
        this_tuple_list.remove(this_value)
    return tuple(this_tuple_list)