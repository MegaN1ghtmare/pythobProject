if __name__ == '__main__':  # pragma: no cover
    data = input()
    data.strip()

    data = data.split()
    data = list(map(int, data))

    print(max(data))