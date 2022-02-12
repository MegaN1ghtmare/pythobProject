def array_scan():
    return [int(elem) for elem in input().strip().split()]

def array_increment(array, increment):
    for i in range(len(array)):
        array[i] += increment

def array_print(array):
    out = [str(elem) for elem in array]
    out = ' '.join(out)
    print(out)

if __name__ == '__main__':
    array = array_scan()
    increment = int(input())
    array_increment(array, increment)
    array_print(array)