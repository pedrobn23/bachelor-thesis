"""
Module that implements function closest string to solve
"""


import math
from bitarray import bitarray
from pysat.solvers import Solver
from pysat.card import CardEnc
from pysat.formula import IDPool
from utility import triple_equal, xvar, yvar, zvar


def closest_string(bitarray_list, distance=4, verbose=True):
    """
    Return if a bitarray exists of distance at most 'distance'.
    Use example:

    s1=bitarray('0010')
    s2=bitarray('0011')
    closest_string([s1,s2], distance=0, verbose=False)
    > False
    closest_string([s1,s2], distance=2, verbose=False)
    > True
    """
    if distance < 0:
        raise ValueError('Distance must be positive integer')

    if verbose:
        print('\nCodifying SAT Solver...')

    length = max(bitarray_list, key=len)
    solver = Solver(name='mcm')
    vpool = IDPool()
    local_list = bitarray_list.copy()

    if verbose:
        print(' -> Codifying: normalizing strings')

    aux = length * bitarray('0')
    for index, bitarr in enumerate(bitarray_list):
        local_list[index] = bitarr + aux

    if verbose:
        print(' -> Codifying: imposing distance condition')

    for index, word in enumerate(local_list):
        for pos in range(length):
            vpool.id(xvar(index, pos))

    for pos in range(length):
        vpool.id(yvar(pos))

    for index, word in enumerate(local_list):
        for pos in range(length):
            vpool.id(zvar(index, pos))

    for index, word in enumerate(local_list):
        for pos in range(length):
            for clause in triple_equal(xvar(index, pos),
                                       yvar(pos),
                                       zvar(index, pos),
                                       vpool=vpool):
                solver.add_clause(clause)
        cnf = CardEnc.atleast(
            lits=[vpool.id(zvar(index, pos)) for pos in range(length)],
            bound=length - distance,
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


def minimum_distance(bitarray_list):
    """
    Using the minimizing trick, return the distance of the bitarray
    to the closest string.
    Use example:

    s1=bitarray('0010')
    s2=bitarray('0011')
    minimum_distance([s1,s2])
    > 1
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
