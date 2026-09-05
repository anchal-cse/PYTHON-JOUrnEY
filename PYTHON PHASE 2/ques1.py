# write a program in python to find the sum
# of n numbers entered by the user implementing using
# the loop. It should be noted that indentation is very
# important in python codes as they are used instead
# of brackets for separating various block of code.

n = int(input("Enter how many numbers: "))

total = 0

for i in range(n):
    num = int(input("Enter a number: "))
    total = total + num

print("Sum =", total)