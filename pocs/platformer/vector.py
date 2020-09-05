import math
import random
from numpy import array as vector
import numpy as np

''' Constants for the x and y attributes of a vector '''
X = 0
Y = 1

np.seterr(all='raise')

def createVector(x, y):
    ''' Return a new vector '''
    return vector([x, y], dtype=np.float64)

def normalize(vec, scale=1):
    ''' return vector normalized '''
    if vec[X] == 0 and vec[Y] == 0:
        return vec

    m = mag(vec)
    return createVector(vec[X]/m, vec[Y]/m) * scale

def mag(vec):
    ''' Return  magnitude of vector '''
    return math.sqrt(vec[X] ** 2 + vec[Y] ** 2)
    '''
    try:
        xs = math.pow(vec[X], 2)
        ys = math.pow(float(vec[Y]), 2)
        return math.sqrt(xs + ys)
    except Exception as e:
        print(f"Caught exception {e}")
        print(f"For value {vec}")
    '''


def withMag(vec, magnitude):
    ''' Return the given vector with the magnitude set to the given mag '''
    return normalize(vec, magnitude)


def limit(vec, limit):
    ''' Return vector with magnitude <= the given limit '''
    m = mag(vec)
    if m > limit:
        return normalize(vec, limit)
    else:
        return vec
    

def createRandomVector(length=100):
    ''' Return a random vector within a given length '''
    x = (length*2) * random.random() - length
    y = (length*2) * random.random() - length
    return createVector(x, y)

def createRandomNormalizedVector(length=1):
    ''' Return a random vector within a given length '''
    return normalize(createRandomVector(100), length)

