def array_scan():  # pragma: no cover
    return [int(elem) for elem in input().strip().split()]


def array_reverse(array):
    return array.reverse()


def array_print(array):  # pragma: no cover
    out = [str(elem) for elem in array]
    out = ' '.join(out)
    print(out)


if __name__ == '__main__':  # pragma: no cover
    array = array_scan()
    array_reverse(array)
    print(array)