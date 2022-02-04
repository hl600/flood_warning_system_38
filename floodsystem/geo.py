# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import numpy as np
from haversine import haversine, Unit
from utils import sorted_by_key  # noqa


#Task 1B
def stations_by_distance(stations, p):
    list_of_tuples=[]
    for station in stations:
        element = (station.name,haversine(station.coord,p))
        list_of_tuples.append(element)
    sorted_list = sorted_by_key(list_of_tuples,1)
    return sorted_list

#Task 1C
def stations_within_radius(stations, centre, r):
    for station in stations:
        