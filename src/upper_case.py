if __name__ == '__main__':
    text = input()
    new_text = ""

    for char in text:
        if ord(char) >= 97 and ord(char) < 123:
            new_text += chr(ord(char) - 32)
        else:
            new_text += char

    print(new_text)

    uppercase_text = text.upper()
    print(uppercase_text)