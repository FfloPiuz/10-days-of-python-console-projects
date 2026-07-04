import random as r

chars = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?"
]

length = int(input("Enter length of password: "))

password = []

for i in range(length):
    rand_char = chars[r.randint(0, len(chars) - 1)]
    password.append(rand_char)

print("".join(password))