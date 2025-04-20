from math import sqrt, acos, pi
'''
File to keep all the public functions of the software system.
'''
def extract_angle_and_dist(x, y):
    '''
    Function to extract an angle and a distance to a point represented by two values.

    :param x: X coordinate of the point.
    :param y: Y coordinate of the point.
    :return: Returns the angle and distance to a point from origo.
    '''
    if x == 0:
        dist = abs(y)
        if y >= 0:
            angle= pi/2
        elif y < 0:
            angle= 3*pi/2
    elif y == 0:
        dist = abs(x)
        if x >= 0:
            angle = 0
        elif x < 0:
            angle = pi
    else:
        #y and x are not 0'
        dist = sqrt(x*x+y*y)
        if y < 0 and x < 0:
            angle = acos(x/dist)+pi/2  
        elif (y < 0 and x >= 0):
            angle = 2*pi-acos(x/dist) 
        else:
            angle = acos(x/dist)  
    return angle , dist