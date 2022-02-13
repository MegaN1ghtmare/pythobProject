if __name__ == '__main__':
    number = int(input())

    digits = len(str(number))
    print('Build in standard func said: ', digits)

    counter = 0

    if number < 0 or number == 0:
        number *= -1
        counter += 1

    while number > 0:
        number = number // 10
        counter += 1

    print('Places needed for number: ', counter)
