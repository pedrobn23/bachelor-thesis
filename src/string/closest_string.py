import time
import math
import random

from bitarray import bitarray
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool, CNF


def triple_equal(x,y,z,vpool):
    return [
        [vpool.id(x), -vpool.id(y), vpool.id(z)],
        [-vpool.id(x), vpool.id(y), vpool.id(z)],
        [-vpool.id(x), -vpool.id(y), -vpool.id(z)],
        [vpool.id(x), vpool.id(y), -vpool.id(z)]]

def closest_string(bitarray_list, distance=4, verbose=True):
    """
    Check if there exists a vertex cover of, at most, k-vertices.
    """
    if distance < 0:
        raise ValueError('Distance must be positive integer')
    
    if verbose:
        print('\nCodifying SAT Solver...')


    length = max(len(word) for word in list)
    solver = Solver(name='cd')
    vpool = IDPool()
    local_bitarray = bitarray_list.copy()

    if verbose:
        print(' -> Codifying: normalizing strings')

    aux = length*bitarray('0')
    for bitarr in bitarray_list:
        bitarr = bitarr + aux

    def x(word,pos):
        return 'x{} {}'.format(i,j)
    
    def y(i):
        return 'y{}'.format(i)

    def z(i,j):
        return 'z{} {}'.format(i,j)

    if verbose:
        print(' -> Codifying: imposing distance condition')
    
    for index, word in string_list:
        for pos in range(length):
            for clause in triple_equal(x(index,pos), y(pos), z(index,pos)):
                solver.add_clause(clause)
        cnf = CardEnc.equals(lits = [ z(index,pos) for pos in range(length)],
                             bound=distance,
                             vpool=vpool)

    if verbose:
        print(' -> Codifying: Words Value')
    for index, word in string_list:
        for pos in range(length):
            solver.propagate(assumptions=[vpool.id(x(index,pos)) * (-1)**(not word[pos]) ])
   



    if verbose:
        print('Running SAT Solver...')
    return solver.solve()


