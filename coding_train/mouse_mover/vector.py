import math
import random
from numpy import array as vector
import numpy as np

def createVector(x, y):
    ''' Return a new vector '''
    return vector([x, y], dtype=np.float64)

def normalize(vec, scale=1):
    ''' return vector normalized '''
    if vec[0] == 0 and vec[1] == 0:
        return vec

    m = mag(vec)
    return createVector(vec[0]/m, vec[1]/m) * scale

def mag(vec):
    ''' Return  magnitude of vector '''
    return math.sqrt(vec[0] ** 2 + vec[1] ** 2)

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

