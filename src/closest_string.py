"""
Module that implements function closest string to solve 

"""

import time
import math
import random

from bitarray import bitarray
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool, CNF
from utility import triple_equal, xvar, yvar, zvar


def closest_string(bitarray_list, distance=4, verbose=True):
    """
    Return a bitarray of distance at most 'distance'
    """
    if distance < 0:
        raise ValueError('Distance must be positive integer')

    if verbose:
        print('\nCodifying SAT Solver...')

    length = max(len(word) for word in bitarray_list)
    solver = Solver(name='mcm')
    vpool = IDPool()
    local_bitarray = bitarray_list.copy()

    if verbose:
        print(' -> Codifying: normalizing strings')

    aux = length * bitarray('0')
    for index, bitarr in enumerate(bitarray_list):
        bitarray_list[index] = bitarr + aux

    if verbose:
        print(' -> Codifying: imposing distance condition')

    for index, word in enumerate(bitarray_list):
        for pos in range(length):
            vpool.id(xvar(index, pos))

    for pos in range(length):
        vpool.id(yvar(pos))

    for index, word in enumerate(bitarray_list):
        for pos in range(length):
            vpool.id(zvar(index, pos))

    for index, word in enumerate(bitarray_list):
        for pos in range(length):
            for clause in triple_equal(xvar(index, pos),
                                       yvar(pos),
                                       zvar(index, pos),
                                       vpool=vpool):
                solver.add_clause(clause)
        cnf = CardEnc.atleast(
            lits=[vpool.id(zvar(index, pos)) for pos in range(length)],
            bound=length-distance,
            vpool=vpool)
        solver.append_formula(cnf)

    if verbose:
        print(' -> Codifying: Words Value')

    assumptions = []
    for index, word in enumerate(bitarray_list):
        for pos in range(length):
            assumptions += [vpool.id(xvar(index, pos)) * (-1)**(not word[pos])]

    if verbose:
        print('Running SAT Solver...')
    
    return solver.solve(assumptions=assumptions)

def minimun_distance(bitarray_list):
    """
    Using the minimizing trick, return the distance of the bitarray 
    to the closest string
    """
    old = max(len(word) for word in bitarray_list)
    new = old // 2

    while old != new:
        if closest_string(bitarray_list, new, False):
            old = new
            new = new // 2
        else:
            new += math.ceil((old - new) / 2)

    return new

