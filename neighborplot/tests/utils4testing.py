"""Little utilities for testing."""



import scipy.stats as stats
import numpy as np


def rand_coords(dim=2, nnodes=50):
    '''
    :param nrows: number of rows in the 2d array
    :param ncols: number of cols in the 2d array
    :param mu:    mean for random generation
    :param std:   standard deviation for random generation
    :return: returns a random 2d numpy array, generated with normal distribution
    '''

    '''
    :return: generates random data
    '''
    return stats.norm.rvs(loc=0, scale=3.5, size=(nnodes, dim))

def flip_coords(coords):
    for ncol in range(coords.shape[1]):
        coords[:, ncol] *= np.random.choice([1,-1])
    return coords


