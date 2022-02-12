if __name__ == '__main__':
    multiple = int(input())
    isMultiple = 0

    if multiple % 2 == 0:
        print('alpha')
        isMultiple = 1
    if multiple % 3 == 0:
        print('bravo')
        isMultiple = 1
    if multiple % 5 == 0:
        print('charlie')
        isMultiple = 1
    if isMultiple == 0:
        print('zulu')