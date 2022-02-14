import math

def gcd_function(x, y):
    if y == 0:
        return x
    print('x =', x, 'y =', y)
    return gcd_function(y, x % y)

if __name__ == '__main__':  # pragma: no cover
    data = input()
    data.strip()

    data = data.split()
    data = list(map(int, data))

    x, y = data

    print('GCD is: ', gcd_function(x, y))

    print('Imported function said: ', math.gcd(x, y))