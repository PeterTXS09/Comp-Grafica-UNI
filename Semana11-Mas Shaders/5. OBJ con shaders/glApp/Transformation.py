import numpy as np
from math import *

def identity_matrix():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]], np.float32)

def translate_mat(x, y, z):
    return np.array([[1, 0, 0, x],
                     [0, 1, 0, y],
                     [0, 0, 1, z],
                     [0, 0, 0, 1]], np.float32)

def scale_mat(s):
    return np.array([[s, 0, 0, 0],
                     [0, s, 0, 0],
                     [0, 0, s, 0],
                     [0, 0, 0, 1]], np.float32)

def scale_mat3(sx, sy, sz):
    return np.array([[sx, 0, 0, 0],
                     [0, sy, 0, 0],
                     [0, 0, sz, 0],
                     [0, 0, 0, 1]], np.float32)

def rotate_x_mat(angle):
    c = cos(radians(angle))
    s = sin(radians(angle))
    return np.array([[1, 0,  0, 0],
                     [0, c, -s, 0],
                     [0, s,  c, 0],
                     [0, 0,  0, 1]], np.float32)

def rotate_y_mat(angle):
    c = cos(radians(angle))
    s = sin(radians(angle))
    return np.array([[ c, 0, s, 0],
                     [ 0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [ 0, 0, 0, 1]], np.float32)

def rotate_z_mat(angle):
    c = cos(radians(angle))
    s = sin(radians(angle))
    return np.array([[c, -s, 0, 0],
                     [s,  c, 0, 0],
                     [0,  0, 1, 0],
                     [0,  0, 0, 1]], np.float32)

def translate(matrix, x, y, z):
    trans = translate_mat(x, y, z)
    return matrix @ trans

def scale(matrix, s):
    sc = scale_mat(s)
    return matrix @ sc

def scale3(matrix, x, y, z):
    sc = scale_mat3(x, y, z)
    return matrix @ sc

def rotate(matrix, angle, axis, local=True):
    rot = identity_matrix()
    if axis == "x":
        rot = rotate_x_mat(angle)
    if axis == "y":
        rot = rotate_y_mat(angle)
    if axis == "z":
        rot = rotate_z_mat(angle)
    if local:
        return matrix @ rot
    else:
        return rot @ matrix