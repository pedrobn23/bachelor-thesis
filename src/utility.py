def triple_equal(x, y, z, vpool):
    return [[vpool.id(x), -vpool.id(y), vpool.id(z)],
            [-vpool.id(x), vpool.id(y),-vpool.id(z)],
            [vpool.id(x), -vpool.id(y),-vpool.id(z)],
            [vpool.id(x), vpool.id(y), vpool.id(z)]]

def xvar(args*):
    return 'x' + ' '.join([str(arg) for arg in args])

def yvar(args*):
    return 'y' + ' '.join([str(arg) for arg in args])

def zvar(args*):
    return 'z' + ' '.join([str(arg) for arg in args])
