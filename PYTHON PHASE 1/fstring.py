# name='anchal'
# age=19
# print(f'my name is {name} and \n my age is {age}')

# var = 20
# print(f"{var}")
# print(f"{var=}") # 7 or 8
# print(f"var = {var}")
# print(f"{1 + 1 = }")


name = "Bob" # Padding and Alignment

print(f"|{name:<10}|")  # Left aligned
print(f"|{name:>10}|")  # Right aligned
print(f"|{name:^10}|")  # Center aligned

print("\n")
print(f"|{name:_<10}|")  # Left aligned
print(f"|{name:_>10}|")  # Right aligned
print(f"|{name:_^10}|")  # Center aligned

print("\n")
print(f"{name:<10}hello bob")  # Left aligned
print(f"{name:.>10}")  # Right aligned
print(f"{name:.^10}")  # Center aligned

name = "Bob"

print(f"|{name:<10}|")  # Left aligned
print(f"|{name:>10}|")  # Right aligned
print(f"|{name:^10}|")  # Center aligned

print("\n")
a = 50

print(f"|{name:<{a}}|")  # Left aligned
print(f"|{name:>{a}}|")  # Right aligned
print(f"|{name:^{a}}|")  # Center aligned

num = 255

print(f"Decimal: {num}")
print(f"Binary : {num:b}")
print(f"Hex    : {num:x}")
print(f"Octal  : {num:o}")