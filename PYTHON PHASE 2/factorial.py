## Factorial using a loop

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.") # if num=0
else:                                                        # range(1,1)
    for i in range(1, num + 1):                              # no iteration
        factorial = factorial * i                             # but still fact=1
    print("Factorial of", num, "is", factorial)              # so 0 fact is 1                                                                                 