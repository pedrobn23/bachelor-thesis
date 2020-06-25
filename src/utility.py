def triple_equal(x, y, z, vpool):
    return [[vpool.id(x), -vpool.id(y), vpool.id(z)],
            [-vpool.id(x), vpool.id(y),-vpool.id(z)],
            [vpool.id(x), -vpool.id(y),-vpool.id(z)],
            [vpool.id(x), vpool.id(y), vpool.id(z)]]

def xvar(word, pos):
    return 'x{} {}'.format(i, j)

def yvar(i):
    return 'y{}'.format(i)

def zvar(i, j):
    return 'z{} {}'.format(i, j)
