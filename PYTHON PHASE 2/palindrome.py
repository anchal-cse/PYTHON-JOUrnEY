x=int(input('enter the first number: '))
temp=x
rev=0
while temp!=0 :
    d = temp%10
    rev= (10*rev + d)
    temp=temp//10
if rev==x:
   print("palindrome")
else :   
   print("not a palindrome")