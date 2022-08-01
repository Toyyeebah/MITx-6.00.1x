#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:00:08 2022

@author: toyyeebahmustapha
"""

import math
def polysum(n,s):
    '''
    Input: n - number of sides(should be an integer)
    s- length of each sides(can be an integer or a float)
    
    Output: Returns Sum of area and the square of the perimeter of the regular polygon(gives a float)
    '''
    #Code
    def areaOfPolygon(n,s):
        #Pi = 3.1428
        area = (0.25 * n * s ** 2)/math.tan(math.pi/n)
        return area
    def perimeterOfPolygon(n,s):
        perimeter = n * s
        return perimeter
    sum = areaOfPolygon(n,s) + (perimeterOfPolygon(n,s) ** 2)
    return round(sum,4)






"""

# Another attempt
def polysum(n, s):
    ""
    input: n = number of sides
    input: s = side length
    output: sum the area and square of the permiter of polygon, round to 4 decimal places
    ""
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    perimeter = n * s
    return round(area + perimeter ** 2, 4)


# another attempt
import math
def polysum(n,s):
return float(format((n*s)**2 + (0.25*n*s**2)/(math.tan(math.pi/n)),'.4f'))

#another attempt
import math
def polysum(n, s):
    total = 0
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    total += area + (n*s)**2
    return float("{0:.4f}".format(total))
    #"%.2f" % 3.14159 will convert to string