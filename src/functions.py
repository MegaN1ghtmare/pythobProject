def sequence_mult(x, y, *args):  # pragma: no cover
    result = x * y
    for arg in args:
        result *= arg

    return result


def crete_point(x, y, *args, color='black', **kwargs):  # pragma: no cover
    print(f'{color.capitalize()} Point({x}, {y})')


if __name__ == '__main__':  # pragma: no cover
    # print(sequence_mult(10, 10, 10, 10))
    array = [2, 4, 100005000, 3000]
    parameters = {'color': 'yellow', 'password': 'admin', 'user': 'caiman'}

    crete_point(*array, **parameters)