from math import sqrt, acos, pi
def extract_angle_and_dist(x, y):
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