n = int(input("Enter a decimal number: "))

print("Binary =", bin(n)[2:])
print("Octal =", oct(n)[2:])
print("Hexadecimal =", hex(n))   


#  here,
# bin(n) → decimal to binary
# oct(n) → decimal to octal
# hex(n) → decimal to hexadecimal
# [2:] → removes 0b, 0o, and 0x

n = int(input("Enter a decimal number: "))


# Decimal to Binary
a = n
binary = ""

while a > 0:
    r = a % 2
    binary = str(r) + binary
    a = a // 2

# Decimal to Octal
a = n
octal = ""

while a > 0:
    r = a % 8
    octal = str(r) + octal
    a = a // 8

# Decimal to Hexadecimal
a = n
hexa = ""

while a > 0:
    r = a % 16

    if r < 10:
        hexa = str(r) + hexa
    else:
        hexa = chr(55 + r) + hexa

    a = a // 16

print("Binary =", binary)
print("Octal =", octal)
print("Hexadecimal =", hexa)