num=int(input("enter the number : "))
rev=0
original=num
if num<=0:
    print("enter the positive valve")
else:    
    while num>0:
         d = num % 10 # get the last digit
         rev= 10*rev + d
         num//=10 # remove the last digit  here ih the last iteration num == 0
    print("the reverse of the ",original,"is", rev)     