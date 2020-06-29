def triple_equal(x, y, z, vpool):
    return [[vpool.id(x), -vpool.id(y), vpool.id(z)],
            [-vpool.id(x), vpool.id(y), -vpool.id(z)],
            [vpool.id(x), -vpool.id(y), -vpool.id(z)],
            [vpool.id(x), vpool.id(y), vpool.id(z)]]


def xvar(*args):
    return 'x' + ' '.join([str(arg) for arg in args])


def yvar(*args):
    return 'y' + ' '.join([str(arg) for arg in args])


def zvar(*args):
    return 'z' + ' '.join([str(arg) for arg in args])


def to_minimun(funct):

    def __minim(graph):
        old = len(graph)
        new = old // 2

        while old != new:
            if funct(graph, new, False):
                old = new
                new = new // 2

            else:
                new += math.ceil((old - new) / 2)

        return new

    return __minim
