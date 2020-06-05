from math import acos, sqrt, pi


def pitch_from_x( v ):

    w = (0, v[1], v[2])

    return acos(dot_product(v, w)/(vec_abs(v)*vec_abs(w)))

def dot_product( v , w):

    assert len(v) == len(w)

    s = 0

    for i in range(len(v)):
        s+= v[i]*w[i]

    return s

def map (value, in_range, out_range):

    normalized_value = max(0 ,(value-in_range[0])/(in_range[1]-in_range[0]))

    return normalized_value * (out_range[1] - out_range[0]) + out_range[0]

def vec_abs(vector):
    sum = 0
    for element in vector:
        sum += element**2
    return sqrt(sum)

def deg_to_rad(angle):
    return (2*pi*angle)/360.0

def rad_to_deg(angle):
    return (angle*360)/(2*pi)