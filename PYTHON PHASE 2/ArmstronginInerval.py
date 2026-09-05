n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

for num in range(n1, n2 + 1):
    a=num
    total=0
    while a>0:
        d=a%10
        total+=(d*d*d)
        a=a//10

    if total==num:
       print(total) #Yes, you can use sum as the variable name. Your program will work, but it is better practice to use total because Python already has a built-in function called sum().