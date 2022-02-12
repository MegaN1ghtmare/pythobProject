if __name__ == '__main__':
    data = input()
    data.strip()

    data = data.split()
    data = list(map(int, data))

    print(max(data))