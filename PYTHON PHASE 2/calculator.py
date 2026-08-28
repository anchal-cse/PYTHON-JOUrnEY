x=int(input('enter the first number: '))
y=int(input("enter second number : "))
op=input("enter the operator : ")
match op:
    case "+":
        print(x+y)
    case "-":
        print(x-y)
    case "*":
        print(x*y)
    case "/":
        print(x/y)
    case _:
        print("invalid operator")