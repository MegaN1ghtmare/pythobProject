def array_scan():  # pragma: no cover
    return [int(elem) for elem in input().strip().split()]


def array_increment(array):  # pragma: no cover
    for i in range(len(array)):
        array[i] += 1


def array_print(array):  # pragma: no cover
    out = [str(elem) for elem in array]
    out = ' '.join(out)
    print(out)


if __name__ == '__main__':  # pragma: no cover
    array = array_scan()
    array_increment(array)
    array_print(array)