#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Import """
from geometry_define import segment, angle, equal
from geometry_define import multiply_units

""" Calculate functions """

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
                    elif equal(angle(point_vertex_1, point_aside_1_1, point_aside_1_2), 
                               angle(point_vertex_2, point_aside_2_1, point_aside_2_2)) in graph.angle_equals:
                        """ SAA """
                        if equal(angle(point_vertex_1, point_aside_1_2, point_aside_1_1), 
                                 angle(point_vertex_2, point_aside_2_2, point_aside_2_1)) in graph.angle_equals:
                            is_congruent_result = True
                            three_points_1 = (point_aside_1_1, point_vertex_1, point_aside_1_2)
                            three_points_2 = (point_aside_2_1, point_vertex_2, point_aside_2_2)   
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
                    """ AS """
                    if equal(multiply_units(segment(point_aside_1_1, point_vertex_1), 
                                            segment(point_aside_2_2, point_vertex_2)), 
                             multiply_units(segment(point_aside_1_2, point_vertex_1), 
                                            segment(point_aside_2_1, point_vertex_2))) in graph.segment_equals:
                        is_similar_result = True
                        three_points_1 = (point_aside_1_1, point_vertex_1, point_aside_1_2)
                        three_points_2 = (point_aside_2_1, point_vertex_2, point_aside_2_2)
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
    """ return judge result """
    return is_similar_result, three_points_1, three_points_2
                        
""" tuple del """
def tuple_del(this_tuple, this_value):
    this_tuple_list = list(this_tuple)
    this_tuple_list.remove(this_value)
    return tuple(this_tuple_list)