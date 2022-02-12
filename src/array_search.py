def array_scan():
    return [int(elem) for elem in input().strip().split()]

def array_search_elem_index(array, elem):
    return array.index(elem)

def array_print(array):
    out = [str(elem) for elem in array]
    out = ' '.join(out)
    print(out)

if __name__ == '__main__':
    array = array_scan()
    elem = int(input())
    print(array_search_elem_index(array, elem))