from alphabets import alph_lower, alph_upper

alph_lower_len = len(alph_lower)
alph_upper_len = len(alph_upper)


def binary_lower(x):
    for i in range(alph_lower_len):
        if x == alph_lower[i]:
            value = ord(alph_lower[i])
            conv = bin(value)
            print(str(conv)[2:], end=" ")


def binary_upper(x):
    for i in range(alph_upper_len):
        if x == alph_upper[i]:
            value = ord(alph_upper[i])
            conv = bin(value)
            print(str(conv)[2:], end=" ")


def convert():
    text = input("Enter the text you want to convert : ")
    while text.isdigit():
        text = input("Enter the text you want to convert : ")

    text_list = list(text)
    for i in range(len(text_list)):
        if text_list[i].isupper():
            binary_upper(text_list[i])

        elif text_list[i].islower():
            binary_lower(text_list[i])


convert()
