a=int(input("enter first number:")) 
b=int(input("enter second number"))

print("first no.",a)
print("second no. is",b)

# c=a #with third variable
# a=b
# b=c

a=a+b #without third variable
b=a-b
a=a-b

print("swapped value of first and second no. is ",a,b)